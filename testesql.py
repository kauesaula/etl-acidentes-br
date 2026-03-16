'''
~k: o intuito deste código é justamente poder fazer o tracking da query SQL para entender se está ou não funcionando conforme deveria.
'''
import pandas as pd
import sqlite3

def testar_query():
    # Carrega os dados limpos da camada prata
    df = pd.read_csv('camada_prata/acidentes_sp_clean.csv')
    
    # Cria um banco de dados temporário local
    conexao = sqlite3.connect(':memory:')
    
    # Envia o Data Frame para dentro desse banco de dados como uma tabela
    df.to_sql('acidentes_sp_clean', conexao, index=False)
    
    #query:
    query = """
    SELECT 
        data_inversa, 
        COUNT(*) as total_acidentes
    FROM 
        acidentes_sp_clean
    GROUP BY 
        data_inversa
    ORDER BY 
        data_inversa;
    """
    
    # Executa a query e mostra os 10 primeiros resultados
    resultado = pd.read_sql_query(query, conexao)
    print(resultado.head(10))

if __name__ == "__main__":
    testar_query()