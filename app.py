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
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Executivo - Tema Dark Executive
st.markdown("""
    <style>
    /* Paleta Dark Executive */
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background-color: #0f172a;
        color: #f1f5f9;
    }
    
    /* Main Container */
    .main {
        background-color: #0f172a;
        padding: 2rem;
    }
    
    /* Tipografia */
    h1 {
        color: #f1f5f9;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    h2 {
        color: #e0e7ff;
        font-weight: 600;
        font-size: 1.875rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    
    h3 {
        color: #93c5fd;
        font-weight: 600;
        font-size: 1.25rem;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    p, li {
        color: #cbd5e1;
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    /* Botões */
    .stButton > button {
        background-color: #1e40af;
        color: #f1f5f9;
        border: 1px solid #3b82f6;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.7rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1e3a8a;
        border-color: #60a5fa;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%);
        border-left: 3px solid #3b82f6;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #334155, transparent);
        margin: 2rem 0;
    }
    
    /* Métrica */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%);
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    /* Links */
    a {
        color: #60a5fa;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    a:hover {
        color: #93c5fd;
        text-decoration: underline;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #334155;
    }
    
    [data-testid="stSidebar"] h1 {
        font-size: 1.25rem;
        color: #f1f5f9;
    }
    
    /* Tabs */
    [data-testid="stTabs"] [role="tablist"] {
        border-bottom: 1px solid #334155;
    }
    
    [data-testid="stTabs"] [role="tab"] {
        color: #94a3b8;
        font-weight: 500;
        border-bottom: 2px solid transparent;
    }
    
    [data-testid="stTabs"] [role="tab"][aria-selected="true"] {
        color: #60a5fa;
        border-bottom-color: #3b82f6;
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        border: 1px solid #334155;
        border-radius: 6px;
        background-color: #1a2332;
    }
    
    /* Dataframe */
    [data-testid="stDataFrame"] {
        background-color: #1a2332;
    }
    
    /* Selectbox e inputs */
    [data-testid="stSelectbox"] > div > div {
        background-color: #1a2332;
        border-color: #334155;
    }
    
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea {
        background-color: #1a2332;
        color: #f1f5f9;
        border-color: #334155;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Navegação Única e Profissional
with st.sidebar:
    st.markdown("## Portfólio")
    st.markdown("*Analista de Dados | Ciência de Dados*")
    st.markdown("---")
    
    page = st.radio(
        "Navegação",
        ["Início", "Sobre", "Projetos", "Storytelling", "Contato"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("""
    **Desenvolvido com:**  
    Python • Streamlit • Plotly
    """)

def show_home():
    st.markdown("# Analista de Dados & Cientista de Dados")
    st.markdown("Transformando dados em estratégia de negócio")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        ### Visão Geral
        
        Profissional especializado em transformar dados complexos em insights acionáveis. 
        Com experiência em análise exploratória, modelagem preditiva e visualização estratégica, 
        entrego soluções que impulsionam decisões baseadas em dados.
        
        **Competências Principais:**
        - Análise Exploratória de Dados (EDA) e Data Profiling
        - Modelagem Preditiva e Machine Learning
        - Business Intelligence e Visualização Executiva
        - Engenharia de Dados e Automação
        """)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h3>Perfil</h3>
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
        st.metric("Projetos", "5+", "2 em desenvolvimento")
    with col2:
        st.metric("Linguagens", "Python, SQL", "R")
    with col3:
        st.metric("Ferramentas", "Streamlit, Power BI", "Tableau, Jupyter")
    
    st.markdown("---")
    
    st.markdown("## Explore")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Projetos", use_container_width=True):
            st.session_state.page = "Projetos"
            st.rerun()
    with col2:
        if st.button("Sobre Mim", use_container_width=True):
            st.session_state.page = "Sobre"
            st.rerun()
    with col3:
        if st.button("Contato", use_container_width=True):
            st.session_state.page = "Contato"
            st.rerun()

def show_about():
    st.markdown("# Sobre Mim")
    st.markdown("Trajetória profissional e competências técnicas")
    st.markdown("---")
    
    st.markdown("## Formação Acadêmica")
    
    with st.expander("Graduação", expanded=True):
        st.markdown("""
        **Curso:** Análise de Dados / Ciência de Dados  
        **Instituição:** [Sua Universidade]  
        **Período:** [Ano de Início] - [Ano de Conclusão]  
        **Destaque:** GPA 3.8/4.0 | Bolsista de Excelência
        """)
    
    with st.expander("Certificações"):
        st.markdown("""
        - Google Analytics Certification
        - Python for Data Analysis (DataCamp)
        - Machine Learning Specialization (Coursera)
        - SQL for Data Analysis (Udemy)
        """)
    
    st.markdown("---")
    
    st.markdown("## Competências Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Linguagens de Programação")
        st.markdown("""
        - **Python** — Avançado
        - **SQL** — Avançado
        - **R** — Intermediário
        - **JavaScript** — Básico
        """)
    
    with col2:
        st.markdown("### Bibliotecas & Frameworks")
        st.markdown("""
        - **Pandas** — Avançado
        - **NumPy** — Avançado
        - **Scikit-learn** — Avançado
        - **Plotly** — Avançado
        """)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### Bancos de Dados")
        st.markdown("""
        - **MySQL** — Avançado
        - **PostgreSQL** — Intermediário
        - **MongoDB** — Intermediário
        - **SQLite** — Avançado
        """)
    
    with col4:
        st.markdown("### Ferramentas de BI")
        st.markdown("""
        - **Power BI** — Avançado
        - **Tableau** — Intermediário
        - **Google Data Studio** — Avançado
        - **Streamlit** — Avançado
        """)

def show_projects():
    st.markdown("# Projetos")
    st.markdown("Análise técnica de dados e modelagem preditiva")
    st.markdown("---")
    
    project = st.selectbox(
        "Selecione um projeto:",
        ["Análise Exploratória (Iris)", "Machine Learning (Classificação)", "Dashboard de Vendas"]
    )
    
    if project == "Análise Exploratória (Iris)":
        show_eda()
    elif project == "Machine Learning (Classificação)":
        show_ml()
    else:
        show_dashboard()

def show_eda():
    st.markdown("## Análise Exploratória - Dataset Iris")
    st.markdown("Exploração detalhada do famoso dataset Iris com visualizações interativas.")
    
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    
    tab1, tab2, tab3, tab4 = st.tabs(["Visão Geral", "Distribuições", "Correlações", "Dados"])
    
    with tab1:
        st.markdown("### Estatísticas Descritivas")
        st.dataframe(df.describe(), use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", len(df))
        with col2:
            st.metric("Número de Features", len(iris.feature_names))
        with col3:
            st.metric("Espécies Únicas", df['species'].nunique())
    
    with tab2:
        st.markdown("### Distribuições de Features")
        feature = st.selectbox("Selecione uma feature:", iris.feature_names)
        
        fig = go.Figure()
        for species in iris.target_names:
            data = df[df['species'] == species][feature]
            fig.add_trace(go.Histogram(
                x=data,
                name=species,
                opacity=0.7,
                marker_color=['#1e40af', '#3b82f6', '#60a5fa'][list(iris.target_names).index(species)]
            ))
        
        fig.update_layout(
            title=f"Distribuição de {feature}",
            xaxis_title=feature,
            yaxis_title="Frequência",
            barmode='overlay',
            template='plotly_dark',
            hovermode='x unified',
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Matriz de Correlação")
        corr_matrix = df.drop('species', axis=1).corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='Blues',
            zmid=0
        ))
        
        fig.update_layout(
            title="Correlação entre Features",
            template='plotly_dark',
            height=500,
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("### Dataset Completo")
        st.dataframe(df, use_container_width=True)

def show_ml():
    st.markdown("## Machine Learning - Classificação")
    st.markdown("Modelo preditivo para classificação de espécies de Iris.")
    
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    
    tab1, tab2, tab3 = st.tabs(["Desempenho", "Matriz de Confusão", "Previsão"])
    
    with tab1:
        st.markdown("### Métricas de Desempenho")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Acurácia", f"{accuracy:.2%}")
        with col2:
            st.metric("Modelo", "Random Forest")
        with col3:
            st.metric("Estimadores", "100")
        
        st.markdown("### Relatório de Classificação")
        report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df, use_container_width=True)
    
    with tab2:
        st.markdown("### Matriz de Confusão")
        
        cm = confusion_matrix(y_test, y_pred)
        
        fig = go.Figure(data=go.Heatmap(
            z=cm,
            x=iris.target_names,
            y=iris.target_names,
            colorscale='Blues',
            text=cm,
            texttemplate='%{text}',
            textfont={"size": 12}
        ))
        
        fig.update_layout(
            title="Matriz de Confusão",
            xaxis_title="Predito",
            yaxis_title="Real",
            template='plotly_dark',
            height=500,
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Fazer Previsão")
        
        col1, col2 = st.columns(2)
        with col1:
            sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.5)
            sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
        
        with col2:
            petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 3.5)
            petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)
        
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        st.markdown("### Resultado")
        st.success(f"**Espécie Prevista:** {iris.target_names[prediction]}")
        
        col1, col2, col3 = st.columns(3)
        for i, species in enumerate(iris.target_names):
            with [col1, col2, col3][i]:
                st.metric(species, f"{probability[i]:.2%}")

def show_dashboard():
    st.markdown("## Dashboard de Vendas")
    st.markdown("Análise de performance de vendas com KPIs e tendências.")
    
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=90, freq='D')
    data = {
        'Data': dates,
        'Vendas': np.random.randint(5000, 15000, 90),
        'Região': np.random.choice(['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'], 90),
        'Categoria': np.random.choice(['Eletrônicos', 'Vestuário', 'Alimentos', 'Serviços'], 90)
    }
    df_sales = pd.DataFrame(data)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Vendas", f"R$ {df_sales['Vendas'].sum():,.0f}")
    with col2:
        st.metric("Média Diária", f"R$ {df_sales['Vendas'].mean():,.0f}")
    with col3:
        st.metric("Máximo", f"R$ {df_sales['Vendas'].max():,.0f}")
    with col4:
        st.metric("Mínimo", f"R$ {df_sales['Vendas'].min():,.0f}")
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Tendência", "Por Região", "Por Categoria"])
    
    with tab1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_sales['Data'],
            y=df_sales['Vendas'],
            mode='lines',
            name='Vendas',
            line=dict(color='#3b82f6', width=2)
        ))
        fig.update_layout(
            title="Tendência de Vendas",
            xaxis_title="Data",
            yaxis_title="Vendas (R$)",
            template='plotly_dark',
            hovermode='x unified',
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        sales_by_region = df_sales.groupby('Região')['Vendas'].sum().sort_values(ascending=False)
        fig = go.Figure(data=[
            go.Bar(x=sales_by_region.index, y=sales_by_region.values, marker_color='#1e40af')
        ])
        fig.update_layout(
            title="Vendas por Região",
            xaxis_title="Região",
            yaxis_title="Vendas (R$)",
            template='plotly_dark',
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        sales_by_category = df_sales.groupby('Categoria')['Vendas'].sum().sort_values(ascending=False)
        fig = go.Figure(data=[
            go.Pie(labels=sales_by_category.index, values=sales_by_category.values, marker_colors=['#1e40af', '#3b82f6', '#60a5fa', '#93c5fd'])
        ])
        fig.update_layout(title="Distribuição por Categoria", template='plotly_dark', paper_bgcolor='#0f172a')
        st.plotly_chart(fig, use_container_width=True)

def show_contact():
    st.markdown("# Contato")
    st.markdown("Conecte-se comigo para oportunidades e colaborações")
    st.markdown("---")
    
    st.markdown("## Canais de Contato")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### LinkedIn")
        st.markdown("Acompanhe minha jornada profissional e conecte-se comigo.\n\n[Visite meu perfil](https://linkedin.com/in/seu-perfil)")
    
    with col2:
        st.markdown("### GitHub")
        st.markdown("Explore meus projetos e contribuições.\n\n[Visite meu GitHub](https://github.com/seu-usuario)")
    
    with col3:
        st.markdown("### Email")
        st.markdown("Envie um email diretamente.\n\n[seu.email@gmail.com](mailto:seu.email@gmail.com)")
    
    st.markdown("---")
    
    st.markdown("## Formulário de Contato")
    
    st.markdown("""
    <div class="info-box">
        <p>Preencha o formulário abaixo. Responderei em 24-48 horas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Nome Completo *", placeholder="João Silva")
        with col2:
            email = st.text_input("Email *", placeholder="joao@example.com")
        
        assunto = st.selectbox(
            "Assunto *",
            ["Oportunidade de Trabalho", "Colaboração em Projeto", "Dúvida Técnica", 
             "Feedback sobre Portfólio", "Outro"]
        )
        
        mensagem = st.text_area(
            "Mensagem *",
            placeholder="Escreva sua mensagem aqui...",
            height=150
        )
        
        submitted = st.form_submit_button("Enviar", use_container_width=True)
        
        if submitted:
            if nome and email and mensagem:
                st.success("Obrigado pela mensagem. Responderei em breve.")
            else:
                st.error("Por favor, preencha todos os campos obrigatórios.")

def show_storytelling():
    st.markdown("# Análise de Impacto de Negócio")
    st.markdown("Uma narrativa de dados que transforma números em decisões")
    st.markdown("---")
    
    # Seção 1: O Problema
    st.markdown("""\n    <div style="background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%); border-left: 4px solid #3b82f6; border-radius: 8px; padding: 2rem; margin: 2rem 0;">
        <h3 style="color: #60a5fa; margin-bottom: 1rem;">1. O Problema</h3>
        <p style="color: #cbd5e1; line-height: 1.8; font-size: 1rem;">Uma empresa de varejo online enfrenta uma queda consistente na taxa de conversão de vendas nos últimos 6 meses. O time de negócios não consegue identificar se o problema está na qualidade do tráfego, no comportamento do cliente ou em fatores sazonais.</p>
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
        line=dict(color='#ef4444', width=3),
        marker=dict(size=6)
    ))
    fig1.update_layout(
        title="Tendência de Taxa de Conversão (6 meses)",
        xaxis_title="Data",
        yaxis_title="Taxa de Conversão (%)",
        template='plotly_dark',
        plot_bgcolor='#1a2332',
        paper_bgcolor='#0f172a',
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("""\n    <div style="background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%); border-left: 4px solid #f59e0b; border-radius: 8px; padding: 2rem; margin: 2rem 0;">
        <h3 style="color: #fbbf24; margin-bottom: 1rem;">2. A Exploração</h3>
        <p style="color: #cbd5e1; line-height: 1.8; font-size: 1rem;">Investigamos os dados em profundidade. Segmentamos por fonte de tráfego, dispositivo e período do dia para identificar padrões.</p>
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
            go.Bar(x=traffic_data['Fonte'], y=traffic_data['Taxa'], marker_color=['#3b82f6', '#ef4444', '#f59e0b', '#10b981'])
        ])
        fig2.update_layout(
            title="Por Fonte de Tráfego",
            template='plotly_dark',
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a',
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
            go.Bar(x=device_data['Dispositivo'], y=device_data['Taxa'], marker_color=['#3b82f6', '#ef4444', '#f59e0b'])
        ])
        fig3.update_layout(
            title="Por Dispositivo",
            template='plotly_dark',
            plot_bgcolor='#1a2332',
            paper_bgcolor='#0f172a',
            height=350
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("""\n    <div style="background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%); border-left: 4px solid #10b981; border-radius: 8px; padding: 2rem; margin: 2rem 0;">
        <h3 style="color: #6ee7b7; margin-bottom: 1rem;">3. O Insight Crítico</h3>
        <p style="color: #cbd5e1; line-height: 1.8; font-size: 1rem;"><strong>Descoberta Principal:</strong> A taxa de conversão em dispositivos móveis caiu 45% em 6 meses, enquanto desktop permaneceu estável. Isso sugere um problema de experiência do usuário (UX) específico para mobile.</p>
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
        line=dict(color='#3b82f6', width=3)
    ))
    fig4.add_trace(go.Scatter(
        x=mobile_data['Data'],
        y=mobile_data['Mobile'],
        mode='lines',
        name='Mobile',
        line=dict(color='#ef4444', width=3, dash='dash')
    ))
    fig4.update_layout(
        title="Divergência de Performance: Desktop vs Mobile",
        xaxis_title="Data",
        yaxis_title="Taxa de Conversão (%)",
        template='plotly_dark',
        plot_bgcolor='#1a2332',
        paper_bgcolor='#0f172a',
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    st.markdown("""\n    <div style="background: linear-gradient(135deg, #1a2f4b 0%, #0f1f35 100%); border-left: 4px solid #8b5cf6; border-radius: 8px; padding: 2rem; margin: 2rem 0;">
        <h3 style="color: #c4b5fd; margin-bottom: 1rem;">4. Recomendações de Ação</h3>
        <p style="color: #cbd5e1; line-height: 1.8; font-size: 1rem;">Com base nesta análise, recomendamos:</p>
        <ul style="color: #cbd5e1; line-height: 2;">
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
        st.metric("Queda Total", "-44.4%", "-2.0 pp")
    with col2:
        st.metric("Queda Mobile", "-51.4%", "-2.7 pp")
    with col3:
        st.metric("Estabilidade Desktop", "-7.5%", "-0.3 pp")
    with col4:
        st.metric("Oportunidade", "+R$ 150k", "Anual")

# Roteamento de Páginas
if page == "Início":
    show_home()
elif page == "Sobre":
    show_about()
elif page == "Projetos":
    show_projects()
elif page == "Storytelling":
    show_storytelling()
elif page == "Contato":
    show_contact()
