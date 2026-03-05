import streamlit as st

def show():
    # Hero Section
    st.markdown("# 🏠 Bem-vindo ao Meu Portfólio")
    st.markdown("*Transformando dados em insights valiosos*")
    st.markdown("---")
    
    # Seção Principal
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.subheader("👋 Olá!")
        st.markdown("""
        Sou um **Analista e Cientista de Dados** apaixonado por transformar dados brutos em decisões estratégicas.
        
        Neste portfólio, você encontrará uma seleção de meus projetos mais interessantes, demonstrando minhas habilidades em:
        
        - 📊 **Análise Exploratória de Dados (EDA)** - Descobrindo padrões e insights
        - 🤖 **Machine Learning** - Desenvolvendo modelos preditivos
        - 📈 **Visualização de Dados** - Contando histórias com dados
        - 💼 **Business Intelligence** - Criando dashboards estratégicos
        """)
    
    with col2:
        st.info("""
        **📌 Resumo Rápido**
        
        **Formação:** Análise de Dados
        
        **Localização:** Brasil
        
        **Experiência:** Iniciante em Dados
        """)
    
    st.markdown("---")
    
    # Destaques
    st.markdown("## 🎯 Destaques do Portfólio")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Projetos Concluídos", "5+", "+2 em desenvolvimento")
    
    with col2:
        st.metric("Linguagens", "Python, SQL", "R (aprendizado)")
    
    with col3:
        st.metric("Ferramentas", "Streamlit, Power BI", "Tableau, Jupyter")
    
    st.markdown("---")
    
    # Chamada para Ação
    st.markdown("## 🚀 Explore Meu Trabalho")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Ver Projetos", use_container_width=True):
            st.switch_page("pages/projects.py")
    
    with col2:
        if st.button("👤 Sobre Mim", use_container_width=True):
            st.switch_page("pages/about.py")
    
    with col3:
        if st.button("✉️ Contato", use_container_width=True):
            st.switch_page("pages/contact.py")
    
    st.markdown("---")
    
    # Seção de Tecnologias
    st.markdown("## 💡 Sobre Este Portfólio")
    st.markdown("""
    Este portfólio foi desenvolvido com **Streamlit**, um framework Python que permite criar aplicações web interativas de forma rápida e eficiente.
    
    Todos os projetos aqui apresentados são **100% interativos**, permitindo que você explore os dados, ajuste parâmetros e veja os resultados em tempo real.
    """)
