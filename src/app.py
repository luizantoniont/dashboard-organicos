import pandas as pd
import plotly.express as px
import streamlit as st
import os

def load_data_csv(file_path):
    """
    Loads data from a CSV file.
    
    :param file_path: Path to the CSV file.
    :return: DataFrame with the data or None if an error occurs.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Erro: Arquivo não encontrado no caminho especificado: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        st.error("Erro: O arquivo está vazio.")
        return None
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

# Início da aplicação Streamlit
if __name__ == '__main__':
    # Parametrizar o caminho do arquivo CSV
    csv_file_path = os.path.join('data', 'output', 'cadastro_produtores.csv')

    # Verificar se o arquivo existe
    if not os.path.exists(csv_file_path):
        st.error(f"Erro: O arquivo não foi encontrado no caminho especificado: {csv_file_path}")
        st.stop()

    # Carregar os dados
    data = load_data_csv(csv_file_path)
    if data is None:
        st.stop()

# Criar visualizações
distribuicao_tipo_entidade = data['tipo_de_entidade'].value_counts()
fig_tipo_entidade = px.bar(distribuicao_tipo_entidade, 
                           title='Distribuição por Tipo de Entidade',
                           template="simple_white",
                           labels={'tipo_de_entidade': 'Tipo de Entidade', 
                                   'value': 'Número de Produtores'})
fig_tipo_entidade.update_layout(showlegend=False)

distribuicao_entidade = data['entidade'].value_counts().head()
fig_entidade = px.bar(distribuicao_entidade, 
                      orientation='h', 
                      title='Distribuição por Entidade',
                      template="simple_white",
                      labels={'entidade': 'Entidade', 'value': 
                              'Número de cadastros'})
fig_entidade.update_layout(showlegend=False)

distribuicao_uf = (
    data['uf'].value_counts().reset_index(name='Número de Produtores')
)
fig_uf = px.bar(distribuicao_uf, 
                x='uf', 
                y='Número de Produtores',
                title='Distribuição por UF',
                template="simple_white",
                labels={'uf': 'UF', 'value': 'Número de cadastros'})
fig_uf.update_layout(showlegend=False)

produtores_por_uf = (
    data.groupby(['uf', 'tipo_de_entidade'])
       .size()
       .reset_index(name='Número de Produtores')
)
produtores_por_uf = produtores_por_uf.sort_values(by='Número de Produtores', 
                                                  ascending=False)
fig_produtores_por_uf = px.bar(
    produtores_por_uf, 
    x='uf', 
    y='Número de Produtores', 
    color='tipo_de_entidade', 
    title='Número de Produtores Orgânicos por UF e Tipo de Entidade',
    template="simple_white",
    labels={'uf': 'UF'}
)
fig_produtores_por_uf.update_layout(legend_title_text='Tipo de Entidade',
                                    xaxis_tickangle=-90)

# Exibir visualizações no Streamlit
st.title('Cadastro de Produtores Orgânicos')
st.plotly_chart(fig_uf)
st.plotly_chart(fig_produtores_por_uf)
st.plotly_chart(fig_entidade)
st.plotly_chart(fig_tipo_entidade)

