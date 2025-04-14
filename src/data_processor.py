import pandas as pd
import os

def load_data(file_path):
    """
    Loads data from an Excel file.
    
    :param file_path: Path to the Excel file.
    :return: DataFrame with the data or None if an error occurs.
    """
    try:
        data = pd.read_excel(file_path, header=2)
        print(f'Dados carregados com sucesso de: , {file_path}')
        return data
    except FileNotFoundError as e:
        print(f'Erro: Arquivo não encontrado no caminho especificado: {e}')
        return None
    except pd.errors.ParserError as e:
        print(f'Erro ao analisar o arquivo: {file_path}: {e}')
        return None
    except Exception as e:
        print(f'Erro ao carregar o arquivo: {file_path}')
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
        # Garante que o diretório de destino exista
        output_dir = os.path.dirname(file_path)
        os.makedirs(output_dir, exist_ok=True)

        data.to_csv(file_path, index=False, encoding='utf-8') # Adicionado encoding
        print(f'Arquivo salvo com sucesso em: {file_path}')
    except Exception as e:
        print(f'Erro ao salvar o arquivo CSV em {file_path}: {e}')
        
if __name__ == '__main__':
    # --- Construção dinâmica dos caminhos ---
    # Obtém o diretório onde o script atual (data_processor.py) está localizado
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho para a pasta 'data' subindo um nível ('..')
    data_base_dir = os.path.join(script_dir, '..', 'data')

    # Constrói os caminhos completos para os arquivos de entrada e saída
    input_file_path = os.path.join(data_base_dir, 'raw', 'cadastro_produtores.xlsx')
    output_file_path = os.path.join(data_base_dir, 'processed', 'cadastro_produtores.csv')

    # Normaliza os caminhos (remove '..' e ajusta separadores)
    input_file_path = os.path.normpath(input_file_path)
    output_file_path = os.path.normpath(output_file_path)
    # --- Fim da construção dinâmica dos caminhos ---

    print(f"Processando arquivo de: {input_file_path}")
    data_excel = load_data(input_file_path)

    if data_excel is not None:
        data_formatted = format_column_names(data_excel)
        print(f"Salvando arquivo processado em: {output_file_path}")
        save_data_to_csv(data_formatted, output_file_path)
    else:
        print("Processamento cancelado devido a erro no carregamento dos dados.")



