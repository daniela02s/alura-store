# %%

import pandas as pd
import os
import carregar_dados

dados_consolidados = carregar_dados.carregar_e_consolidar_dados()

# Calcula as métricas de desempenho
df_metricas = dados_consolidados.groupby('Loja').agg(
Faturamento_Total=('Preço', 'sum'),
Avaliacao_Media=('Avaliação da compra', 'mean'),
Frete_Medio=('Frete', 'mean')
)

df_metricas.columns = ['Faturamento Total (R$)', 'Avaliação Média', 'Frete Médio (R$)']

# Formata a tabela (criando a variável 'df_metricas_formatado')
df_metricas_formatado = df_metricas.copy()
df_metricas_formatado['Faturamento Total (R$)'] = df_metricas_formatado['Faturamento Total (R$)'].map('R$ {:,.2f}'.format)
df_metricas_formatado['Avaliação Média'] = df_metricas_formatado['Avaliação Média'].map('{:.2f}'.format)
df_metricas_formatado['Frete Médio (R$)'] = df_metricas_formatado['Frete Médio (R$)'].map('R$ {:,.2f}'.format)

# Exibe o resultado final
print("\nAnálise de Desempenho Comparativo\n")
print(df_metricas_formatado)
# %%
