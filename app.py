import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Portfólio de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo customizado
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    .main {
        padding-top: 2rem;
    }
    h1 {
        color: #1f77b4;
        text-align: center;
    }
    h2 {
        color: #1f77b4;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Navegação lateral
with st.sidebar:
    st.markdown("### 👤 Seu Nome")
    st.markdown("**Analista de Dados | Cientista de Dados**")
    
    page = st.radio(
        "Navegação",
        ["🏠 Home", "👤 Sobre Mim", "📊 Projetos", "✉️ Contato"],
        label_visibility="collapsed"
    )

# Roteamento de páginas
if page == "🏠 Home":
    from pages import home
    home.show()
elif page == "👤 Sobre Mim":
    from pages import about
    about.show()
elif page == "📊 Projetos":
    from pages import projects
    projects.show()
elif page == "✉️ Contato":
    from pages import contact
    contact.show()
