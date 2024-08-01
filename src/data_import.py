import pandas as pd

URL_ROOT = 'https://www.gov.br/agricultura/pt-br/assuntos/sustentabilidade/organicos/CNPO_MAPA_03_07_2024_IMASCARA.xlsx'

def import_data(URL_ROOT):

    try:
        data = pd.read_excel(URL_ROOT)
        print('Dados importados com sucesso')
        return data
    
    except Exception as e:
        print(f'Erro ao importar o arquivo')
        return None

def save_data_excel(data):

    try:
        data.to_excel('dashboard/data/input/cadastro_produtores.xlsx', index=False)
        print('Dados salvos com sucesso')
        return data
    
    except Exception as e:
        print(f'Erro ao salvar o arquivo')
        return None
    
data = import_data(URL_ROOT)
save_data_excel(data)

