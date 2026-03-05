import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def show():
    st.markdown("# Projetos")
    st.markdown("Análise técnica de dados e modelagem preditiva")
    st.markdown("---")
    
    # Seletor de Projeto
    project = st.selectbox(
        "Selecione um projeto:",
        ["Análise Exploratória (Iris)", "Machine Learning (Classificação)", "Dashboard de Vendas"]
    )
    
    if project == "Análise Exploratória (Iris)":
        show_eda()
    elif project == "Machine Learning (Classificação)":
        show_ml()
    else:
        show_dashboard()

def show_eda():
    st.markdown("## Análise Exploratória - Dataset Iris")
    st.markdown("Exploração detalhada do famoso dataset Iris com visualizações interativas.")
    
    # Carregar dados
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Visão Geral", "Distribuições", "Correlações", "Dados"])
    
    with tab1:
        st.markdown("### Estatísticas Descritivas")
        st.dataframe(df.describe(), use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", len(df))
        with col2:
            st.metric("Número de Features", len(iris.feature_names))
        with col3:
            st.metric("Espécies Únicas", df['species'].nunique())
    
    with tab2:
        st.markdown("### Distribuições de Features")
        
        feature = st.selectbox("Selecione uma feature:", iris.feature_names)
        
        fig = go.Figure()
        for species in iris.target_names:
            data = df[df['species'] == species][feature]
            fig.add_trace(go.Histogram(
                x=data,
                name=species,
                opacity=0.7,
                marker_color=['#1e40af', '#3b82f6', '#60a5fa'][list(iris.target_names).index(species)]
            ))
        
        fig.update_layout(
            title=f"Distribuição de {feature}",
            xaxis_title=feature,
            yaxis_title="Frequência",
            barmode='overlay',
            template='plotly_white',
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Matriz de Correlação")
        
        corr_matrix = df.drop('species', axis=1).corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='Blues',
            zmid=0
        ))
        
        fig.update_layout(
            title="Correlação entre Features",
            template='plotly_white',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.markdown("### Dataset Completo")
        st.dataframe(df, use_container_width=True)

def show_ml():
    st.markdown("## Machine Learning - Classificação")
    st.markdown("Modelo preditivo para classificação de espécies de Iris.")
    
    # Carregar e preparar dados
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predições
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["Desempenho", "Matriz de Confusão", "Previsão"])
    
    with tab1:
        st.markdown("### Métricas de Desempenho")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Acurácia", f"{accuracy:.2%}")
        with col2:
            st.metric("Modelo", "Random Forest")
        with col3:
            st.metric("Estimadores", "100")
        
        st.markdown("### Relatório de Classificação")
        report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df, use_container_width=True)
    
    with tab2:
        st.markdown("### Matriz de Confusão")
        
        cm = confusion_matrix(y_test, y_pred)
        
        fig = go.Figure(data=go.Heatmap(
            z=cm,
            x=iris.target_names,
            y=iris.target_names,
            colorscale='Blues',
            text=cm,
            texttemplate='%{text}',
            textfont={"size": 12}
        ))
        
        fig.update_layout(
            title="Matriz de Confusão",
            xaxis_title="Predito",
            yaxis_title="Real",
            template='plotly_white',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("### Fazer Previsão")
        
        col1, col2 = st.columns(2)
        with col1:
            sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.5)
            sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
        
        with col2:
            petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 3.5)
            petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)
        
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        st.markdown("### Resultado")
        st.success(f"**Espécie Prevista:** {iris.target_names[prediction]}")
        
        col1, col2, col3 = st.columns(3)
        for i, species in enumerate(iris.target_names):
            with [col1, col2, col3][i]:
                st.metric(species, f"{probability[i]:.2%}")

def show_dashboard():
    st.markdown("## Dashboard de Vendas")
    st.markdown("Análise de performance de vendas com KPIs e tendências.")
    
    # Gerar dados simulados
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=90, freq='D')
    data = {
        'Data': dates,
        'Vendas': np.random.randint(5000, 15000, 90),
        'Região': np.random.choice(['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'], 90),
        'Categoria': np.random.choice(['Eletrônicos', 'Vestuário', 'Alimentos', 'Serviços'], 90)
    }
    df_sales = pd.DataFrame(data)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Vendas", f"R$ {df_sales['Vendas'].sum():,.0f}")
    with col2:
        st.metric("Média Diária", f"R$ {df_sales['Vendas'].mean():,.0f}")
    with col3:
        st.metric("Máximo", f"R$ {df_sales['Vendas'].max():,.0f}")
    with col4:
        st.metric("Mínimo", f"R$ {df_sales['Vendas'].min():,.0f}")
    
    st.markdown("---")
    
    # Gráficos
    tab1, tab2, tab3 = st.tabs(["Tendência", "Por Região", "Por Categoria"])
    
    with tab1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_sales['Data'],
            y=df_sales['Vendas'],
            mode='lines',
            name='Vendas',
            line=dict(color='#1e40af', width=2)
        ))
        fig.update_layout(
            title="Tendência de Vendas",
            xaxis_title="Data",
            yaxis_title="Vendas (R$)",
            template='plotly_white',
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        sales_by_region = df_sales.groupby('Região')['Vendas'].sum().sort_values(ascending=False)
        fig = go.Figure(data=[
            go.Bar(x=sales_by_region.index, y=sales_by_region.values, marker_color='#1e40af')
        ])
        fig.update_layout(
            title="Vendas por Região",
            xaxis_title="Região",
            yaxis_title="Vendas (R$)",
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        sales_by_category = df_sales.groupby('Categoria')['Vendas'].sum().sort_values(ascending=False)
        fig = go.Figure(data=[
            go.Pie(labels=sales_by_category.index, values=sales_by_category.values, marker_colors=['#1e40af', '#3b82f6', '#60a5fa', '#93c5fd'])
        ])
        fig.update_layout(title="Distribuição por Categoria")
        st.plotly_chart(fig, use_container_width=True)
