import streamlit as st

def show():
    st.markdown("# Contato")
    st.markdown("Conecte-se comigo para oportunidades e colaborações")
    st.markdown("---")
    
    # Canais de Contato
    st.markdown("## Canais de Contato")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### LinkedIn")
        st.markdown("""
        Acompanhe minha jornada profissional e conecte-se comigo.
        
        [Visite meu perfil](https://linkedin.com/in/seu-perfil)
        """)
    
    with col2:
        st.markdown("### GitHub")
        st.markdown("""
        Explore meus projetos e contribuições.
        
        [Visite meu GitHub](https://github.com/seu-usuario)
        """)
    
    with col3:
        st.markdown("### Email")
        st.markdown("""
        Envie um email diretamente.
        
        [seu.email@gmail.com](mailto:seu.email@gmail.com)
        """)
    
    st.markdown("---")
    
    # Formulário de Contato
    st.markdown("## Formulário de Contato")
    
    st.info("Preencha o formulário abaixo. Responderei em 24-48 horas.")
    
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
    
    st.markdown("---")
    
    # Informações Adicionais
    st.markdown("## Informações Adicionais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Disponibilidade")
        st.markdown("""
        **Horário:** Segunda a Sexta, 9h às 18h
        
        **Timezone:** GMT-3 (Brasília)
        
        **Tempo de Resposta:** 24-48 horas
        """)
    
    with col2:
        st.markdown("### Interesses")
        st.markdown("""
        - Projetos de Análise de Dados
        - Consultoria em Business Intelligence
        - Desenvolvimento de Modelos de ML
        - Parcerias em Pesquisa
        - Oportunidades de Aprendizado
        """)
