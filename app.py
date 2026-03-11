import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import base64
import requests


def load_image_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

st.set_page_config(
    page_title="Portfólio | Juan Uchise",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Cyber-Executive - Dark Purple & Neon Green
st.markdown("""
    <style>
    /* Paleta Cyber-Executive */
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background-color: #0F0718;
        color: #E0E7FF;
    }
    
    /* Main Container */
    [data-testid="stAppViewContainer"]{
    background-color:#0F0718;
    padding: 2rem;
    }
    
    /* Tipografia */
    h1 {
        color: #E0E7FF;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        text-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }
    
    h2 {
        color: #10B981;
        font-weight: 600;
        font-size: 1.875rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
        text-shadow: 0 0 15px rgba(16, 185, 129, 0.2);
    }
    
    h3 {
        color: #10B981;
        font-weight: 600;
        font-size: 1.25rem;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    p, li {
        color: #CBD5E1;
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    /* Botões Neon - Sidebar */
    [data-testid="stSidebar"] .stButton > button {
        background-color: rgba(16,185,129,0.05) !important;
    color: #10B981 !important;

    border-left: 2px solid #10B981 !important;

    text-shadow:
        0 0 5px #10B981,
        0 0 10px #10B981,
        0 0 20px #10B981;

    box-shadow:
        inset 0 0 10px rgba(16,185,129,0.25),
        0 0 10px rgba(16,185,129,0.3);

    transform: translateX(3px);

    transition: all 0.25s ease;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: transparent;
        color: #10B981;
        border: none;
        box-shadow: none;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
        transform: none;
    }
    
    [data-testid="stSidebar"] .stButton > button:focus {
        background-color: transparent;
        color: #10B981;
        border: none;
        box-shadow: none;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
    }
    
    /* Botões Neon - Conteúdo Principal */
    .main .stButton > button {
        background-color: transparent;
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.7rem 1.5rem;
        transition: all 0.3s ease;
        box-shadow: none;
    }
    
    .main .stButton > button:hover {
        background-color: rgba(16, 185, 129, 0.1);
        color: #10B981;
        border: 1px solid #10B981;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.4);
        text-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
        transform: translateY(-1px);
    }
    
    /* HUD Card */
    .hud-card {
        background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 100%);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 4px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 0 8px rgba(16, 185, 129, 0.1);
        position: relative;
    }
    
    .hud-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #10B981, transparent);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #10B981, transparent);
        margin: 2rem 0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0F0718;
        border-right: 1px solid rgba(16, 185, 129, 0.2);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #E0E7FF;
    }
    
    /* Radio Buttons */
    [data-testid="stRadio"] label {
        color: #CBD5E1;
        font-weight: 500;
    }
    
    [data-testid="stRadio"] [role="radio"] {
        accent-color: #10B981;
    }
    
    /* Metric */
    .stMetric {
        background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 100%);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 4px;
        padding: 1rem;
        box-shadow: 0 0 5px rgba(16, 185, 129, 0.1);
    }
    
    [data-testid="stMetricLabel"] {
        color: #CBD5E1;
    }
    
    [data-testid="stMetricValue"] {
        color: #10B981;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }
    
    /* Expandable */
    [data-testid="stExpander"] {
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 4px;
        background-color: #1A0F2E;
    }
    
    [data-testid="stExpander"] summary {
        color: #10B981;
        font-weight: 600;
    }
    
    /* Input Fields */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea {
        background-color: #1A0F2E;
        color: #E0E7FF;
        border: 1px solid rgba(16, 185, 129, 0.25);
    }
    
    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus {
        border-color: #10B981;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }
    
    /* Icon-like elements */
    .icon-neon {
        color: #10B981;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }
    
    /* Highlight */
    .highlight-neon {
        color: #10B981;
        font-weight: 600;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
    }
    
    /* Navigation Icons Menu */
    .nav-icons-container {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        margin: 0.5rem 0;
        padding: 0;
    }
    
    .nav-icon-btn {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.5rem 0.5rem;
        background-color: transparent;
        border: none;
        border-radius: 0;
        color: #CBD5E1;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 500;
        font-size: 0.95rem;
        text-align: left;
        width: 100%;
    }
    
    .nav-icon-btn:hover {
        border: none;
        color: #10B981;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }
    
    .nav-icon-btn.active {
        background-color: transparent;
        border: none;
        color: #10B981;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.5);
        text-shadow: 0 0 8px rgba(16, 185, 129, 0.6);
    }
    
    .nav-icon {
        font-size: 1.25rem;
        min-width: 1.5rem;
        text-align: center;
    }
            
            .education-container{
    display:flex;
    gap:25px;
    margin-top:20px;
}

.edu-card{
    flex:1;
    padding:20px;
    border-radius:6px;
    background: linear-gradient(135deg,#1A0F2E,#0F0718);
    border:1px solid rgba(16,185,129,0.25);
    transition: all 0.35s ease;
}

.edu-card:hover{

    transform: translateY(-6px);

    border:1px solid #10B981;

    box-shadow:
        0 0 10px rgba(16,185,129,0.3),
        0 0 20px rgba(16,185,129,0.3),
        inset 0 0 10px rgba(16,185,129,0.2);
}

.edu-card h4{
    color:#10B981;
}

.edu-tags{
    margin-top:10px;
}

.edu-tags span{

    display:inline-block;
    margin:4px;
    padding:4px 10px;

    border:1px solid #10B981;
    border-radius:20px;

    font-size:0.8rem;

    color:#10B981;

    box-shadow:0 0 6px rgba(16,185,129,0.3);
}
            .badge-container{

display:flex;
gap:25px;
margin-top:20px;

}

.badge-card{

flex:1;
padding:20px;

text-align:center;

background:linear-gradient(135deg,#1A0F2E,#0F0718);

border:1px solid rgba(16,185,129,0.25);

border-radius:6px;

transition:all 0.35s ease;

}

.badge-card:hover{

transform:translateY(-6px);

border:1px solid #10B981;

box-shadow:
0 0 12px rgba(16,185,129,0.4),
inset 0 0 10px rgba(16,185,129,0.2);

}

.badge-card h4{

color:#10B981;
margin-top:10px;

}

.language-bar{

margin-top:10px;

height:8px;

background:#1A0F2E;

border-radius:10px;

}

.language-progress{

height:100%;
width:45%;

background:#10B981;

border-radius:10px;

box-shadow:0 0 8px rgba(16,185,129,0.6);

}
.skills-container{

display:grid;
grid-template-columns:repeat(2,1fr);

gap:20px;
margin-top:20px;

}

.skill-category{

padding:18px;

background:linear-gradient(135deg,#1A0F2E,#0F0718);

border:1px solid rgba(16,185,129,0.25);

border-radius:6px;

}

.skill-category h4{

color:#10B981;
margin-bottom:10px;

}

.skill-badge{

display:inline-block;

margin:4px;
padding:6px 12px;

font-size:0.85rem;

border-radius:20px;

border:1px solid #10B981;

color:#10B981;

transition:all 0.3s ease;

}

.skill-badge:hover{

background:#10B981;

color:#0F0718;

box-shadow:
0 0 10px rgba(16,185,129,0.6),
0 0 20px rgba(16,185,129,0.4);

}
            
.hero{
padding:40px 10px 20px 10px;
}

.hero-title{
font-size:48px;
font-weight:700;
color:#E5E7EB;
margin-bottom:10px;
}

.hero-sub{
font-size:20px;
color:#9CA3AF;
max-width:700px;
}
.hero-buttons{

display:flex;

gap:20px;

margin-top:20px;

}

.hero-link{

display:flex;

align-items:center;

gap:8px;

padding:8px 16px;

border:1px solid #10B981;

border-radius:6px;

text-decoration:none;

color:#10B981 !important;

font-weight:600;

transition:all 0.3s ease;

}

.hero-link span{
color:#10B981;
}


/* hover */

.hero-link:hover{

background:#10B981;

color:#0F0718 !important;

box-shadow:
0 0 12px rgba(16,185,129,0.7),
0 0 24px rgba(16,185,129,0.5);

transform:translateY(-2px);

}

.hero-link:hover span{
color:#0F0718;
}

.hero-link img{

width:20px;

height:20px;

filter:drop-shadow(0 0 4px rgba(16,185,129,0.6));

}

.hero-link:hover{

background:#10B981;

color:#0F0718;

box-shadow:
0 0 12px rgba(16,185,129,0.7),
0 0 24px rgba(16,185,129,0.5);

transform:translateY(-2px);

}
            
.profile-card{

padding:20px;

background:linear-gradient(145deg,#0F172A,#020617);

border-radius:10px;

border:1px solid rgba(16,185,129,0.25);

box-shadow:0 0 10px rgba(16,185,129,0.15);

transition:0.3s;

}

.profile-card:hover{

transform:translateY(-5px);

box-shadow:
0 0 15px rgba(16,185,129,0.4);

}

.tech-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(120px,1fr));

gap:20px;

margin-top:20px;

}

.tech-card{

text-align:center;

padding:15px;

border-radius:8px;

background:#020617;

border:1px solid rgba(16,185,129,0.2);

transition:0.3s;

}

.tech-card img{
width:40px;
height:40px;
margin-bottom:6px;
filter: drop-shadow(0 0 6px rgba(16,185,129,0.5));
}

.tech-card:hover{

transform:translateY(-5px);

border:1px solid #10B981;

box-shadow:
0 0 10px rgba(16,185,129,0.4);

}
.gallery{
display:grid !important;
grid-template-columns: 1fr 1fr !important;
gap:20px;
width:100%;
}

.card{
position:relative;
width:50%;
border-radius:14px;
overflow:hidden;
cursor:pointer;
height: 400px;            
}

.card img{
width:100%;
aspect-ratio:16/9;
object-fit:cover;
display:block;
}


.card:hover img{
transform:scale(1.06);
}

.overlay{
position:absolute;
top:0;
left:0;
width:100%;
height:100%;
background:rgba(15,7,24,0.88);
opacity:0;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
padding:20px;
transition:0.3s;
}

.card:hover .overlay{
opacity:1;
}

.overlay h3{
margin-bottom:10px;
}

.overlay p{
font-size:14px;
opacity:0.85;
}

.tags{
margin-top:10px;
display:flex;
gap:6px;
flex-wrap:wrap;
justify-content:center;
}

.tag{
border:1px solid rgba(16,185,129,0.5);
color:#10B981;
padding:3px 8px;
font-size:11px;
border-radius:6px;
}

.buttons{
margin-top:12px;
display:flex;
gap:10px;
}

.btn{
border:1px solid #10B981;
color:#10B981;
padding:6px 12px;
border-radius:6px;
text-decoration:none;
font-size:13px;
}

.btn:hover{
background:#10B981;
color:#0F0718;
}

/* ===== NETFLIX CARD HOVER ===== */
.netflix-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 16px;
}

.netflix-card {
    position: relative;
    border-radius: 10px;
    overflow: hidden;
    aspect-ratio: 16/9;
    cursor: pointer;
    border: 1px solid rgba(16,185,129,0.15);
    background: #1A0F2E;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.netflix-card:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 32px rgba(16,185,129,0.25), 0 0 0 1px rgba(16,185,129,0.4);
    z-index: 10;
}

.netflix-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: filter 0.4s ease;
}

.netflix-card:hover img {
    filter: brightness(0.25) saturate(0.5);
}

.netflix-overlay {
    position: absolute;
    inset: 0;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    background: linear-gradient(to top, rgba(15,7,24,0.95) 0%, rgba(15,7,24,0.4) 50%, transparent 100%);
    transition: background 0.4s ease;
}

.netflix-card:hover .netflix-overlay {
    background: rgba(15,7,24,0.0);
    justify-content: center;
    align-items: flex-start;
}

.netflix-title {
    color: #E0E7FF;
    font-size: 1rem;
    font-weight: 700;
    margin: 0 0 4px 0;
    text-shadow: 0 2px 8px rgba(0,0,0,0.8);
    transition: all 0.4s ease;
}

.netflix-status {
    font-size: 0.7rem;
    padding: 2px 8px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 6px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.netflix-desc {
    color: #CBD5E1;
    font-size: 0.82rem;
    line-height: 1.5;
    margin: 0 0 12px 0;
    opacity: 0;
    transform: translateY(10px);
    transition: opacity 0.4s ease 0.1s, transform 0.4s ease 0.1s;
}

.netflix-card:hover .netflix-desc {
    opacity: 1;
    transform: translateY(0);
}

.netflix-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    opacity: 0;
    transform: translateY(10px);
    transition: opacity 0.4s ease 0.2s, transform 0.4s ease 0.2s;
}

.netflix-card:hover .netflix-tags {
    opacity: 1;
    transform: translateY(0);
}

.netflix-card:hover .netflix-title {
    color: #10B981;
    text-shadow: 0 0 12px rgba(16,185,129,0.6);
}

.netflix-card:hover .netflix-status {
    opacity: 0;
}

.netflix-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 50%, #1A0F2E 100%);
    font-size: 3rem;
    color: rgba(16,185,129,0.3);
    letter-spacing: 2px;
}
.contact-card{
background: rgba(255,255,255,0.02);
border:1px solid rgba(16,185,129,0.2);
border-radius:14px;
padding:24px;
transition:0.3s;
}

.contact-card:hover{
border:1px solid #10B981;
box-shadow:0 0 12px rgba(16,185,129,0.35);
transform:translateY(-3px);
}

.contact-buttons{
display:flex;
gap:12px;
margin-top:15px;
flex-wrap:wrap;
}

.contact-btn{
display:flex;
align-items:center;
gap:8px;
border:1px solid #10B981;
padding:8px 14px;
border-radius:8px;
text-decoration:none;
color:#10B981;
font-size:14px;
transition:0.25s;
}

.contact-btn img{
width:18px;
}

.contact-btn:hover{
background:#10B981;
color:#0F0718;
}

.cta-box{
text-align:center;
padding:20px;
margin-bottom:25px;
}          


</style>
    """, unsafe_allow_html=True)

# Inicializar session_state para navegação
if "page" not in st.session_state:
    st.session_state.page = "Início"

# Sidebar - Navegação Cyber-Executive
with st.sidebar:
    # Foto de Perfil com Efeito Neon Circular
    import os
    import base64
    
    perfil_path = "Perfil.png"
    
    if os.path.exists(perfil_path):
        with open(perfil_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()
        
        st.markdown(f"""
        <div style='text-align: center; margin-bottom: 1rem;'>
            <img src='data:image/jpeg;base64,{img_base64}' 
                 style='width: 150px; height: 150px; border-radius: 50%; 
                        border: 1px solid #10B981; 
                        box-shadow: 0 0 8px rgba(16, 185, 129, 0.3);
                        object-fit: cover; display: block; margin: 0 auto;'>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 1rem;'>
            <div style='width: 150px; height: 150px; margin: 0 auto; 
                        border: 1px solid #10B981; border-radius: 50%; 
                        display: flex; align-items: center; justify-content: center; 
                        font-size: 3rem; background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 100%); 
                        box-shadow: 0 0 8px rgba(16, 185, 129, 0.3);'>
                👤
            </div>
            <p style='text-align: center; color: #CBD5E1; font-size: 0.85rem; margin-top: 0.5rem;'><em>Adicione perfil.jpg</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## Portfólio - Juan Uchise")
    st.markdown("*Analista de Dados | Ciência de Dados*")
    st.markdown("---")
    
    # Menu de Navegação com Ícones Neon
    st.markdown("<div class='nav-icons-container'>", unsafe_allow_html=True)
    
    nav_items = [
        ("Início", "🏠"),
        ("Sobre mim", "👤"),
        ("Projetos", "📊"),
        ("Storytelling", "📖"),
        ("Contato", "✉️")
    ]
    
    for page_name, icon in nav_items:
        is_active = st.session_state.page == page_name
        active_class = "active" if is_active else ""
        
        if st.button(
            f"{icon} {page_name}",
            key=f"nav_{page_name}",
            use_container_width=True
        ):
            st.session_state.page = page_name
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    **Desenvolvido com:**  
    🐍 Python • ⚡ Streamlit • 📊 Plotly
    """)

def show_home():

    # HERO
    st.markdown("""
    <div class="hero">

    <h1 class="hero-title">
    Juan Uchise
    </h1>

    <p class="hero-sub">
    Analista de Dados • Ciência de Dados • Machine Learning
    </p>

    <div class="hero-buttons">

    <a href="https://github.com/juanights" target="_blank" class="hero-link">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg">
    <span>GitHub</span>
    </a>

    <a href="https://www.linkedin.com/in/juan-uchise/" target="_blank" class="hero-link">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg">
    <span>LinkedIn</span>
    </a>

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # BIO + PROFILE
    col1, col2 = st.columns([2,1], gap="large")

    with col1:
        st.markdown("""
        ## Visão Geral

        Profissional em transição para a área de dados com foco em:

        • **Análise Exploratória de Dados (EDA)**  
        • **Machine Learning e Modelagem Preditiva**  
        • **Business Intelligence**  
        • **Storytelling com Dados**

        Meu objetivo é transformar **dados complexos em insights acionáveis**
        que apoiem decisões estratégicas.
        """)

    with col2:
        st.markdown("""
        <div class="profile-card">

        <h4>Resumo profissional</h4>

        <p>🎓 <strong>Formação</strong><br>
        Ciência de Dados</p>

        <p>🌎 <b>Localização</b><br>
        Brasil</p>

        <p>📊 <b>Experiência</b><br>
        Início de carreira em dados</p>

        <p>🚀 <b>Status</b><br>
        Aberto a oportunidades</p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # METRICS
    st.markdown("## Destaques")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Projetos", "2+", "em desenvolvimento")

    with col2:
        st.metric("Linguagens", "Python • SQL", "R")

    with col3:
        st.metric("Ferramentas", "Power BI • Excel", "Tableau")

    st.markdown("---")

    # TECH STACK
    st.markdown("## Tech Stack")

    st.markdown("""
    <div class="tech-grid">

    <div class="tech-card">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
    <p>Python</p>
    </div>

    <div class="tech-card">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg">
    <p>Pandas</p>
    </div>

    <div class="tech-card">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg">
    <p>NumPy</p>
    </div>

    <div class="tech-card">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg">
    <p>SQL</p>
    </div>

    <div class="tech-card">
    <img src="https://streamlit.io/images/brand/streamlit-mark-color.png">
    <p>Streamlit</p>
    </div>

    <div class="tech-card">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg">
    <p>Power BI</p>
    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # EXPLORE
    st.markdown("## Explore o Portfólio")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Projetos", use_container_width=True):
            st.session_state.page = "Projetos"
            st.rerun()

    with col2:
        if st.button("Sobre mim", use_container_width=True):
            st.session_state.page = "Sobre mim"
            st.rerun()

    with col3:
        if st.button("Storytelling", use_container_width=True):
            st.session_state.page = "Storytelling"
            st.rerun()

    with col4:
        if st.button("Contato", use_container_width=True):
            st.session_state.page = "Contato"
            st.rerun()

def show_about():
    st.markdown("# <span class='icon-neon'>◆</span> Sobre Mim", unsafe_allow_html=True)
    st.write("""
Sou estudante de Ciência de Dados e Inteligência Artificial focado em análise de dados,
machine learning e visualização. Tenho experiência com Python, SQL e ferramentas de BI
para transformar dados em insights.
""")
    st.markdown("---")
    
    st.markdown("""
    <div class="hud-card">

    <h3 style="color:#10B981;">⬥ Formação Acadêmica</h3>

    <div class="education-container">

    <div class="edu-card">

    <h4>🎓 Graduação</h4>

    <p><strong>Curso:</strong> Análise e Desenvolvimento de Sistemas</p>
    <p><strong>Instituição:</strong> UNICID</p>
    <p><strong>Período:</strong> 2023 - 2025</p>

    <div class="edu-tags">
    <span>Python</span>
    <span>SQL</span>
    <span>Power BI</span>
    </div>

    </div>

    <div class="edu-card">

    <h4>📚 Pós-graduação</h4>

    <p><strong>Curso:</strong> Ciência de Dados e IA</p>
    <p><strong>Instituição:</strong> UNINTER</p>
    <p><strong>Conclusão:</strong> 06/2026</p>

    <div class="edu-tags">
    <span>Machine Learning</span>
    <span>Estatística</span>
    <span>Modelagem</span>
    </div>

    </div>

    </div>

    <h4 style="margin-top:25px;">Projetos Acadêmicos</h4>

    <ul>
    <li>Modelo de classificação com RandomForest</li>
    <li>Dashboard interativo de análise de vendas</li>
    <li>Análise exploratória de dataset público</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hud-card">

    <h3 style="color:#10B981;">⬥ Certificações & Idiomas</h3>

    <div class="badge-container">

    <div class="badge-card">

    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" width="60">

    <h4>Google Data Analytics</h4>

    <p>Google | 2025</p>
    <p>Professional Certificate</p>
    <a href="https://www.coursera.org/account/accomplishments/specialization/certificate/WZXH5MS66WCB" target="_blank">
        Ver credencial
    </a>

    </div>

    <div class="badge-card">

    <h4>🌎 English</h4>

    <p>Basic → Intermediate</p>

    <div class="language-bar">
    <div class="language-progress"></div>
    </div>

    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Competências Técnicas")

    st.markdown("""
    <div class="skills-container">

    <div class="skill-category">
    <h4>Linguagens</h4>

    <span class="skill-badge">Python</span>
    <span class="skill-badge">SQL</span>
    <span class="skill-badge">R</span>
    <span class="skill-badge">JavaScript</span>

    </div>

    <div class="skill-category">
    <h4>Data Science</h4>

    <span class="skill-badge">Pandas</span>
    <span class="skill-badge">NumPy</span>
    <span class="skill-badge">Scikit-learn</span>
    <span class="skill-badge">Plotly</span>

    </div>

    <div class="skill-category">
    <h4>Bancos de Dados</h4>

    <span class="skill-badge">MySQL</span>
    <span class="skill-badge">SQL Server</span>

    </div>

    <div class="skill-category">
    <h4>BI & Apps</h4>

    <span class="skill-badge">Power BI</span>
    <span class="skill-badge">Excel/Sheets</span>
    <span class="skill-badge">Streamlit</span>

    </div>

    </div>
    """, unsafe_allow_html=True)

def show_projects():
    import base64, os

    def get_img_base64(path):
        """Converte imagem local para base64. Retorna None se não encontrar."""
        if path and os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        return None

    st.markdown("# <span class='icon-neon'>◆</span> Projetos", unsafe_allow_html=True)
    st.markdown("Portfólio de projetos em Análise de Dados e Ciência de Dados")
    st.markdown("---")

    # Definição dos projetos
    # Para adicionar imagem: coloque o arquivo na pasta 'images/' e informe o caminho em 'cover'
    projects = [
        {
            "title": "Análise de Vendas",
            "description": "Dashboard de vendas com análise regional, KPIs estratégicos e visualização de tendências mensais. Identificação de padrões sazonais e oportunidades de crescimento.",
            "tech": ["Python", "Pandas", "Power BI"],
            "github": "#",
            "dashboard": "#",
            "status": "Concluído",
            "cover": "images/capa_vendas.png"   # substitua pelo caminho da sua imagem
        },
        {
            "title": "Dashboard Financeiro",
            "description": "Visualização financeira com indicadores de receita, lucro e margem. Análise de fluxo de caixa e projeções baseadas em séries temporais.",
            "tech": ["SQL", "Power BI"],
            "github": "#",
            "dashboard": "#",
            "status": "Concluído",
            "cover": "images/capa_financeiro.png"
        },
        {
            "title": "Análise de Clientes",
            "description": "Exploração de dados para identificar padrões de comportamento e segmentação de clientes. Modelo de clustering para personalização de ofertas.",
            "tech": ["Python", "Pandas", "Streamlit"],
            "github": "#",
            "dashboard": "#",
            "status": "Em desenvolvimento",
            "cover": "images/capa_clientes.png"
        },
        {
            "title": "Modelo Preditivo — Churn",
            "description": "Modelo de Machine Learning para prever cancelamento de clientes com Random Forest e XGBoost. Acurácia de 87% em validação cruzada.",
            "tech": ["Python", "Scikit-learn", "Pandas"],
            "github": "#",
            "dashboard": "#",
            "status": "Em desenvolvimento",
            "cover": "images/capa_churn.png"
        },
    ]

    # Filtro por tecnologia
    all_techs = sorted(set(t for p in projects for t in p["tech"]))
    techs = ["Todos"] + all_techs

    col_filter, _ = st.columns([1, 3])
    with col_filter:
        selected = st.selectbox("Filtrar por tecnologia", techs, label_visibility="collapsed")

    filtered_projects = projects if selected == "Todos" else [p for p in projects if selected in p["tech"]]

    st.markdown("")

    # Renderização Netflix-style: grid HTML puro para garantir hover CSS
    cards_html = "<div class='netflix-grid'>"

    for p in filtered_projects:
        img_b64 = get_img_base64(p["cover"])
        status_color = "#10B981" if p["status"] == "Concluído" else "#F59E0B"
        tags_html = "".join([f"<span class='tag'>{t}</span>" for t in p["tech"]])

        if img_b64:
            img_tag = f"<img src='data:image/png;base64,{img_b64}' alt='{p['title']}' />"
        else:
            # Placeholder estilizado quando não há imagem
            img_tag = f"<div class='netflix-placeholder'>◆ {p['title'][:2].upper()}</div>"

        cards_html += f"""
        <div class="netflix-card">
            {img_tag}
            <div class="netflix-overlay">
                <span class="netflix-status" style="color:{status_color}; border:1px solid {status_color};">{p['status']}</span>
                <p class="netflix-title">◆ {p['title']}</p>
                <p class="netflix-desc">{p['description']}</p>
                <div class="netflix-tags">
                    {tags_html}
                    <div style="display:flex; gap:8px; margin-top:8px;">
                        <a href="{p['github']}" target="_blank" class="btn" style="font-size:11px; padding:4px 10px;">Código</a>
                        <a href="{p['dashboard']}" target="_blank" class="btn" style="font-size:11px; padding:4px 10px;">Dashboard</a>
                    </div>
                </div>
            </div>
        </div>
        """

    cards_html += "</div>"

    # CSS do efeito Netflix embutido no componente para garantir renderização correta
    full_html = f"""
    <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }}
    .netflix-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        padding: 4px;
    }}
    .netflix-card {{
        position: relative;
        border-radius: 10px;
        overflow: hidden;
        aspect-ratio: 16/9;
        cursor: pointer;
        border: 1px solid rgba(16,185,129,0.15);
        background: #1A0F2E;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .netflix-card:hover {{
        transform: scale(1.03);
        box-shadow: 0 8px 32px rgba(16,185,129,0.3), 0 0 0 1px rgba(16,185,129,0.5);
        z-index: 10;
    }}
    .netflix-card img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: filter 0.4s ease;
    }}
    .netflix-card:hover img {{
        filter: brightness(0.2) saturate(0.4);
    }}
    .netflix-overlay {{
        position: absolute;
        inset: 0;
        padding: 18px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        background: linear-gradient(to top, rgba(15,7,24,0.95) 0%, rgba(15,7,24,0.3) 55%, transparent 100%);
        transition: all 0.4s ease;
    }}
    .netflix-card:hover .netflix-overlay {{
        background: rgba(10,5,18,0.15);
        justify-content: center;
    }}
    .netflix-title {{
        color: #E0E7FF;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 4px;
        transition: all 0.4s ease;
    }}
    .netflix-card:hover .netflix-title {{
        color: #10B981;
        text-shadow: 0 0 14px rgba(16,185,129,0.7);
    }}
    .netflix-status {{
        font-size: 0.68rem;
        padding: 2px 8px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 6px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: opacity 0.3s ease;
    }}
    .netflix-card:hover .netflix-status {{
        opacity: 0;
    }}
    .netflix-desc {{
        color: #CBD5E1;
        font-size: 0.78rem;
        line-height: 1.5;
        margin-bottom: 10px;
        opacity: 0;
        transform: translateY(12px);
        transition: opacity 0.4s ease 0.1s, transform 0.4s ease 0.1s;
    }}
    .netflix-card:hover .netflix-desc {{
        opacity: 1;
        transform: translateY(0);
    }}
    .netflix-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        opacity: 0;
        transform: translateY(12px);
        transition: opacity 0.4s ease 0.2s, transform 0.4s ease 0.2s;
    }}
    .netflix-card:hover .netflix-tags {{
        opacity: 1;
        transform: translateY(0);
    }}
    .tag {{
        border: 1px solid rgba(16,185,129,0.6);
        color: #10B981;
        padding: 2px 8px;
        font-size: 10px;
        border-radius: 6px;
        background: rgba(16,185,129,0.08);
    }}
    .btn {{
        border: 1px solid #10B981;
        color: #10B981;
        padding: 4px 10px;
        border-radius: 6px;
        text-decoration: none;
        font-size: 11px;
        transition: all 0.2s ease;
        background: transparent;
    }}
    .btn:hover {{
        background: #10B981;
        color: #0F0718;
    }}
    .netflix-placeholder {{
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 50%, #1A0F2E 100%);
        font-size: 2.5rem;
        color: rgba(16,185,129,0.25);
        font-weight: 700;
        letter-spacing: 3px;
    }}
    </style>
    {cards_html}
    """

    import streamlit.components.v1 as components
    components.html(full_html, height=len(filtered_projects) * 220 + 60, scrolling=False)

def show_storytelling():
    st.markdown("# <span class='icon-neon'>◆</span> Análise de Impacto de Negócio", unsafe_allow_html=True)
    st.markdown("Uma narrativa de dados que transforma números em decisões")
    st.markdown("---")
    
    st.markdown("""
    <div class='hud-card'>
        <h3 style='color: #10B981;'>⬥ 1. O Problema</h3>
        <p>Uma empresa de varejo online enfrenta uma queda consistente na taxa de conversão de vendas nos últimos 6 meses. O time de negócios não consegue identificar se o problema está na qualidade do tráfego, no comportamento do cliente ou em fatores sazonais.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Dados Iniciais")
    np.random.seed(42)
    dates = pd.date_range('2023-09-01', periods=180, freq='D')
    conversion_data = pd.DataFrame({
        'Data': dates,
        'Taxa_Conversao': 4.5 - np.linspace(0, 2, 180) + np.random.normal(0, 0.3, 180),
        'Visitantes': np.random.randint(5000, 15000, 180),
        'Vendas': np.random.randint(200, 600, 180)
    })
    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=conversion_data['Data'],
        y=conversion_data['Taxa_Conversao'],
        mode='lines+markers',
        name='Taxa de Conversão (%)',
        line=dict(color='#10B981', width=3),
        marker=dict(size=6)
    ))
    fig1.update_layout(
        title="Tendência de Taxa de Conversão (6 meses)",
        xaxis_title="Data",
        yaxis_title="Taxa de Conversão (%)",
        template='plotly_dark',
        plot_bgcolor='#1A0F2E',
        paper_bgcolor='#0F0718',
        font=dict(color='#E0E7FF'),
        title_font_color='#10B981',
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("""
    <div class='hud-card'>
        <h3 style='color: #10B981;'>⬥ 2. A Exploração</h3>
        <p>Investigamos os dados em profundidade. Segmentamos por fonte de tráfego, dispositivo e período do dia para identificar padrões.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Taxa de Conversão por Fonte de Tráfego")
        traffic_data = pd.DataFrame({
            'Fonte': ['Orgânico', 'Pago', 'Social', 'Direto'],
            'Taxa': [3.2, 2.8, 1.5, 4.1]
        })
        fig2 = go.Figure(data=[
            go.Bar(x=traffic_data['Fonte'], y=traffic_data['Taxa'], marker_color='#10B981')
        ])
        fig2.update_layout(
            title="Por Fonte de Tráfego",
            template='plotly_dark',
            plot_bgcolor='#1A0F2E',
            paper_bgcolor='#0F0718',
            font=dict(color='#E0E7FF'),
            title_font_color='#10B981',
            height=350
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        st.markdown("### Taxa de Conversão por Dispositivo")
        device_data = pd.DataFrame({
            'Dispositivo': ['Desktop', 'Mobile', 'Tablet'],
            'Taxa': [3.8, 2.1, 2.9]
        })
        fig3 = go.Figure(data=[
            go.Bar(x=device_data['Dispositivo'], y=device_data['Taxa'], marker_color='#10B981')
        ])
        fig3.update_layout(
            title="Por Dispositivo",
            template='plotly_dark',
            plot_bgcolor='#1A0F2E',
            paper_bgcolor='#0F0718',
            font=dict(color='#E0E7FF'),
            title_font_color='#10B981',
            height=350
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("""
    <div class='hud-card'>
        <h3 style='color: #10B981;'>⬥ 3. O Insight Crítico</h3>
        <p><strong>Descoberta Principal:</strong> A taxa de conversão em dispositivos móveis caiu 45% em 6 meses, enquanto desktop permaneceu estável. Isso sugere um problema de experiência do usuário (UX) específico para mobile.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Evolução de Conversão: Desktop vs Mobile")
    mobile_data = pd.DataFrame({
        'Data': dates,
        'Desktop': 4.0 - np.linspace(0, 0.3, 180) + np.random.normal(0, 0.2, 180),
        'Mobile': 3.5 - np.linspace(0, 1.8, 180) + np.random.normal(0, 0.25, 180)
    })
    
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=mobile_data['Data'],
        y=mobile_data['Desktop'],
        mode='lines',
        name='Desktop',
        line=dict(color='#10B981', width=3)
    ))
    fig4.add_trace(go.Scatter(
        x=mobile_data['Data'],
        y=mobile_data['Mobile'],
        mode='lines',
        name='Mobile',
        line=dict(color='#10B981', width=3, dash='dash')
    ))
    fig4.update_layout(
        title="Divergência de Performance: Desktop vs Mobile",
        xaxis_title="Data",
        yaxis_title="Taxa de Conversão (%)",
        template='plotly_dark',
        plot_bgcolor='#1A0F2E',
        paper_bgcolor='#0F0718',
        font=dict(color='#E0E7FF'),
        title_font_color='#10B981',
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("""
    <div class='hud-card'>
        <h3 style='color: #10B981;'>⬥ 4. Recomendações de Ação</h3>
        <p>Com base nesta análise, recomendamos:</p>
        <ul>
            <li><strong>Auditoria de UX Mobile:</strong> Revisar o fluxo de checkout em dispositivos móveis (tempo de carregamento, clareza de botões, processo de pagamento).</li>
            <li><strong>Teste A/B:</strong> Implementar testes para otimizar a experiência mobile (simplificar formulários, aumentar tamanho de botões).</li>
            <li><strong>Monitoramento Contínuo:</strong> Acompanhar métricas de conversão por dispositivo em tempo real.</li>
            <li><strong>Impacto Financeiro Esperado:</strong> Recuperar 50% da queda em mobile = +R$ 150k em receita anual.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### Resumo Executivo")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("◆ Queda Total", "-44.4%", "-2.0 pp")
    with col2:
        st.metric("◆ Queda Mobile", "-51.4%", "-2.7 pp")
    with col3:
        st.metric("◆ Estabilidade Desktop", "-7.5%", "-0.3 pp")
    with col4:
        st.metric("◆ Oportunidade", "+R$ 150k", "Anual")

def show_contact():

    st.markdown("# <span class='icon-neon'>◆</span> Contato", unsafe_allow_html=True)

    st.markdown("""
    <div class='cta-box'>

    ### 🚀 Vamos trabalhar juntos?

    Se você procura alguém para transformar **dados em insights estratégicos**,  
    ficarei feliz em conversar sobre **projetos ou oportunidades em dados**.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class='contact-card'>

        <h3 style='color:#10B981;'>📬 Informações</h3>

        <p>📧 juan.uxz@gmail.com</p>
        <p>🌎 Brasil</p>

        <div class='contact-buttons'>

        <a class='contact-btn' href='https://github.com/juanights' target='_blank'>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg">
        GitHub
        </a>

        <a class='contact-btn' href='https://www.linkedin.com/in/juan-uchise/' target='_blank'>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg">
        LinkedIn
        </a>

        <a class='contact-btn' href='https://docs.google.com/document/d/1XtfdFV0CB9yeIDVarnMa-ihDCXUCR-CQ/edit?usp=drive_link&ouid=104338678762938389768&rtpof=true&sd=true' target='_blank'>
        📄 Baixar CV
        </a>

        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class='contact-card'>

        <h3 style='color:#10B981;'>🚀 Disponibilidade</h3>

        <p><strong>Status:</strong> Aberto a oportunidades</p>
        <p><strong>Modalidade:</strong> Remoto / Híbrido</p>
        <p><strong>Tempo de resposta:</strong> 24-48 horas</p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### ✉️ Envie uma mensagem")

    with st.form("contact_form", clear_on_submit=True):

        nome = st.text_input("Seu nome")
        email = st.text_input("Seu email")
        mensagem = st.text_area("Digite sua mensagem")

        submitted = st.form_submit_button("Enviar mensagem")

        if submitted:

            if not nome or not email or not mensagem:
                st.error("Preencha todos os campos.")
            else:

                url = "https://formspree.io/f/xreypjng"

                data = {
                    "name": nome,
                    "email": email,
                    "message": mensagem
                }

                response = requests.post(url, data=data)

                if response.status_code == 200:
                    st.success("✅ Mensagem enviada com sucesso!")
                else:
                    st.error("❌ Erro ao enviar mensagem.")

    

# Roteamento de Páginas
if st.session_state.page == "Início":
    show_home()
elif st.session_state.page == "Sobre mim":
    show_about()
elif st.session_state.page == "Projetos":
    show_projects()
elif st.session_state.page == "Storytelling":
    show_storytelling()
elif st.session_state.page == "Contato":
    show_contact()
