import streamlit as st

def show():
    st.markdown("# Sobre Mim")
    st.markdown("Trajetória profissional e competências técnicas")
    st.markdown("---")
    
    # Formação Acadêmica
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
    
    # Competências Técnicas
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
    
    st.markdown("---")
    
    # Competências Transversais
    st.markdown("## Competências Transversais")
    
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
    st.markdown("## Áreas de Foco")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Business Intelligence")
        st.markdown("Transformar dados em dashboards e relatórios que impulsionam decisões estratégicas.")
    
    with col2:
        st.markdown("### Machine Learning")
        st.markdown("Desenvolver modelos preditivos que agregam valor aos negócios.")
    
    with col3:
        st.markdown("### Data Science")
        st.markdown("Explorar dados complexos para descobrir insights ocultos.")
    
    st.markdown("---")
    
    # Filosofia Profissional
    st.markdown("## Filosofia Profissional")
    st.markdown("""
    Acredito que dados bem interpretados são a base para decisões estratégicas. 
    Meu objetivo é não apenas criar análises, mas contar histórias com dados que inspirem ação.
    
    Estou em constante evolução, acompanhando as melhores práticas e novas tecnologias 
    em um campo dinâmico e em transformação contínua.
    """)
