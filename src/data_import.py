import pandas as pd
import os
<<<<<<< HEAD
# teste
=======

>>>>>>> 08fe3d6d3f01ed3337323b9308383e8a5668851d
URL_ROOT = (
'https://www.gov.br/agricultura/pt-br/assuntos/sustentabilidade/organicos/CNPO_MAPA_01_04_2025MASCARADO.xlsx')

def import_data(url):
    """
    Import data from an Excel file.

    :param url: URL to the Excel file.
    :return: DataFrame with the data or None is an error occurrs"""
    try:
        data = pd.read_excel(url)
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
        # Garante que o diretório de destino exista
        output_dir = os.path.dirname(file_path)
        os.makedirs(output_dir, exist_ok=True)

        data.to_excel(file_path, index=False)
        print(f'Dados salvos com sucesso em: {file_path}')
        # Removido 'return data' para alinhar com a docstring e o propósito (apenas salvar)
    except Exception as e:
        print(f'Erro ao salvar o arquivo em {file_path}: {e}')
        # Não retorna nada em caso de erro

def main():
    data = import_data(URL_ROOT)
    if data is not None:
        # Obtém o diretório onde o script atual (data_import.py) está localizado
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Constrói o caminho para a pasta 'data/input' subindo um nível ('..') a partir de 'src'
        # e depois entrando em 'data/input'
        input_folder_path = os.path.join(script_dir, '..', 'data', 'raw')

        # Constrói o caminho completo para o arquivo de saída
        output_file_path = os.path.join(input_folder_path, 'cadastro_produtores.xlsx')

        # Normaliza o caminho (remove '..' e ajusta separadores como '/' ou '\')
        output_file_path = os.path.normpath(output_file_path)

        print(f"Tentando salvar os dados em: {output_file_path}")
        save_data(data, output_file_path)
    else:
        print("Não foi possível importar os dados. O salvamento foi cancelado.")

if __name__ == '__main__':
    main()