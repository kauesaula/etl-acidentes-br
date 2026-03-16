# Pipeline ETL - Ocorrências de Acidentes Rodoviários

Este repositório contém um processo simplificado de ETL (Extração, Transformação e Carga) para processamento de dados de acidentes rodoviários no Brasil.

## Instruções de Execução

1. Clone este repositório em sua máquina:
   `git clone https://github.com/kauesaula/etl-acidentes-br.git`
2. Crie um ambiente virtual na pasta do projeto: 
   `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale a biblioteca necessária: 
   `pip install pandas`
5. **Importante:** Como os dados originais não são versionados, certifique-se de colocar o arquivo bruto `acidentes_brasil.csv` (fornecido na descrição do case) solto no diretório raiz do projeto.
6. Navegue até o diretório raiz, copie seu caminho e acesse-o pelo cmd. EXEMPLO: `cd C:\Users\Home\etl-acidentes-br`
7. Execute o pipeline de dados (Ingestão, Transformação e Carga): 
   `python case.py`

## Documentação das Transformações (Camada Prata)

Durante a Etapa 2, as seguintes transformações foram aplicadas para garantir a qualidade e padronização dos dados para os analistas:
 - Padronização de Colunas: Conversão de todos os nomes de colunas para minúsculas e substituição de espaços por underscores para facilitar consultas SQL futuras;
 - Tratamento de Datas: Conversão da coluna `data_inversa` para o formato `datetime` nativo do Pandas, permitindo agregações temporais;
 - Limpeza de Nulos: Linhas onde atributos críticos (`data_inversa` ou `uf`) estavam vazios foram removidas (dropna). Para os demais campos com dados faltantes, foi aplicado o preenchimento com a flag "Não Informado" para evitar quebra de tipagem;
- Filtragem: O dataset foi reduzido para conter apenas as ocorrências do estado de São Paulo (`SP`), simulando um recorte analítico específico.

## Automação

Para agendar este script para rodar todos os dias automaticamente em um ambiente de produção, eu utilizaria uma ferramenta de orquestração como o Apache Airflow. O script Python seria encapsulado dentro de uma DAG (Directed Acyclic Graph) com um agendamento definido (ex: `schedule_interval='@daily'`). Como alternativa mais simples para infraestruturas menores, o script poderia ser executado via GitHub Actions utilizando um gatilho de *cron schedule*, ou mesmo através de uma tarefa Cron (crontab) em uma máquina virtual Linux.

## Relato de Desafios

 Durante o desenvolvimento da ingestão (Camada Bronze), me deparei com um problema de dados tabulares brasileiros. O Pandas tentou ler o arquivo usando vírgulas, mas o CSV do governo usava ponto e vírgula (;). Além disso, ao abrir o DataFrame, a primeira coluna apresentava o erro de caracteres ï»¿id. Com ajuda da IA, pude entender que para resolver o desafio, bastava ajustar os parâmetros da função read_csv, forçando o sep=';' e alterando o encoding para utf-8-sig. Também adicionei o parâmetro on_bad_lines='skip' para garantir que uma única linha corrompida na origem não derrubasse todo o processo de ETL.
