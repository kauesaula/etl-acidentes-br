import pandas as pd
import os

def ingestao_bronze(file_path, bronze_dir):
    os.makedirs(bronze_dir, exist_ok=True)
    
    df = pd.read_csv(
        file_path, 
        sep=';', 
        encoding='utf-8-sig', # <--- Esta pequena mudança remove o ï»¿
        on_bad_lines='skip',
        low_memory=False
    )
    
    bronze_path = os.path.join(bronze_dir, 'acidentes_brasil_raw.csv')
    df.to_csv(bronze_path, index=False)
    
    return df

def transformacao_prata(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    if 'data_inversa' in df.columns:
        df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce')
    
    df = df.dropna(subset=['data_inversa', 'uf'])
    df = df.fillna('Não Informado')
    
    df_sp = df[df['uf'] == 'SP']
    
    return df_sp

def carga_prata(df, prata_dir):
    os.makedirs(prata_dir, exist_ok=True)
    prata_path = os.path.join(prata_dir, 'acidentes_sp_clean.csv')
    df.to_csv(prata_path, index=False)

def main():
    raw_file = 'acidentes_brasil.csv'
    bronze_dir = 'camada_bronze'
    prata_dir = 'camada_prata'

    df_raw = ingestao_bronze(raw_file, bronze_dir)
    df_clean = transformacao_prata(df_raw)
    carga_prata(df_clean, prata_dir)

if __name__ == "__main__":
    main()