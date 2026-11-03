# 📊 Automação de Limpeza e Análise de Dados com Pandas

Este projeto é um script em Python desenvolvido para automatizar o tratamento e a análise de planilhas bagunçadas, simulando rotinas reais de Ciência e Engenharia de Dados.

## 🎯 O problema que ele resolve
Planilhas provenientes de formulários ou sistemas legados frequentemente contêm dados duplicados, valores nulos e formatos de data inconsistentes. Este script automatiza a limpeza desses dados e gera um relatório consolidado em Excel, economizando horas de trabalho manual.

## 🛠️ Tecnologias utilizadas
- **Python 3.8+**
- **Pandas**: Para manipulação, limpeza e agrupamento de dados (DataFrames).
- **OpenPyXL**: Para exportação do relatório final em múltiplas abas no Excel.

## ⚙️ Funcionalidades
- **Geração de Dados:** Um script (`gerador_dados.py`) cria uma base de dados simulada com erros intencionais (duplicatas, nulos, datas bagunçadas).
- **Limpeza:** O script principal (`main.py`) remove duplicatas, trata valores ausentes e padroniza datas.
- **Análise:** Calcula a média de notas agrupada por curso.
- **Exportação:** Gera um arquivo `relatorio_final.xlsx` com duas abas: `Dados_Limpos` e `Resumo_Cursos`.

## 🚀 Como rodar o projeto

Siga os passos abaixo no seu terminal:

**Passo 1: Clone o repositório**
    git clone https://github.com/DeathWingg/automacao-planilhas-pandas.git

**Passo 2: Instale as dependências**
    pip install -r requirements.txt

**Passo 3: Gere os dados sujos (opcional, para testar)**
    python gerador_dados.py

**Passo 4: Execute a automação de limpeza**
    python main.py

## 📁 Estrutura do projeto
    automacao-planilhas-pandas/
    │
    ├── gerador_dados.py      # Script que cria a planilha "suja" para testes
    ├── main.py               # Script principal que limpa e gera o relatório
    ├── requirements.txt      # Dependências do projeto
    └── .gitignore            # Arquivos que não devem ir para o GitHub

---
*Desenvolvido por [Wallysson Costa](https://github.com/DeathWingg)*