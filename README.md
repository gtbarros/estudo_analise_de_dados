# 📊 Dashboard de Inteligência de Vendas e Controle de Devoluções

Uma solução completa de **Analytics e Business Intelligence** desenvolvida em **Python** utilizando **Pandas** e **Streamlit**. O sistema automatiza o pipeline de **ETL (Extract, Transform, Load)** de dados brutos de vendas e devoluções, consolidando métricas estratégicas em uma aplicação web interativa para suporte à tomada de decisão.

---

## 🎯 Escopo do Projeto & Solução de Negócio

* **Pipeline de ETL Automatizado:** Consolidação e tratamento de bases de dados heterogêneas contendo históricos transacionais de vendas, registros de devoluções e tabelas dimensionais de lojas e colaboradores.
* **Métricas de Eficiência Operacional:** Avaliação do desempenho de vendas por loja, volume de devoluções por motivo e cálculo de produtividade relativa por colaborador.
* **Interface de Visualização Executiva:** Dashboard centralizado para monitoramento comparativo de performance anual e diagnóstico rápido de lojas e regiões.

---

## 🛠️ Arquitetura e Tecnologias

* **Linguagem Core:** Python 3.x
* **Manipulação & Engenharia de Dados:** `pandas`, `openpyxl`
* **Visualização Web Interativa:** `streamlit`
* **Visualização Gráfica & Computação Numérica:** `matplotlib`, `numpy`

---

## 📁 Estrutura do Repositório

```text
.
├── main.py                     # Aplicação principal e dashboard interativo (Streamlit)
├── Venda_por_ano.ipynb         # Notebook Jupyter para prototipagem e pipeline de ETL
├── Total Vendas.xlsx           # Base de dados sumarizada de vendas
├── Vendas por ano.xlsx         # Dataset consolidado de vendas pós-tratamento
├── Devoluções por ano.xlsx     # Dataset consolidado de devoluções por período
└── Planejamento.txt            # Documentação de requisitos do projeto
```

---

## 🚀 Como Executar a Aplicação

### 1. Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em seu ambiente. Instale as dependências necessárias executando:

```bash
pip install streamlit pandas matplotlib numpy openpyxl
```

### 2. Execução do Dashboard
Navegue até o diretório do projeto e inicie o servidor do Streamlit:

```bash
streamlit run main.py
```

O dashboard estará disponível em seu navegador no endereço `http://localhost:8501`.

---

## 📈 Funcionalidades & Análises Disponíveis

* **Módulos Temporais:** Filtros integrados por abas para análise isolada dos anos de 2020, 2021 e 2022.
* **Análise Visual de Performance:**
  * **Volume de Vendas por Unidade:** Identificação das top unidades em volume transacionado.
  * **Métrica de Produtividade (Vendas x Colaboradores):** Relação entre o volume de vendas e o tamanho da equipe de cada loja.
  * **Controle de Devoluções:** Mapeamento do volume de devoluções por loja para ações preventivas de qualidade.
* **Tabelas de Dados Detalhadas:** Exibição das bases consolidadas com ordenação e formatação apropriadas.