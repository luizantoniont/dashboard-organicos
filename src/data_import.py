import pandas as pd
import os

URL_ROOT = (
'https://www.gov.br/agricultura/pt-br/assuntos/sustentabilidade/organicos/CNPO_MAPA_14_01_2025_Imascara.xlsx'
)
OUTPUT_DIR = 'data/input/'

def import_data(URL_ROOT):
    """
    Import data from an Excel file.

    :param url: URL to the Excel file.
    :return: DataFrame with the data or None is an error occurrs"""
    try:
        data = pd.read_excel(URL_ROOT)
        print('Dados importados com sucesso')
        return data
    except pd.errors.ParserError as e:
        print(f'Erro ao analisar o arquivo: {e}')
    except Exception as e:
        print(f'Erro ao importar o arquivo: {e}')
        return None

def save_data(data, file_path):
    """
    Save the Dataframe to an Excel file.

    :param data: DataFrame to an Excel file.
    :param file_path: Path to the output Excel file.
    :return: None
    """

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data.to_excel(file_path, index=False)
        print('Dados salvos com sucesso')
        return data
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')

def main():
    data = import_data(URL_ROOT)
    if data is not None:
        output_file_path = f'{OUTPUT_DIR}cadastro_produtores.xlsx'
        save_data(data, output_file_path)

if __name__ == '__main__':
    main()