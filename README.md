# Pipeline_elt

📊 Pipeline de Dados em Python (ETL)
📌 Visão Geral

Este projeto implementa um pipeline de dados simples (ETL) utilizando Python e Pandas.
O objetivo é extrair dados brutos, aplicar transformações para garantir qualidade e gerar um dataset final pronto para análise ou BI.

O projeto simula um cenário real de dados corporativos, lidando com:

valores ausentes

dados duplicados

inconsistências de texto

tipos incorretos

🔄 O que é ETL?

ETL é um processo fundamental em engenharia e análise de dados:

E — Extract (Extrair)
Leitura de dados a partir de arquivos CSV brutos.

T — Transform (Transformar)
Limpeza, padronização, validação e tratamento dos dados.

L — Load (Carregar)
Exportação dos dados tratados para um novo arquivo CSV.

🎯 Objetivo do Projeto

Ler um arquivo CSV com dados brutos

Aplicar regras de qualidade de dados

Padronizar informações textuais

Remover inconsistências e duplicidades

Exportar um arquivo final confiável

📌 O resultado é um dataset pronto para uso em Power BI, Excel ou bancos de dados.

📂 Estrutura do Projeto

pipeline-etl
│
├── data
│   ├── raw_dados.csv          # Dados brutos (entrada)
│   └── dados_tratados.csv     # Dados limpos (saída)
│
├── etl.py                     # Script principal do pipeline
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação

⚙️ Tecnologias Utilizadas

Python 3

Pandas

Bibliotecas padrão do Python

🧠 Transformações Aplicadas

Durante a etapa de Transform, o pipeline realiza:

Remoção ou tratamento de valores nulos

Padronização de textos (nomes e cidades)

Conversão correta de tipos de dados

Remoção de registros duplicados

Aplicação de regras de negócio (ex: idade mínima)

Essas etapas garantem qualidade e consistência dos dados.

📈 Possíveis Evoluções

Geração de relatório de qualidade de dados

Logs estruturados da execução

Suporte a múltiplos arquivos

Integração com banco de dados

Execução via linha de comando (CLI)

⭐ Por que este projeto é relevante?

✔ Simula um problema real do mercado
✔ Demonstra domínio de ETL e Pandas
✔ Mostra preocupação com qualidade de dados
✔ Excelente para portfólio de dados e BI
