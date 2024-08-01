import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv(r'C:\Users\luizz\Desktop\dashboard-organicos\dashboard\streamlit\data\output\cadastro_produtores.csv')

# visão geral 
distribuicao_tipo_entidade = data['tipo_de_entidade'].value_counts()
fig_tipo_entidade = px.bar(distribuicao_tipo_entidade, 
                           title='Distribuição por Tipo de Entidade',
                           template="simple_white",
                           labels={'tipo_de_entidade': 'Tipo de Entidade', 'value': 'Número de Produtores'})
fig_tipo_entidade.update_layout(showlegend=False)
st.plotly_chart(fig_tipo_entidade)


distribuicao_entidade = data['entidade'].value_counts().head()
fig_entidade = px.bar(distribuicao_entidade, orientation='h', 
                      title='Distribuição por Entidade',
                      template="simple_white",
                      labels={'entidade': 'Entidade', 'value': 'Número de cadastros'})
fig_entidade.update_layout(showlegend=False)
st.plotly_chart(fig_entidade)

distribuicao_uf = data['uf'].value_counts().reset_index(name='Número de Produtores')
fig_uf = px.bar(distribuicao_uf, x='uf', y='Número de Produtores',
                title='Distribuição por UF',
                template="simple_white",
                labels={'uf': 'UF', 'value': 'Número de cadastros'})
fig_uf.update_layout(showlegend=False)
st.plotly_chart(fig_uf)


produtores_por_uf = data.groupby(['uf', 'tipo_de_entidade']).size().reset_index(name='Número de Produtores')
produtores_por_uf = produtores_por_uf.sort_values(by='Número de Produtores', ascending=False)
fig = px.bar(produtores_por_uf, x='uf', y='Número de Produtores', 
             color='tipo_de_entidade', 
             title='Número de Produtores Orgânicos por UF e Tipo de Entidade',
             template="simple_white",
             labels={'uf': 'UF'})
fig.update_layout(legend_title_text='Tipo de Entidade',
                  xaxis_tickangle=-90)
st.plotly_chart(fig)


#distribuicao_pais = data['pais'].value_counts()
#st.dataframe(distribuicao_pais, width=300)