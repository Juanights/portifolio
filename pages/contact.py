import streamlit as st

def show():
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h1>Vamos Conversar</h1>
        <p style="font-size: 1.05rem; color: #6B7280;">Estou aberto a novas oportunidades e colaborações</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Seção de contatos
    st.markdown("<h2>🔗 Conecte-se Comigo</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">💼 LinkedIn</div>
            <div class="card-text">
                Acompanhe minha jornada profissional e conecte-se comigo.
                <br><br>
                <a href="https://linkedin.com/in/seu-perfil" target="_blank">
                    <strong>Visite meu perfil →</strong>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-header">💻 GitHub</div>
            <div class="card-text">
                Explore meus projetos e contribuições no GitHub.
                <br><br>
                <a href="https://github.com/seu-usuario" target="_blank">
                    <strong>Visite meu GitHub →</strong>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-header">📧 Email</div>
            <div class="card-text">
                Envie um email diretamente para mim.
                <br><br>
                <a href="mailto:seu.email@gmail.com">
                    <strong>seu.email@gmail.com →</strong>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Formulário de contato
    st.markdown("<h2>📝 Formulário de Contato</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-box-title">💡 Dica</div>
        <div class="info-box-text">
            Preencha o formulário abaixo e entrarei em contato em breve. 
            Geralmente respondo em 24-48 horas.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
    st.markdown("<h2>ℹ️ Informações Adicionais</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">⏰ Disponibilidade</div>
            <div class="card-text">
                <strong>Horário:</strong> Segunda a Sexta, 9h às 18h<br>
                <strong>Timezone:</strong> GMT-3 (Brasília)<br>
                <strong>Tempo de Resposta:</strong> 24-48 horas
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-header">🎯 Interesses</div>
            <div class="card-text">
                • Projetos de Análise de Dados<br>
                • Consultoria em BI<br>
                • Modelos de Machine Learning<br>
                • Parcerias em Pesquisa<br>
                • Oportunidades de Aprendizado
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Rodapé
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F8FAFB 0%, #F0F9F8 100%); 
                border: 1px solid #E5E7EB; border-radius: 8px; padding: 2rem; 
                text-align: center;">
        <h3 style="color: #0F766E; margin-top: 0;">🙏 Obrigado!</h3>
        <p style="color: #6B7280; margin-bottom: 0;">
            Obrigado por visitar meu portfólio. Qualquer dúvida ou sugestão, 
            não hesite em entrar em contato. Estou sempre aberto a feedback e novas oportunidades!
        </p>
    </div>
    """, unsafe_allow_html=True)
