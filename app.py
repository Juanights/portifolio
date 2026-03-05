import streamlit as st

st.set_page_config(
    page_title="Portfólio | Analista de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Profissional - Paleta Deep Tech
st.markdown("""
    <style>
    /* Paleta de Cores Profissional */
    :root {
        --primary-dark: #0f172a;
        --primary-blue: #1e40af;
        --secondary-blue: #3b82f6;
        --slate-600: #475569;
        --slate-400: #94a3b8;
        --bg-light: #f8fafc;
        --bg-lighter: #f1f5f9;
        --border: #e2e8f0;
    }
    
    /* Remover espaçamento excessivo */
    .main {
        padding-top: 0.5rem;
    }
    
    /* Tipografia */
    h1 {
        color: #0f172a;
        font-weight: 700;
        font-size: 2.25rem;
        margin-bottom: 0.25rem;
        letter-spacing: -0.02em;
    }
    
    h2 {
        color: #0f172a;
        font-weight: 600;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    h3 {
        color: #1e40af;
        font-weight: 600;
        font-size: 1.125rem;
    }
    
    p, li {
        color: #475569;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #1e40af;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.6rem 1.2rem;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #1e3a8a;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3);
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #eff6ff 0%, #f0f9ff 100%);
        border-left: 3px solid #1e40af;
        border-radius: 6px;
        padding: 1.25rem;
        margin: 1rem 0;
    }
    
    .info-box h4 {
        color: #1e40af;
        margin-top: 0;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: #e2e8f0;
        margin: 2rem 0;
    }
    
    /* Métrica */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
    }
    
    /* Links */
    a {
        color: #1e40af;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: #1e3a8a;
        text-decoration: underline;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
    }
    
    [data-testid="stSidebar"] h1 {
        font-size: 1.5rem;
        color: #0f172a;
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        border: 1px solid #e2e8f0;
        border-radius: 6px;
    }
    
    /* Table */
    [data-testid="stDataFrame"] {
        background-color: #f8fafc;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Navegação Profissional
with st.sidebar:
    st.markdown("## Portfólio")
    st.markdown("*Analista de Dados | Ciência de Dados*")
    st.markdown("---")
    
    page = st.radio(
        "Navegação",
        ["Início", "Sobre", "Projetos", "Contato"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    **Desenvolvido com:**  
    Python • Streamlit • Plotly
    """)

# Roteamento de páginas
if page == "Início":
    from pages import home
    home.show()
elif page == "Sobre":
    from pages import about
    about.show()
elif page == "Projetos":
    from pages import projects
    projects.show()
elif page == "Contato":
    from pages import contact
    contact.show()
