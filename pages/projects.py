import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("📊 Meus Projetos")
    
    st.markdown("""
    ---
    """)
    
    # Seleção de projeto
    project = st.selectbox(
        "Selecione um projeto para explorar:",
        ["Análise Exploratória (EDA)", "Machine Learning", "Dashboard de BI"]
    )
    
    st.markdown("""
    ---
    """)
    
    if project == "Análise Exploratória (EDA)":
        show_eda_project()
    elif project == "Machine Learning":
        show_ml_project()
    elif project == "Dashboard de BI":
        show_dashboard_project()

def show_eda_project():
    st.markdown("### 📊 Análise Exploratória de Dados - Dataset Iris")
    
    st.markdown("""
    **Objetivo:** Explorar o famoso dataset Iris, compreendendo a distribuição das espécies 
    e as características das flores.
    """)
    
    # Carregar dados
    from sklearn.datasets import load_iris
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['Species'] = iris.target_names[iris.target]
    
    # Abas para diferentes análises
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Visão Geral", "🔍 Distribuições", "📊 Correlações", "📋 Dados"])
    
    with tab1:
        st.markdown("#### Estatísticas Descritivas")
        st.dataframe(df.describe(), use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", len(df))
        with col2:
            st.metric("Número de Features", len(iris.feature_names))
        with col3:
            st.metric("Espécies Únicas", df['Species'].nunique())
    
    with tab2:
        st.markdown("#### Distribuições das Features")
        
        feature = st.selectbox(
            "Selecione uma feature para visualizar:",
            iris.feature_names
        )
        
        fig = px.histogram(df, x=feature, color='Species', nbins=30, 
                          title=f"Distribuição de {feature}")
        st.plotly_chart(fig, use_container_width=True)
        
        # Gráfico de dispersão
        st.markdown("#### Gráfico de Dispersão")
        x_axis = st.selectbox("Eixo X:", iris.feature_names, key="x_scatter")
        y_axis = st.selectbox("Eixo Y:", iris.feature_names, key="y_scatter")
        
        fig_scatter = px.scatter(df, x=x_axis, y=y_axis, color='Species',
                                title=f"{x_axis} vs {y_axis}",
                                size_max=8)
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab3:
        st.markdown("#### Matriz de Correlação")
        
        # Calcular correlação
        corr_matrix = df.drop('Species', axis=1).corr()
        
        # Heatmap
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
        st.pyplot(fig)
    
    with tab4:
        st.markdown("#### Visualizar Dados Brutos")
        
        col1, col2 = st.columns(2)
        with col1:
            n_rows = st.slider("Número de linhas:", 5, 150, 10)
        with col2:
            species_filter = st.multiselect("Filtrar por espécie:", df['Species'].unique(), 
                                           default=df['Species'].unique())
        
        filtered_df = df[df['Species'].isin(species_filter)].head(n_rows)
        st.dataframe(filtered_df, use_container_width=True)

def show_ml_project():
    st.markdown("### 🤖 Projeto de Machine Learning - Classificação de Iris")
    
    st.markdown("""
    **Objetivo:** Treinar um modelo de Machine Learning para classificar espécies de flores 
    com base em suas características.
    """)
    
    # Carregar dados
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Fazer predições
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Abas
    tab1, tab2, tab3 = st.tabs(["📊 Performance", "🔮 Fazer Previsão", "📈 Feature Importance"])
    
    with tab1:
        st.markdown("#### Métricas do Modelo")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Acurácia", f"{accuracy:.2%}")
        with col2:
            st.metric("Conjunto de Treino", f"{len(X_train)} amostras")
        with col3:
            st.metric("Conjunto de Teste", f"{len(X_test)} amostras")
        
        # Matriz de Confusão
        st.markdown("#### Matriz de Confusão")
        cm = confusion_matrix(y_test, y_pred)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                   xticklabels=iris.target_names, yticklabels=iris.target_names)
        ax.set_ylabel('Verdadeiro')
        ax.set_xlabel('Predito')
        st.pyplot(fig)
    
    with tab2:
        st.markdown("#### Fazer uma Previsão")
        
        st.markdown("**Insira os valores das características da flor:**")
        
        col1, col2 = st.columns(2)
        with col1:
            sepal_length = st.slider("Comprimento da Sépala (cm):", 4.0, 8.0, 5.5)
            sepal_width = st.slider("Largura da Sépala (cm):", 2.0, 4.5, 3.0)
        with col2:
            petal_length = st.slider("Comprimento da Pétala (cm):", 1.0, 7.0, 3.5)
            petal_width = st.slider("Largura da Pétala (cm):", 0.1, 2.5, 1.0)
        
        # Fazer previsão
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        
        st.markdown("---")
        st.markdown("#### Resultado da Previsão")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"**Espécie Prevista:** {iris.target_names[prediction]}")
        with col2:
            st.info(f"**Confiança:** {probabilities[prediction]:.2%}")
        
        # Probabilidades para cada classe
        st.markdown("#### Probabilidades por Classe")
        prob_df = pd.DataFrame({
            'Espécie': iris.target_names,
            'Probabilidade': probabilities
        })
        
        fig = px.bar(prob_df, x='Espécie', y='Probabilidade', 
                    title="Distribuição de Probabilidades",
                    color='Probabilidade', color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("#### Importância das Features")
        
        feature_importance = pd.DataFrame({
            'Feature': iris.feature_names,
            'Importância': model.feature_importances_
        }).sort_values('Importância', ascending=False)
        
        fig = px.bar(feature_importance, x='Importância', y='Feature', 
                    orientation='h', title="Importância das Features",
                    color='Importância', color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)

def show_dashboard_project():
    st.markdown("### 📈 Dashboard de BI - Análise de Vendas")
    
    st.markdown("""
    **Objetivo:** Criar um dashboard interativo que monitora indicadores de vendas, 
    permitindo análise por período, região e produto.
    """)
    
    # Gerar dados fictícios
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    regions = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    products = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    
    data = []
    for _ in range(500):
        data.append({
            'Data': np.random.choice(dates),
            'Região': np.random.choice(regions),
            'Produto': np.random.choice(products),
            'Vendas': np.random.randint(100, 5000),
            'Quantidade': np.random.randint(1, 100)
        })
    
    df_sales = pd.DataFrame(data)
    df_sales['Mês'] = df_sales['Data'].dt.to_period('M')
    
    # Filtros
    st.markdown("#### 🔍 Filtros")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_regions = st.multiselect("Regiões:", regions, default=regions)
    with col2:
        selected_products = st.multiselect("Produtos:", products, default=products)
    with col3:
        date_range = st.date_input("Período:", 
                                   value=(df_sales['Data'].min(), df_sales['Data'].max()),
                                   max_value=df_sales['Data'].max())
    
    # Filtrar dados
    df_filtered = df_sales[
        (df_sales['Região'].isin(selected_regions)) &
        (df_sales['Produto'].isin(selected_products)) &
        (df_sales['Data'] >= pd.Timestamp(date_range[0])) &
        (df_sales['Data'] <= pd.Timestamp(date_range[1]))
    ]
    
    st.markdown("---")
    
    # KPIs
    st.markdown("#### 📊 Indicadores Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_vendas = df_filtered['Vendas'].sum()
        st.metric("Total de Vendas", f"R$ {total_vendas:,.0f}")
    with col2:
        total_quantidade = df_filtered['Quantidade'].sum()
        st.metric("Total de Itens", f"{total_quantidade:,}")
    with col3:
        ticket_medio = df_filtered['Vendas'].mean()
        st.metric("Ticket Médio", f"R$ {ticket_medio:,.0f}")
    with col4:
        num_transacoes = len(df_filtered)
        st.metric("Nº de Transações", f"{num_transacoes:,}")
    
    st.markdown("---")
    
    # Gráficos
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Vendas por Período", "🗺️ Vendas por Região", 
                                       "📦 Vendas por Produto", "📊 Análise Comparativa"])
    
    with tab1:
        vendas_por_mes = df_filtered.groupby('Mês')['Vendas'].sum().reset_index()
        vendas_por_mes['Mês'] = vendas_por_mes['Mês'].astype(str)
        
        fig = px.line(vendas_por_mes, x='Mês', y='Vendas', 
                     title="Evolução de Vendas por Mês",
                     markers=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        vendas_por_regiao = df_filtered.groupby('Região')['Vendas'].sum().sort_values(ascending=False)
        
        fig = px.bar(vendas_por_regiao, 
                    title="Vendas por Região",
                    labels={'value': 'Vendas (R$)', 'index': 'Região'},
                    color=vendas_por_regiao.values,
                    color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        vendas_por_produto = df_filtered.groupby('Produto')['Vendas'].sum().sort_values(ascending=False)
        
        fig = px.pie(values=vendas_por_produto.values, 
                    names=vendas_por_produto.index,
                    title="Distribuição de Vendas por Produto")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        vendas_regiao_produto = df_filtered.groupby(['Região', 'Produto'])['Vendas'].sum().reset_index()
        
        fig = px.bar(vendas_regiao_produto, x='Região', y='Vendas', color='Produto',
                    title="Vendas por Região e Produto",
                    barmode='group')
        st.plotly_chart(fig, use_container_width=True)
