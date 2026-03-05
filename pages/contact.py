import streamlit as st

def show():
    st.markdown("# ✉️ Vamos Conversar")
    st.markdown("*Estou aberto a novas oportunidades e colaborações*")
    st.markdown("---")
    
    # Seção de contatos
    st.markdown("## 🔗 Conecte-se Comigo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("💼 LinkedIn")
        st.markdown("""
        Acompanhe minha jornada profissional e conecte-se comigo.
        
        [Visite meu perfil →](https://linkedin.com/in/seu-perfil)
        """)
    
    with col2:
        st.subheader("💻 GitHub")
        st.markdown("""
        Explore meus projetos e contribuições no GitHub.
        
        [Visite meu GitHub →](https://github.com/seu-usuario)
        """)
    
    with col3:
        st.subheader("📧 Email")
        st.markdown("""
        Envie um email diretamente para mim.
        
        [seu.email@gmail.com](mailto:seu.email@gmail.com)
        """)
    
    st.markdown("---")
    
    # Formulário de contato
    st.markdown("## 📝 Formulário de Contato")
    
    st.info("Preencha o formulário abaixo e entrarei em contato em breve. Geralmente respondo em 24-48 horas.")
    
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
        
        submitted = st.form_submit_button("Enviar Mensagem", use_container_width=True)
        
        if submitted:
            if nome and email and mensagem:
                st.success("""
                ✅ **Obrigado pela mensagem!**
                
                Recebi seu contato e responderei em breve. 
                Verifique seu email para atualizações.
                """)
            else:
                st.error("❌ Por favor, preencha todos os campos obrigatórios (marcados com *).")
    
    st.markdown("---")
    
    # Informações adicionais
    st.markdown("## ℹ️ Informações Adicionais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⏰ Disponibilidade")
        st.markdown("""
        **Horário:** Segunda a Sexta, 9h às 18h
        
        **Timezone:** GMT-3 (Brasília)
        
        **Tempo de Resposta:** 24-48 horas
        """)
    
    with col2:
        st.subheader("🎯 Interesses")
        st.markdown("""
        - Projetos de Análise de Dados
        - Consultoria em BI
        - Modelos de Machine Learning
        - Parcerias em Pesquisa
        - Oportunidades de Aprendizado
        """)
    
    st.markdown("---")
    
    # Rodapé
    st.markdown("## 🙏 Obrigado!")
    st.markdown("""
    Obrigado por visitar meu portfólio. Qualquer dúvida ou sugestão, 
    não hesite em entrar em contato. Estou sempre aberto a feedback e novas oportunidades!
    """)
