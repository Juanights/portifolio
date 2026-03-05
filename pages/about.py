import streamlit as st

def show():
    st.markdown("# 👤 Sobre Mim")
    st.markdown("*Conheça minha trajetória e habilidades*")
    st.markdown("---")
    
    # Trajetória
    st.markdown("## 📚 Trajetória Acadêmica")
    
    with st.expander("🎓 Formação", expanded=True):
        st.markdown("""
        **Graduação:** Análise de Dados / Ciência de Dados  
        **Instituição:** [Sua Universidade]  
        **Período:** [Ano de Início] - [Ano de Conclusão]  
        **Destaque:** GPA 3.8/4.0 | Bolsista de Excelência
        """)
    
    with st.expander("📜 Certificações"):
        st.markdown("""
        - Google Analytics Certification - Google
        - Python for Data Analysis - DataCamp
        - Machine Learning Specialization - Coursera
        - SQL for Data Analysis - Udemy
        """)
    
    st.markdown("---")
    
    # Habilidades Técnicas
    st.markdown("## 🛠️ Habilidades Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🐍 Linguagens de Programação")
        st.markdown("""
        - **Python** ⭐⭐⭐⭐⭐
        - **SQL** ⭐⭐⭐⭐
        - **R** ⭐⭐⭐
        - **JavaScript** ⭐⭐
        """)
    
    with col2:
        st.subheader("📊 Bibliotecas & Frameworks")
        st.markdown("""
        - **Pandas** ⭐⭐⭐⭐⭐
        - **NumPy** ⭐⭐⭐⭐⭐
        - **Scikit-learn** ⭐⭐⭐⭐
        - **Plotly** ⭐⭐⭐⭐⭐
        """)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("🗄️ Bancos de Dados")
        st.markdown("""
        - **MySQL** ⭐⭐⭐⭐
        - **PostgreSQL** ⭐⭐⭐
        - **MongoDB** ⭐⭐⭐
        - **SQLite** ⭐⭐⭐⭐
        """)
    
    with col4:
        st.subheader("📈 Ferramentas de BI")
        st.markdown("""
        - **Power BI** ⭐⭐⭐⭐
        - **Tableau** ⭐⭐⭐
        - **Google Data Studio** ⭐⭐⭐⭐
        - **Streamlit** ⭐⭐⭐⭐⭐
        """)
    
    st.markdown("---")
    
    # Soft Skills
    st.markdown("## 💼 Soft Skills")
    
    skills = {
        "Comunicação": 90,
        "Resolução de Problemas": 85,
        "Trabalho em Equipe": 88,
        "Pensamento Crítico": 92,
        "Criatividade": 87,
        "Gestão de Projetos": 80
    }
    
    col1, col2, col3 = st.columns(3)
    
    for idx, (skill, score) in enumerate(skills.items()):
        if idx % 3 == 0:
            col = col1
        elif idx % 3 == 1:
            col = col2
        else:
            col = col3
        
        with col:
            st.markdown(f"**{skill}**")
            st.progress(score / 100)
    
    st.markdown("---")
    
    # Áreas de Foco
    st.markdown("## 🎯 Áreas de Foco")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📊 Business Intelligence")
        st.markdown("Transformar dados em dashboards e relatórios que impulsionam decisões estratégicas.")
    
    with col2:
        st.subheader("🤖 Machine Learning")
        st.markdown("Desenvolver modelos preditivos que agregam valor aos negócios.")
    
    with col3:
        st.subheader("🔍 Data Science")
        st.markdown("Explorar dados complexos para descobrir insights ocultos.")
    
    st.markdown("---")
    
    # Filosofia
    st.markdown("## 🌟 Minha Filosofia")
    st.markdown("""
    Acredito que **dados bem interpretados são a chave para decisões melhores**. 
    Meu objetivo é não apenas criar análises, mas contar histórias com dados que inspirem ação.
    
    Estou sempre em busca de aprender novas ferramentas, técnicas e melhores práticas 
    para me manter atualizado neste campo dinâmico e em constante evolução.
    """)
