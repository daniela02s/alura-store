# Análise de Desempenho - Alura Store

> Análise de dados de vendas de quatro lojas da rede Alura Store para identificar a unidade com menor eficiência e fornecer uma recomendação estratégica de venda.

## 1. Descrição do Projeto
Este projeto foi desenvolvido como parte de um desafio de ciência de dados, com o objetivo de auxiliar o "Senhor João", proprietário da rede fictícia Alura Store, a tomar uma decisão de negócios. A análise consiste em avaliar dados de vendas, desempenho e avaliações das quatro lojas para identificar qual delas apresenta a menor performance. A recomendação final é baseada em uma análise quantitativa e visual dos dados, visando a venda da unidade menos eficiente para viabilizar novos investimentos.

## 2. Funcionalidades

- **Carregamento e Limpeza de Dados:** Scripts para carregar e consolidar dados de vendas de múltiplos arquivos CSV.
- **Análise de Métricas:** Cálculo de KPIs (Key Performance Indicators) essenciais, como:
  - Faturamento total por loja.
  - Avaliação média dos clientes.
  - Produtos e categorias mais/menos vendidos.
  - Custo médio do frete.
- **Visualização de Dados:** Geração de gráficos (barras, pizza, dispersão, linhas e heatmap) para apresentar os resultados de forma clara.
- **Análise Geográfica (Extra):** Mapeamento das vendas por latitude e longitude para identificar concentrações e padrões regionais.

## 3. Tecnologias Utilizadas

As seguintes tecnologias e bibliotecas foram utilizadas no desenvolvimento deste projeto:

- **Python 3:** Linguagem de programação principal.
- **Pandas:** Para manipulação e análise de dados.
- **Matplotlib e Seaborn:** Para a criação das visualizações de dados.
- **Jupyter Notebook:** Como ambiente de desenvolvimento para a análise interativa.
- **Conda:** Para gerenciamento do ambiente virtual e das dependências.

## 4. Acesso ao Projeto

Você pode acessar os arquivos do projeto de duas formas:

- **Clonando o repositório:**
  ```bash
  git clone https://github.com/daniela02s/alura-store.git
  ```
- **Baixando o ZIP:**
  Na página do repositório, clique em "Code" > "Download ZIP".

## 5. Abrir e Rodar o Projeto

Para executar a análise em sua máquina local, siga os passos abaixo.

### Pré-requisitos

- Python 3.x
- Conda (ou Mamba/Miniconda) instalado.

### Instalação

1.  **Crie o Ambiente Virtual:**
    No terminal, dentro da pasta do projeto, crie um novo ambiente Conda com as dependências necessárias.
    ```bash
    conda create --name alura-store python=3. pandas matplotlib seaborn jupyter
    ```

2.  **Ative o Ambiente:**
    Antes de prosseguir, ative o ambiente que você acabou de criar.
    ```bash
    conda activate alura-store
    ```

### Execução

1.  **Inicie o Jupyter Notebook:**
    Com o ambiente ativado, execute o comando:
    ```bash
    jupyter notebook
    ```

2.  **Abra o Notebook de Análise:**
    Seu navegador será aberto. Nele, navegue até a pasta `notebooks/` e abra o arquivo `analise_alura_store.ipynb`.

3.  **Execute as Células:**
    Execute as células do notebook em sequência para carregar os dados, realizar os cálculos e gerar todos os gráficos e resultados.

## 6. Conclusão

A análise concluiu que a **Loja 4 é a unidade com o menor desempenho financeiro**, sendo a recomendada para venda. O relatório final detalhado e todos os gráficos gerados podem ser encontrados na pasta `relatorios/` e no notebook principal.
