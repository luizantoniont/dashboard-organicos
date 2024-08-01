import pandas as pd
import sqlite3

database = 'cadastro_produtores.db'
table_name = 'cad_prod_org'

data = pd.read_csv(r'C:\Users\luizz\Desktop\dashboard-organicos\dashboard\data\output\cadastro_produtores.csv')

def create_database_from_dataframe(data, database, table_name):
    
    try:
        conn = sqlite3.connect(database)
        print(f'Conexão estabelecida com sucesso ao banco de dados {database}')

        data.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Tabela '{table_name}' criada com sucesso no banco de dados {database}")

    except Exception as e:
        print(f'Erro ao criar banco de dados ou tabela: {e}')
    finally:
        if conn:
           conn.close()

create_database_from_dataframe(data, database, table_name)

