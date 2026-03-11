import pandas as pd
import os

def ingestao_bronze(file_path, bronze_dir):
    """
    ~k: Aqui ele le o arquivo CSV bruto e salva uma copia exata na camada Bronze __garantia de historico__
    """
    print("Iniciando ingestão na Camada Bronze...")
    os.makedirs(bronze_dir, exist_ok=True)
    
    #Forcando o separador e o encoding para evitar erros com o padrao de formatacao Brasileiro
    df = pd.read_csv(
        file_path, 
        sep=';', 
        encoding='utf-8-sig',
        on_bad_lines='skip',
        low_memory=False
    )
    
    bronze_path = os.path.join(bronze_dir, 'acidentes_brasil_raw.csv')
    df.to_csv(bronze_path, index=False)
    print(f"Sucesso! Arquivo salvo no caminho: {bronze_path}\n")
    
    return df

def transformacao_prata(df):
    """
    ~k: Aqui ele vai aplicar regras de negocio, limpeza e filtros para a camada Prata, focando no estado SP __analise regional__
    """
    print("Iniciando transformações na Camada Prata...")
    
    #Padronizacao de Colunas
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    #Tratamento de datas
    if 'data_inversa' in df.columns:
        df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce')
    
    #Limpeza de nulos
    df = df.dropna(subset=['data_inversa', 'uf'])
    df = df.fillna('Não Informado')
    
    #Filtro regional
    df_sp = df[df['uf'] == 'SP']
    
    print(f"Transformação concluída. O total de registros válidos para SP é: {len(df_sp)}\n")
    return df_sp

def carga_prata(df, prata_dir):
    """
    ~k: salvando o Data Frame limpo e processado no diretorio final
    """
    os.makedirs(prata_dir, exist_ok=True)
    prata_path = os.path.join(prata_dir, 'acidentes_sp_clean.csv')
    df.to_csv(prata_path, index=False)
    print(f"Carga finalizada com sucesso, no caminho: {prata_path}")

def main():
    print("--- INICIANDO PIPELINE DE DADOS ---")
    raw_file = 'acidentes_brasil.csv'
    bronze_dir = 'camada_bronze'
    prata_dir = 'camada_prata'

    df_raw = ingestao_bronze(raw_file, bronze_dir)
    df_clean = transformacao_prata(df_raw)
    carga_prata(df_clean, prata_dir)
    print("--- PIPELINE CONCLUÍDO ---")

if __name__ == "__main__":
    main()