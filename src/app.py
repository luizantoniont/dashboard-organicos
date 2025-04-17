import pandas as pd
import plotly.express as px
import streamlit as st
import os

st.set_page_config(layout="wide")
@st.cache_data
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
    # Ajustar o caminho do arquivo CSV para ser relativo à raiz do projeto
    # quando app.py está dentro da pasta src.
    root_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(root_dir, '..', 'data', 'processed', 'cadastro_produtores.csv')
    csv_file_path = os.path.normpath(csv_file_path)  # Normaliza o caminho para evitar problemas com barras duplas ou barras invertidas.

    # Verificar se o arquivo existe
    if not os.path.exists(csv_file_path):
        st.error(f"Erro: O arquivo não foi encontrado no caminho especificado: {csv_file_path}")
        st.stop()

    # Carregar os dados
    data = load_data_csv(csv_file_path)
    if data is None:
        st.stop()

# Cria barras laterais e adiciona filtros
st.sidebar.header('Filtros')

# Cria filtro por Tipo de Entidade
tipos_entidade = sorted(data['tipo_de_entidade'].unique())
tipo_entidade_selecionado = st.sidebar.multiselect('Tipo de Entidade:', 
                                                    tipos_entidade, 
                                                    default=tipos_entidade)
data_filtrada_tipo = data[data['tipo_de_entidade'].isin(tipo_entidade_selecionado)]

# Cria filtro Entidade
entidades = sorted(data_filtrada_tipo['entidade'].unique())
entidade_selecionada = st.sidebar.multiselect('Entidade:',
                                                entidades, 
                                                default=entidades)
data_filtrada_entidade = data_filtrada_tipo[data_filtrada_tipo['entidade'].isin(entidade_selecionada)]

# Cria filtro UF
ufs = sorted(data_filtrada_entidade['uf'].unique())
uf_selecionada = st.sidebar.multiselect('UF:', ufs, default=ufs)
data_filtrada_uf = data_filtrada_entidade[data_filtrada_entidade['uf'].isin(uf_selecionada)]    


st.title('Cadastro de Produtores Orgânicos')
col1, col2 = st.columns(2)
with col1:
# Criar visualizações
    distribuicao_tipo_entidade = data['tipo_de_entidade'].value_counts()
    fig_tipo_entidade = px.bar(distribuicao_tipo_entidade, 
                            title='Distribuição por Tipo de Entidade',
                            template="simple_white",
                            labels={'tipo_de_entidade': 'Tipo de Entidade', 
                                    'value': 'Número de Produtores'})
    fig_tipo_entidade.update_layout(showlegend=False)
    st.plotly_chart(fig_tipo_entidade, use_container_width=True)

    distribuicao_entidade = data['entidade'].value_counts().head()
    fig_entidade = px.bar(distribuicao_entidade, 
                        orientation='h', 
                        title='Distribuição por Entidade',
                        template="simple_white",
                        labels={'entidade': 'Entidade', 'value': 
                                'Número de cadastros'})
    fig_entidade.update_layout(showlegend=False)
    st.plotly_chart(fig_entidade, use_container_width=True)
with col2:
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
    st.plotly_chart(fig_uf, use_container_width=True)

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
    fig_produtores_por_uf.update_layout(showlegend=True)
    st.plotly_chart(fig_produtores_por_uf, use_container_width=True)

