import pandas as pd
import os

INPUT_PATH = 'data/input/cadastro_produtores.xlsx'
OUTPUT_PATH = 'data/output/cadastro_produtores.csv'

def load_data(file_path):
    """
    Loads data from an Excel file.
    
    :param file_path: Path to the Excel file.
    :return: DataFrame with the data or None if an error occurs.
    """
    try:
        data = pd.read_excel(file_path, header=2)
        print('Dados carregados com sucesso')
        return data
    except FileNotFoundError as e:
        print(f'Erro: Arquivo não encontrado no caminho especificado: {e}')
        return None
    except pd.errors.ParserError as e:
        print(f'Erro ao analisar o arquivo: {e}')
        return None
    except Exception as e:
        print(f'Erro ao carregar o arquivo: {e}')
        return None
        
def format_column_names(data):
    """
    Formats column names to replace spaces with underscores and convert to 
    lowercase.

    :param data: DataFrame whose column names will be formatted.
    :return: DataFrame with formatted column names.
    """
    data.columns = data.columns.str.replace(' ', '_').str.lower()
    return data

def save_data_to_csv(data, file_path):
    """
    Saves the DataFrame to a CSV file.

    :param data: DataFrame to be saved.
    :param file_path: Path to the output CSV file.
    :return: None 
    """
    try:
        # Criar o diretório de saída, se não existir
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data.to_csv(file_path, index=False)
        print('Arquivo salvo com sucesso')
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')
        
if __name__ == '__main__':
    data_excel = load_data(INPUT_PATH)
    if data_excel is not None:
        data_excel = format_column_names(data_excel)
        save_data_to_csv(data_excel, OUTPUT_PATH)



