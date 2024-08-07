import pandas as pd

INPUT_PATH = 'dashboard/data/input/cadastro_produtores.xlsx'
OUTPUT_PATH = 'dashboard\src\cadastro_produtores.csv'

def load_data(file_path):
    """Loads data form an Excel file.
    
    :param file_path: Path to the Excel file.
    :return: DataFrame with the data or None if an error
    """
    try:
        data = pd.read_excel(file_path, header=2)
        print('Dados carregados com sucesso')
        return data
    except pd.errors.ParserError as e:
        print(f'Dados carregados com sucesso {e}')
        return None
    except Exception as e:
        print(f'Erro ao carregar o arquivo {e}')
        
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
        data.to_csv('file_path', index=False)
        print('Arquivo salvo com sucesso')
    except Exception as e:
        print('Erro ao salvar o arquivo')
        
if __name__ == '__main__':
    data_excel = load_data(INPUT_PATH)
    if data_excel is not None:
        data_excel = format_column_names(data_excel)
        save_data_to_csv(data_excel, OUTPUT_PATH)



