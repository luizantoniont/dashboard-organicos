import pandas as pd
import re

PATH = 'dashboard/data/input/cadastro_produtores.xlsx'

def load_data(PATH):

    try:
        data_excel = pd.read_excel(PATH, header=2)
        print('Dados carregados com sucesso')
        return data_excel
    
    except Exception as e:
        print(f'Erro ao carregar o arquivo')
        return None
 
def format_column_name():
    data_excel.columns = data_excel.columns.str.replace(' ', '_').str.lower()
    return data_excel

def save_data_csv(data_excel):

    try:
        data_excel.to_csv('dashboard/data/output/cadastro_produtores.csv', index=False)
        print('Arquivo salvo com sucesso')

    except Exception as e:
        print('Erro ao salvar o arquivo')
        return None
    
data_excel = load_data(PATH)
format_column_name()
save_data_csv(data_excel)


