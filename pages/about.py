import streamlit as st

def show():
    st.title("👤 Sobre Mim")
    
    st.markdown("""
    ---
    """)
    
    # Seção de trajetória
    st.markdown("### 📚 Trajetória Acadêmica")
    
    with st.expander("🎓 Formação", expanded=True):
        st.markdown("""
        - **Graduação:** Análise de Dados / Ciência de Dados
        - **Instituição:** [Sua Universidade]
        - **Período:** [Ano de Início] - [Ano de Conclusão]
        - **Destaque:** GPA 3.8/4.0 | Bolsista de Excelência
        """)
    
    with st.expander("📜 Certificações"):
        st.markdown("""
        - **Google Analytics Certification** - Google
        - **Python for Data Analysis** - DataCamp
        - **Machine Learning Specialization** - Coursera
        - **SQL for Data Analysis** - Udemy
        """)
    
    st.markdown("""
    ---
    """)
    
    # Seção de habilidades técnicas
    st.markdown("### 🛠️ Habilidades Técnicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Linguagens de Programação
        - **Python** ⭐⭐⭐⭐⭐
        - **SQL** ⭐⭐⭐⭐
        - **R** ⭐⭐⭐
        - **JavaScript** ⭐⭐
        """)
    
    with col2:
        st.markdown("""
        #### Ferramentas e Bibliotecas
        - **Pandas** ⭐⭐⭐⭐⭐
        - **NumPy** ⭐⭐⭐⭐⭐
        - **Scikit-learn** ⭐⭐⭐⭐
        - **Plotly / Matplotlib** ⭐⭐⭐⭐⭐
        """)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        #### Bancos de Dados
        - **MySQL** ⭐⭐⭐⭐
        - **PostgreSQL** ⭐⭐⭐
        - **MongoDB** ⭐⭐⭐
        """)
    
    with col4:
        st.markdown("""
        #### Ferramentas de BI
        - **Power BI** ⭐⭐⭐⭐
        - **Tableau** ⭐⭐⭐
        - **Google Data Studio** ⭐⭐⭐⭐
        """)
    
    st.markdown("""
    ---
    """)
    
    # Seção de soft skills
    st.markdown("### 💼 Soft Skills")
    
    skills = {
        "Comunicação": 90,
        "Resolução de Problemas": 85,
        "Trabalho em Equipe": 88,
        "Pensamento Crítico": 92,
        "Criatividade": 87,
        "Gestão de Projetos": 80
    }
    
    for skill, score in skills.items():
        st.write(f"**{skill}**")
        st.progress(score / 100)
    
    st.markdown("""
    ---
    """)
    
    # Seção de interesses
    st.markdown("### 🎯 Interesses e Áreas de Foco")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        ### 📊 Business Intelligence
        
        Transformar dados em dashboards e relatórios que impulsionam decisões estratégicas.
        """)
    
    with col2:
        st.info("""
        ### 🤖 Machine Learning
        
        Desenvolver modelos preditivos que agregam valor aos negócios.
        """)
    
    with col3:
        st.info("""
        ### 🔍 Data Science
        
        Explorar dados complexos para descobrir insights ocultos.
        """)
    
    st.markdown("""
    ---
    """)
    
    # Seção de filosofia
    st.markdown("""
    ### 🌟 Minha Filosofia
    
    Acredito que **dados bem interpretados são a chave para decisões melhores**. 
    Meu objetivo é não apenas criar análises, mas contar histórias com dados que inspirem ação.
    
    Estou sempre em busca de aprender novas ferramentas, técnicas e melhores práticas 
    para me manter atualizado neste campo dinâmico e em constante evolução.
    """)
