import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Portfólio de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Minimalista - Apenas o essencial
st.markdown("""
    <style>
    /* Cores e Tipografia Base */
    :root {
        --primary: #0F766E;
        --text-dark: #1F2937;
        --text-light: #6B7280;
        --bg-light: #F9FAFB;
        --border: #E5E7EB;
    }
    
    /* Remover espaçamento excessivo */
    .main {
        padding-top: 1rem;
    }
    
    /* Tipografia */
    h1 {
        color: #1F2937;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: #1F2937;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #374151;
        font-weight: 600;
    }
    
    p, li {
        color: #4B5563;
        line-height: 1.6;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #0F766E;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #0D5D56;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.2);
    }
    
    /* Cards */
    .card {
        background: white;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: #0F766E;
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.1);
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #E0F2FE 0%, #F0F9F8 100%);
        border-left: 4px solid #0F766E;
        border-radius: 6px;
        padding: 1.25rem;
        margin: 1rem 0;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #E5E7EB, transparent);
        margin: 2rem 0;
    }
    
    /* Métrica */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #F9FAFB 0%, #F3F4F6 100%);
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    /* Links */
    a {
        color: #0F766E;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: #0D5D56;
        text-decoration: underline;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F9FAFB;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Portfólio de Dados")
    st.markdown("*Análise de Dados & Ciência de Dados*")
    st.markdown("---")
    
    page = st.radio(
        "Navegação",
        ["🏠 Home", "👤 Sobre Mim", "📊 Projetos", "✉️ Contato"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    **Desenvolvido com:**  
    🐍 Python • 🎨 Streamlit • 📊 Plotly
    """)

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
