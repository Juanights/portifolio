import streamlit as st

def show():
    # Hero Section
    st.markdown("# Analista de Dados & Cientista de Dados")
    st.markdown("Transformando dados em estratégia de negócio")
    st.markdown("---")
    
    # Introdução Profissional
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
        st.info("""
        #### Perfil
        
        **Formação:** Análise de Dados / Ciência de Dados
        
        **Localização:** Brasil
        
        **Experiência:** Iniciante em Dados
        
        **Disponibilidade:** Aberto a oportunidades
        """)
    
    st.markdown("---")
    
    # Destaques Técnicos
    st.markdown("## Destaques")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Projetos", "5+", "2 em desenvolvimento")
    
    with col2:
        st.metric("Linguagens", "Python, SQL", "R")
    
    with col3:
        st.metric("Ferramentas", "Streamlit, Power BI", "Tableau, Jupyter")
    
    st.markdown("---")
    
    # Chamada para Ação
    st.markdown("## Explore")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Projetos", use_container_width=True, key="btn_projects"):
            st.switch_page("pages/projects.py")
    
    with col2:
        if st.button("Sobre Mim", use_container_width=True, key="btn_about"):
            st.switch_page("pages/about.py")
    
    with col3:
        if st.button("Contato", use_container_width=True, key="btn_contact"):
            st.switch_page("pages/contact.py")
    
    st.markdown("---")
    
    # Sobre o Portfólio
    st.markdown("## Sobre Este Portfólio")
    st.markdown("""
    Desenvolvido com Streamlit, um framework Python moderno para aplicações web interativas. 
    Todos os projetos aqui são 100% interativos, permitindo exploração dinâmica de dados e resultados em tempo real.
    """)
