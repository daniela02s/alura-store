# %%

import pandas as pd
import os

lista_dfs = []

# Carrega os dados de todas as lojas, adiciona uma coluna de identificação
# e retorna um único DF consolidado

def carregar_e_consolidar_dados():

    caminho_script = os.path.realpath(__file__)
    diretorio_script = os.path.dirname(caminho_script)
    raiz_projeto = os.path.join(diretorio_script, '..')
   
# Loop para carregar os arquivos de loja_1.csv até loja_4.csv

    for i in range(1, 5):
        caminho_arquivo = os.path.join(raiz_projeto, 'database', 'raw', f'loja_{i}.csv')
        df = pd.read_csv(caminho_arquivo)
        df['Loja'] = f'Loja {i}'
        lista_dfs.append(df)

    df_consolidado = pd.concat(lista_dfs, ignore_index=True)
    return df_consolidado

# %%
