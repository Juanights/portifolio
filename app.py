import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Portfólio de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Customizado - Design Moderno e Minimalista
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF;
    }
    
    [data-testid="stSidebar"] {
        background-color: #F8FAFB;
        border-right: 1px solid #E5E7EB;
    }
    
    [data-testid="stSidebarContent"] {
        padding: 2rem 1.5rem;
    }
    
    .main {
        padding: 2rem;
    }
    
    /* Tipografia */
    h1 {
        color: #1F2937;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    h2 {
        color: #1F2937;
        font-size: 1.875rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        letter-spacing: -0.01em;
    }
    
    h3 {
        color: #374151;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    p, li {
        color: #4B5563;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }
    
    /* Cards Minimalistas */
    .card {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    .card:hover {
        border-color: #0F766E;
        box-shadow: 0 4px 12px rgba(15, 118, 110, 0.1);
    }
    
    .card-header {
        color: #0F766E;
        font-size: 1.125rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }
    
    .card-text {
        color: #6B7280;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #0F766E;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(15, 118, 110, 0.15);
    }
    
    .stButton > button:hover {
        background-color: #0D5D56;
        box-shadow: 0 4px 8px rgba(15, 118, 110, 0.25);
        transform: translateY(-1px);
    }
    
    /* Métrica */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #F8FAFB 0%, #F0F9F8 100%);
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #E5E7EB, transparent);
        margin: 2rem 0;
    }
    
    /* Sidebar */
    .sidebar-header {
        color: #1F2937;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-subtitle {
        color: #6B7280;
        font-size: 0.9rem;
        margin-bottom: 2rem;
        line-height: 1.4;
    }
    
    .nav-item {
        padding: 0.75rem 1rem;
        margin-bottom: 0.5rem;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        color: #4B5563;
        font-weight: 500;
    }
    
    .nav-item:hover {
        background-color: #E5E7EB;
        color: #0F766E;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #E0F2FE 0%, #F0F9F8 100%);
        border-left: 4px solid #0F766E;
        border-radius: 6px;
        padding: 1.25rem;
        margin: 1rem 0;
    }
    
    .info-box-title {
        color: #0F766E;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .info-box-text {
        color: #4B5563;
        font-size: 0.95rem;
    }
    
    /* Tabs */
    [data-testid="stTabs"] [role="tablist"] {
        border-bottom: 2px solid #E5E7EB;
    }
    
    [data-testid="stTabs"] [role="tab"] {
        color: #6B7280;
        font-weight: 500;
        border-bottom: 2px solid transparent;
        padding: 0.75rem 1rem;
    }
    
    [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
        color: #0F766E;
        border-bottom-color: #0F766E;
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        border: 1px solid #E5E7EB;
        border-radius: 6px;
        background-color: #FFFFFF;
    }
    
    [data-testid="stExpander"] [data-testid="stExpanderToggleButton"] {
        color: #0F766E;
    }
    
    /* Select Box */
    [data-testid="stSelectbox"] > div > div {
        border-radius: 6px;
        border-color: #E5E7EB;
    }
    
    /* Slider */
    [data-testid="stSlider"] > div > div > div {
        color: #0F766E;
    }
    
    /* Links */
    a {
        color: #0F766E;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    a:hover {
        color: #0D5D56;
        text-decoration: underline;
    }
    
    /* Success/Error/Warning */
    [data-testid="stAlert"] {
        border-radius: 6px;
        border: 1px solid;
    }
    
    [data-testid="stAlert"] [data-testid="stMarkdownContainer"] {
        font-size: 0.95rem;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.875rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
        
        .main {
            padding: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Navegação Minimalista
with st.sidebar:
    st.markdown('<div class="sidebar-header">📊 Portfólio</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Análise de Dados & Ciência de Dados</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    page = st.radio(
        "Navegação",
        ["🏠 Home", "👤 Sobre Mim", "📊 Projetos", "✉️ Contato"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.markdown("""
    <div style="font-size: 0.85rem; color: #9CA3AF; margin-top: 2rem;">
    <p><strong>Desenvolvido com:</strong></p>
    <p>🐍 Python • 🎨 Streamlit • 📊 Plotly</p>
    </div>
    """, unsafe_allow_html=True)

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
