import streamlit as st

def show():
    st.title("🏠 Bem-vindo ao Meu Portfólio de Dados!")
    
    st.markdown("""
    ---
    """)
    
    # Seção de boas-vindas
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Olá! 👋
        
        Meu nome é **[Seu Nome]** e sou um **Analista e Cientista de Dados** apaixonado por transformar dados em insights valiosos.
        
        Neste portfólio, você encontrará uma seleção de meus projetos mais interessantes, demonstrando minhas habilidades em:
        
        - 📊 **Análise Exploratória de Dados (EDA)**
        - 🤖 **Machine Learning e Modelagem Preditiva**
        - 📈 **Visualização de Dados e Business Intelligence**
        - 🔧 **Engenharia de Dados e Automação**
        """)
    
    with col2:
        st.info("""
        ### 📌 Resumo Rápido
        
        **Formação:** Análise de Dados / Ciência de Dados
        
        **Experiência:** Iniciante em Dados
        
        **Localização:** Brasil
        """)
    
    st.markdown("""
    ---
    """)
    
    # Seção de destaques
    st.markdown("### 🎯 Destaques do Portfólio")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Projetos Concluídos", "5+", "+2 em desenvolvimento")
    
    with col2:
        st.metric("Linguagens", "Python, SQL", "R (em aprendizado)")
    
    with col3:
        st.metric("Ferramentas", "Streamlit, Power BI", "Tableau, Jupyter")
    
    st.markdown("""
    ---
    """)
    
    # Seção de chamada para ação
    st.markdown("### 🚀 Próximos Passos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Ver Projetos", use_container_width=True):
            st.switch_page("pages/projects.py")
    
    with col2:
        if st.button("👤 Sobre Mim", use_container_width=True):
            st.switch_page("pages/about.py")
    
    with col3:
        if st.button("✉️ Entrar em Contato", use_container_width=True):
            st.switch_page("pages/contact.py")
    
    st.markdown("""
    ---
    
    ### 💡 Sobre Este Portfólio
    
    Este portfólio foi desenvolvido com **Streamlit**, um framework Python que permite criar aplicações web interativas de forma rápida e eficiente.
    
    Todos os projetos aqui apresentados são **100% interativos**, permitindo que você explore os dados, ajuste parâmetros e veja os resultados em tempo real.
    """)
