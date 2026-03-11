# Pipeline ETL - Ocorrências de Acidentes Rodoviários

Este repositório contém um processo simplificado de ETL (Extração, Transformação e Carga) para processamento de dados de acidentes rodoviários no Brasil.

## Instruções de Execução

1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install pandas`
5. Certifique-se de que o arquivo original `acidentes_brasil.csv` está no diretório raiz.
6. Execute o script principal: `python etl_script.py`

## Documentação das Transformações (Camada Prata)

Durante a Etapa 2, as seguintes transformações foram aplicadas para garantir a qualidade e padronização dos dados para os analistas:
- **Padronização de Colunas:** Conversão de todos os nomes de colunas para minúsculas e substituição de espaços por underscores para facilitar consultas SQL futuras.
- **Tratamento de Datas:** Conversão da coluna `data_inversa` para o formato `datetime` nativo do Pandas, permitindo agregações temporais.
- **Limpeza de Nulos:** Linhas onde atributos críticos (`data_inversa` ou `uf`) estavam vazios foram removidas (dropna). Para os demais campos com dados faltantes, foi aplicado o preenchimento com a flag "Não Informado" para evitar quebra de tipagem.
- **Filtragem:** O dataset foi reduzido para conter apenas as ocorrências do estado de São Paulo (`SP`), simulando um recorte analítico específico.

## Automação (Diferencial)

Para agendar este script para rodar todos os dias automaticamente em um ambiente de produção, eu utilizaria uma ferramenta de orquestração como o Apache Airflow. O script Python seria encapsulado dentro de uma DAG (Directed Acyclic Graph) com um agendamento definido (ex: `schedule_interval='@daily'`). Como alternativa mais simples para infraestruturas menores, o script poderia ser executado via GitHub Actions utilizando um gatilho de *cron schedule*, ou mesmo através de uma tarefa Cron (crontab) em uma máquina virtual Linux.

## Relato de Desafios

[Descreva aqui com suas palavras um desafio real que você enfrentou ao rodar o script no seu ambiente, como por exemplo descobrir o encoding correto do CSV original ou lidar com algum formato de data inesperado, e como você usou a documentação para contornar o problema.]