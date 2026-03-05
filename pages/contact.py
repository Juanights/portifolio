import streamlit as st

def show():
    st.title("✉️ Contato")
    
    st.markdown("""
    ---
    """)
    
    st.markdown("""
    Fico feliz em receber mensagens, sugestões e oportunidades de colaboração!
    Abaixo estão as formas de entrar em contato comigo.
    """)
    
    st.markdown("""
    ---
    """)
    
    # Seção de redes sociais e contatos
    st.markdown("### 🔗 Redes Sociais e Contatos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 💼 LinkedIn
        
        Conecte-se comigo no LinkedIn para acompanhar minha jornada profissional.
        
        [Acesse meu perfil](https://linkedin.com/in/seu-perfil)
        """)
    
    with col2:
        st.markdown("""
        #### 💻 GitHub
        
        Veja meus projetos e contribuições no GitHub.
        
        [Acesse meu GitHub](https://github.com/seu-usuario)
        """)
    
    with col3:
        st.markdown("""
        #### 📧 Email
        
        Envie um email diretamente para mim.
        
        [seu.email@gmail.com](mailto:seu.email@gmail.com)
        """)
    
    st.markdown("""
    ---
    """)
    
    # Formulário de contato
    st.markdown("### 📝 Formulário de Contato")
    
    with st.form("contact_form"):
        nome = st.text_input("Seu Nome *", placeholder="João Silva")
        email = st.text_input("Seu Email *", placeholder="joao@example.com")
        assunto = st.selectbox(
            "Assunto *",
            ["Oportunidade de Trabalho", "Colaboração em Projeto", "Dúvida Técnica", 
             "Feedback sobre Portfólio", "Outro"]
        )
        mensagem = st.text_area("Mensagem *", placeholder="Escreva sua mensagem aqui...", height=150)
        
        submitted = st.form_submit_button("Enviar Mensagem", use_container_width=True)
        
        if submitted:
            if nome and email and mensagem:
                st.success("""
                ✅ Obrigado pela mensagem! 
                
                Recebi seu contato e responderei em breve. 
                Verifique seu email para atualizações.
                """)
            else:
                st.error("❌ Por favor, preencha todos os campos obrigatórios (marcados com *).")
    
    st.markdown("""
    ---
    """)
    
    # Informações adicionais
    st.markdown("### ℹ️ Informações Adicionais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### ⏰ Disponibilidade
        
        - **Horário:** Segunda a Sexta, 9h às 18h (Horário de Brasília)
        - **Tempo de Resposta:** Geralmente 24-48 horas
        - **Timezone:** GMT-3 (Brasília)
        """)
    
    with col2:
        st.markdown("""
        #### 🎯 Interesses
        
        - Projetos de Análise de Dados
        - Consultoria em BI
        - Desenvolvimento de Modelos de ML
        - Parcerias em Pesquisa
        - Oportunidades de Aprendizado
        """)
    
    st.markdown("""
    ---
    """)
    
    # Rodapé
    st.markdown("""
    ### 🙏 Obrigado pela Visita!
    
    Espero que tenha apreciado meu portfólio. Qualquer dúvida ou sugestão, 
    não hesite em entrar em contato. Estou sempre aberto a feedback e novas oportunidades!
    """)
