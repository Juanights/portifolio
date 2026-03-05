import streamlit as st

def show():
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1>Sobre Mim</h1>
        <p style="font-size: 1.05rem; color: #6B7280;">Conheça minha trajetória e habilidades</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Trajetória
    st.markdown("<h2>📚 Trajetória Acadêmica</h2>", unsafe_allow_html=True)
    
    with st.expander("🎓 Formação", expanded=True):
        st.markdown("""
        **Graduação:** Análise de Dados / Ciência de Dados  
        **Instituição:** [Sua Universidade]  
        **Período:** [Ano de Início] - [Ano de Conclusão]  
        **Destaque:** GPA 3.8/4.0 | Bolsista de Excelência
        """)
    
    with st.expander("📜 Certificações"):
        st.markdown("""
        - **Google Analytics Certification** - Google
        - **Python for Data Analysis** - DataCamp
        - **Machine Learning Specialization** - Coursera
        - **SQL for Data Analysis** - Udemy
        """)
    
    st.markdown("---")
    
    # Habilidades Técnicas
    st.markdown("<h2>🛠️ Habilidades Técnicas</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">🐍 Linguagens de Programação</div>
            <div class="card-text">
                <strong>Python</strong> ⭐⭐⭐⭐⭐<br>
                <strong>SQL</strong> ⭐⭐⭐⭐<br>
                <strong>R</strong> ⭐⭐⭐<br>
                <strong>JavaScript</strong> ⭐⭐
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-header">📊 Bibliotecas & Frameworks</div>
            <div class="card-text">
                <strong>Pandas</strong> ⭐⭐⭐⭐⭐<br>
                <strong>NumPy</strong> ⭐⭐⭐⭐⭐<br>
                <strong>Scikit-learn</strong> ⭐⭐⭐⭐<br>
                <strong>Plotly</strong> ⭐⭐⭐⭐⭐
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2, gap="large")
    
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-header">🗄️ Bancos de Dados</div>
            <div class="card-text">
                <strong>MySQL</strong> ⭐⭐⭐⭐<br>
                <strong>PostgreSQL</strong> ⭐⭐⭐<br>
                <strong>MongoDB</strong> ⭐⭐⭐<br>
                <strong>SQLite</strong> ⭐⭐⭐⭐
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-header">📈 Ferramentas de BI</div>
            <div class="card-text">
                <strong>Power BI</strong> ⭐⭐⭐⭐<br>
                <strong>Tableau</strong> ⭐⭐⭐<br>
                <strong>Google Data Studio</strong> ⭐⭐⭐⭐<br>
                <strong>Streamlit</strong> ⭐⭐⭐⭐⭐
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Soft Skills
    st.markdown("<h2>💼 Soft Skills</h2>", unsafe_allow_html=True)
    
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
            st.markdown(f"<div style='margin-bottom: 1.5rem;'><strong>{skill}</strong></div>", unsafe_allow_html=True)
            st.progress(score / 100)
    
    st.markdown("---")
    
    # Áreas de Foco
    st.markdown("<h2>🎯 Áreas de Foco</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">📊 Business Intelligence</div>
            <div class="card-text">
                Transformar dados em dashboards e relatórios que impulsionam decisões estratégicas.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-header">🤖 Machine Learning</div>
            <div class="card-text">
                Desenvolver modelos preditivos que agregam valor aos negócios.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-header">🔍 Data Science</div>
            <div class="card-text">
                Explorar dados complexos para descobrir insights ocultos.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Filosofia
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F8FAFB 0%, #F0F9F8 100%); 
                border: 1px solid #E5E7EB; border-radius: 8px; padding: 2rem;">
        <h3 style="color: #0F766E; margin-top: 0;">🌟 Minha Filosofia</h3>
        <p style="color: #6B7280; margin-bottom: 0;">
            Acredito que <strong>dados bem interpretados são a chave para decisões melhores</strong>. 
            Meu objetivo é não apenas criar análises, mas contar histórias com dados que inspirem ação.
            <br><br>
            Estou sempre em busca de aprender novas ferramentas, técnicas e melhores práticas 
            para me manter atualizado neste campo dinâmico e em constante evolução.
        </p>
    </div>
    """, unsafe_allow_html=True)
