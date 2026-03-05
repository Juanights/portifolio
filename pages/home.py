import streamlit as st

def show():
    # Hero Section
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0 2rem 0;">
        <h1 style="margin-bottom: 0.5rem;">Bem-vindo ao Meu Portfólio</h1>
        <p style="font-size: 1.1rem; color: #6B7280; margin-bottom: 0;">
            Transformando dados em insights valiosos
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Seção Principal
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">👋 Olá!</div>
            <div class="card-text">
                Sou um <strong>Analista e Cientista de Dados</strong> apaixonado por transformar dados brutos em decisões estratégicas.
                <br><br>
                Neste portfólio, você encontrará uma seleção de meus projetos mais interessantes, demonstrando minhas habilidades em:
                <br><br>
                • <strong>Análise Exploratória de Dados (EDA)</strong> - Descobrindo padrões e insights<br>
                • <strong>Machine Learning</strong> - Desenvolvendo modelos preditivos<br>
                • <strong>Visualização de Dados</strong> - Contando histórias com dados<br>
                • <strong>Business Intelligence</strong> - Criando dashboards estratégicos
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <div class="info-box-title">📌 Resumo Rápido</div>
            <div class="info-box-text">
                <strong>Formação:</strong><br>
                Análise de Dados
                <br><br>
                <strong>Localização:</strong><br>
                Brasil
                <br><br>
                <strong>Experiência:</strong><br>
                Iniciante em Dados
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Destaques
    st.markdown("<h2 style='text-align: center;'>🎯 Destaques</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.metric("Projetos", "5+", "+2 em desenvolvimento")
    
    with col2:
        st.metric("Linguagens", "Python, SQL", "R (aprendizado)")
    
    with col3:
        st.metric("Ferramentas", "Streamlit, Power BI", "Tableau, Jupyter")
    
    st.markdown("---")
    
    # Chamada para Ação
    st.markdown("<h2 style='text-align: center;'>🚀 Explore Meu Trabalho</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        if st.button("📊 Ver Projetos", use_container_width=True, key="btn_projects"):
            st.switch_page("pages/projects.py")
    
    with col2:
        if st.button("👤 Sobre Mim", use_container_width=True, key="btn_about"):
            st.switch_page("pages/about.py")
    
    with col3:
        if st.button("✉️ Contato", use_container_width=True, key="btn_contact"):
            st.switch_page("pages/contact.py")
    
    st.markdown("---")
    
    # Seção de Tecnologias
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F8FAFB 0%, #F0F9F8 100%); 
                border: 1px solid #E5E7EB; border-radius: 8px; padding: 2rem; 
                margin-top: 2rem; text-align: center;">
        <h3 style="color: #0F766E; margin-top: 0;">💡 Sobre Este Portfólio</h3>
        <p style="color: #6B7280; margin-bottom: 0;">
            Este portfólio foi desenvolvido com <strong>Streamlit</strong>, um framework Python que permite 
            criar aplicações web interativas de forma rápida e eficiente.
            <br><br>
            Todos os projetos aqui apresentados são <strong>100% interativos</strong>, permitindo que você 
            explore os dados, ajuste parâmetros e veja os resultados em tempo real.
        </p>
    </div>
    """, unsafe_allow_html=True)
