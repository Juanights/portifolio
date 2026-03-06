import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

st.set_page_config(
    page_title="Portfólio | Analista de Dados",
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
    .main {
        background-color: #0F0718;
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
    
    /* Botões Neon */
    .stButton > button {
        background-color: #1A0F2E;
        color: #10B981;
        border: 2px solid #10B981;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.7rem 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
    }
    
    .stButton > button:hover {
        background-color: #10B981;
        color: #0F0718;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.8);
        transform: translateY(-2px);
    }
    
    /* HUD Card */
    .hud-card {
        background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 100%);
        border: 1px solid #10B981;
        border-radius: 4px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 0 15px rgba(16, 185, 129, 0.2), inset 0 0 15px rgba(16, 185, 129, 0.05);
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
        border-right: 1px solid #10B981;
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
        border: 1px solid #10B981;
        border-radius: 4px;
        padding: 1rem;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
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
        border: 1px solid #10B981;
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
        border-color: #10B981;
        border: 1px solid #10B981;
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
    
    /* Profile Image */
    .profile-image {
        border-radius: 50%;
        border: 3px solid #10B981;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.6), inset 0 0 20px rgba(16, 185, 129, 0.1);
        display: block;
        margin: 0 auto 1.5rem;
        width: 150px;
        height: 150px;
        object-fit: cover;
        transition: all 0.3s ease;
    }
    
    .profile-image:hover {
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.8), inset 0 0 30px rgba(16, 185, 129, 0.2);
        transform: scale(1.05);
    }
    
    /* Profile Placeholder */
    .profile-placeholder {
        width: 150px;
        height: 150px;
        margin: 0 auto 1.5rem;
        border: 3px solid #10B981;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        background: linear-gradient(135deg, #1A0F2E 0%, #0F0718 100%);
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.6), inset 0 0 20px rgba(16, 185, 129, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar session_state para navegação
if "page" not in st.session_state:
    st.session_state.page = "Início"

# Sidebar - Navegação Cyber-Executive
with st.sidebar:
    # Foto de Perfil com Efeito Neon
    import os
    perfil_path = "Perfil.png"
    
    if os.path.exists(perfil_path):
        st.image(perfil_path, use_column_width=True, caption=None)
    else:
        st.markdown("""
        <div class='profile-placeholder'>
            👤
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #CBD5E1; font-size: 0.85rem;'><em>Adicione perfil.jpg</em></p>", unsafe_allow_html=True)
    
    st.markdown("## ⚡ Portfólio")
    st.markdown("*Analista de Dados | Ciência de Dados*")
    st.markdown("---")
    
    page = st.radio(
        "Navegação",
        ["Início", "Sobre", "Projetos", "Storytelling", "Contato"],
        label_visibility="collapsed",
        index=["Início", "Sobre", "Projetos", "Storytelling", "Contato"].index(st.session_state.page)
    )
    
    # Atualizar session_state quando o radio muda
    st.session_state.page = page
    
    st.markdown("---")
    st.markdown("""
    **Desenvolvido com:**  
    🐍 Python • ⚡ Streamlit • 📊 Plotly
    """)

def show_home():
    st.markdown("# <span class='icon-neon'>◆</span> Analista de Dados & Cientista de Dados", unsafe_allow_html=True)
    st.markdown("Transformando dados em estratégia de negócio")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        ### Visão Geral
        
        Profissional em transição de carreira capaz de transformar dados complexos em insights acionáveis. Com foco em análise exploratória, modelagem preditiva e visualização estratégica, entrego soluções que impulsionam decisões baseadas em dados.
        
        **Competências Principais:**
        
        • Análise Exploratória de Dados (EDA) 
        • Modelagem Preditiva e Machine Learning  
        • Business Intelligence e Visualização Executiva  
        • Storytelling de Dados para Comunicação Eficaz
        """)
    
    with col2:
        st.markdown("""
        <div class='hud-card'>
            <h4 style='color: #10B981; margin-bottom: 1rem;'>⬥ Perfil</h4>
            <p><strong>Formação:</strong> Análise de Dados / Ciência de Dados</p>
            <p><strong>Localização:</strong> Brasil</p>
            <p><strong>Experiência:</strong> Iniciante em Dados</p>
            <p><strong>Disponibilidade:</strong> Aberto a oportunidades</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Destaques")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("◆ Projetos", "5+", "2 em desenvolvimento")
    with col2:
        st.metric("◆ Linguagens", "Python, SQL", "R")
    with col3:
        st.metric("◆ Ferramentas", "Streamlit, Power BI", "Tableau, Jupyter")
    
    st.markdown("---")
    
    st.markdown("## Explore")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("▶ Projetos", use_container_width=True, key="btn_explore_projetos"):
            st.session_state.page = "Projetos"
            st.rerun()
    with col2:
        if st.button("▶ Sobre Mim", use_container_width=True, key="btn_explore_sobre"):
            st.session_state.page = "Sobre"
            st.rerun()
    with col3:
        if st.button("▶ Storytelling", use_container_width=True, key="btn_explore_storytelling"):
            st.session_state.page = "Storytelling"
            st.rerun()
    with col4:
        if st.button("▶ Contato", use_container_width=True, key="btn_explore_contato"):
            st.session_state.page = "Contato"
            st.rerun()

def show_about():
    st.markdown("# <span class='icon-neon'>◆</span> Sobre Mim", unsafe_allow_html=True)
    st.markdown("Trajetória profissional e competências técnicas")
    st.markdown("---")
    
    with st.expander("📚 Formação Acadêmica"): 
         st.markdown("""
    <div class='hud-card'>
        <h3 style='color: #10B981;'>⬥ Formação Acadêmica</h3>
        <p><strong>Graduação:</strong> Análise e Desenvolvimento de Sistemas</p>
        <p><strong>Instituição:</strong> UNICID</p>
        <p><strong>Período:</strong> 2023 - 2025</p>       
        <p><strong>Pós-Graduação:</strong> Ciência de Dados e Inteligência Artificial</p>
        <p><strong>Instituição:</strong> UNINTER</p>
        <p><strong>Período:</strong> 2025 - 2026</p>
    </div>
    """, unsafe_allow_html=True)
    
    
    with st.expander("📜 Certificações Profissionais"):
        st.markdown("""
        • **Google Data Analytics Professional Certificate** - Google  
        """)
    
    st.markdown("---")
    
    st.markdown("## Competências Técnicas")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='hud-card'>
            <h4 style='color: #10B981;'>Linguagens de Programação</h4>
            • <span class='highlight-neon'>Python</span> — Intermediário<br />
            • <span class='highlight-neon'>SQL</span> — Básico<br /> 
            • <span class='highlight-neon'>R</span> — Básico<br />  
            • <span class='highlight-neon'>JavaScript</span> — Básico<br />
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='hud-card'>
            <h4 style='color: #10B981;'>Bibliotecas & Frameworks</h4>
            • <span class='highlight-neon'>Pandas</span> — Basico
            • <span class='highlight-neon'>NumPy</span> — Basico  
            • <span class='highlight-neon'>Scikit-learn</span> — Basico  
            • <span class='highlight-neon'>Plotly</span> — Basico
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class='hud-card'>
            <h4 style='color: #10B981;'>Bancos de Dados</h4>
            • <span class='highlight-neon'>MySQL</span> — Básico  
            • <span class='highlight-neon'>SQL Server</span> — Básico 
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='hud-card'>
            <h4 style='color: #10B981;'>Ferramentas de BI</h4>
            • <span class='highlight-neon'>Power BI</span> — Básico  
            • <span class='highlight-neon'>Excel/Sheets</span> — Intermediário  
            • <span class='highlight-neon'>Streamlit</span> — Intermediário
        </div>
        """, unsafe_allow_html=True)

def show_projects():
    st.markdown("# <span class='icon-neon'>◆</span> Projetos", unsafe_allow_html=True)
    st.markdown("Análise técnica de dados e modelagem preditiva")
    st.markdown("---")
    
    st.markdown("## Selecione um projeto:")
    project = st.selectbox(
        "Projetos Disponíveis",
        ["Análise Exploratória (Iris)", "Machine Learning", "Dashboard de Vendas"],
        label_visibility="collapsed"
    )
    
    if project == "Análise Exploratória (Iris)":
        st.markdown("""
        <div class='hud-card'>
            <h3 style='color: #10B981;'>⬥ Análise Exploratória - Dataset Iris</h3>
            <p>Análise detalhada do dataset Iris com visualizações interativas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Visão Geral", "Distribuições", "Correlações", "Dados"])
        
        with tab1:
            st.markdown("### Estatísticas Descritivas")
            iris_data = load_iris()
            df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
            st.dataframe(df.describe(), use_container_width=True)
        
        with tab2:
            st.markdown("### Distribuições de Variáveis")
            iris_data = load_iris()
            df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
            
            col1, col2 = st.columns(2)
            with col1:
                fig = px.histogram(df, x="sepal length (cm)", nbins=30, title="Sepal Length")
                fig.update_layout(
                    template='plotly_dark',
                    plot_bgcolor='#1A0F2E',
                    paper_bgcolor='#0F0718',
                    font=dict(color='#E0E7FF'),
                    title_font_color='#10B981'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.histogram(df, x="petal length (cm)", nbins=30, title="Petal Length")
                fig.update_layout(
                    template='plotly_dark',
                    plot_bgcolor='#1A0F2E',
                    paper_bgcolor='#0F0718',
                    font=dict(color='#E0E7FF'),
                    title_font_color='#10B981'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.markdown("### Matriz de Correlações")
            iris_data = load_iris()
            df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
            
            fig = px.imshow(df.corr(), color_continuous_scale='Greens', title="Correlation Matrix")
            fig.update_layout(
                template='plotly_dark',
                plot_bgcolor='#1A0F2E',
                paper_bgcolor='#0F0718',
                font=dict(color='#E0E7FF'),
                title_font_color='#10B981'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            st.markdown("### Dataset Completo")
            iris_data = load_iris()
            df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
            st.dataframe(df, use_container_width=True)
    
    elif project == "Machine Learning":
        st.markdown("""
        <div class='hud-card'>
            <h3 style='color: #10B981;'>⬥ Modelo de Classificação - Iris</h3>
            <p>Random Forest para classificação de espécies de flores.</p>
        </div>
        """, unsafe_allow_html=True)
        
        iris_data = load_iris()
        X = iris_data.data
        y = iris_data.target
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        accuracy = model.score(X_test, y_test)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("◆ Acurácia", f"{accuracy:.2%}")
        with col2:
            st.metric("◆ Amostras Teste", len(X_test))
        with col3:
            st.metric("◆ Features", X.shape[1])
        
        st.markdown("---")
        
        st.markdown("### Importância das Features")
        feature_importance = pd.DataFrame({
            'Feature': iris_data.feature_names,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        fig = px.bar(feature_importance, x='Importance', y='Feature', orientation='h', title="Feature Importance")
        fig.update_layout(
            template='plotly_dark',
            plot_bgcolor='#1A0F2E',
            paper_bgcolor='#0F0718',
            font=dict(color='#E0E7FF'),
            title_font_color='#10B981',
            marker_color='#10B981'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif project == "Dashboard de Vendas":
        st.markdown("""
        <div class='hud-card'>
            <h3 style='color: #10B981;'>⬥ Dashboard de Vendas</h3>
            <p>Painel executivo com métricas de vendas e tendências.</p>
        </div>
        """, unsafe_allow_html=True)
        
        np.random.seed(42)
        dates = pd.date_range('2024-01-01', periods=90, freq='D')
        sales_data = pd.DataFrame({
            'Data': dates,
            'Vendas': np.random.randint(5000, 20000, 90),
            'Clientes': np.random.randint(50, 200, 90)
        })
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("◆ Total de Vendas", f"R$ {sales_data['Vendas'].sum():,.0f}")
        with col2:
            st.metric("◆ Média Diária", f"R$ {sales_data['Vendas'].mean():,.0f}")
        with col3:
            st.metric("◆ Total de Clientes", sales_data['Clientes'].sum())
        
        st.markdown("---")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=sales_data['Data'],
            y=sales_data['Vendas'],
            mode='lines+markers',
            name='Vendas',
            line=dict(color='#10B981', width=3),
            marker=dict(size=6)
        ))
        fig.update_layout(
            title="Tendência de Vendas (90 dias)",
            xaxis_title="Data",
            yaxis_title="Vendas (R$)",
            template='plotly_dark',
            plot_bgcolor='#1A0F2E',
            paper_bgcolor='#0F0718',
            font=dict(color='#E0E7FF'),
            title_font_color='#10B981',
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)

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
    st.markdown("Entre em contato para oportunidades e colaborações")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='hud-card'>
            <h3 style='color: #10B981;'>⬥ Informações de Contato</h3>
            <p><strong>Email:</strong> seu.email@example.com</p>
            <p><strong>LinkedIn:</strong> linkedin.com/in/seu-perfil</p>
            <p><strong>GitHub:</strong> github.com/seu-usuario</p>
            <p><strong>Localização:</strong> Brasil</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='hud-card'>
            <h3 style='color: #10B981;'>⬥ Disponibilidade</h3>
            <p><strong>Status:</strong> Aberto a oportunidades</p>
            <p><strong>Modalidade:</strong> Remoto / Híbrido</p>
            <p><strong>Tempo de Resposta:</strong> 24-48 horas</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## Envie uma Mensagem")
    with st.form("contact_form"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        mensagem = st.text_area("Mensagem")
        submitted = st.form_submit_button("Enviar Mensagem")
        
        if submitted:
            if nome and email and mensagem:
                st.success("Obrigado pela mensagem. Responderei em breve.")
            else:
                st.error("Por favor, preencha todos os campos obrigatórios.")

# Roteamento de Páginas
if st.session_state.page == "Início":
    show_home()
elif st.session_state.page == "Sobre":
    show_about()
elif st.session_state.page == "Projetos":
    show_projects()
elif st.session_state.page == "Storytelling":
    show_storytelling()
elif st.session_state.page == "Contato":
    show_contact()
