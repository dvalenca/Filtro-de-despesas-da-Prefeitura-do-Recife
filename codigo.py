import pandas as pd
from os import listdir

headers = ["ano_movimentacao",
            "mes_movimentacao",
            "orgao_codigo",
            "orgao_nome",
            "unidade_codigo",
            "unidade_nome",
            "categoria_economica_codigo",
            "categoria_economica_nome",
            "grupo_despesa_codigo",
            "grupo_despesa_nome",
            "modalidade_aplicacao_codigo",
            "modalidade_aplicacao_nome",
            "elemento_codigo",
            "elemento_nome",
            "subelemento_codigo",
            "subelemento_nome",
            "funcao_codigo",
            "funcao_nome",
            "subfuncao_codigo",
            "subfuncao_nome",
            "programa_codigo",
            "programa_nome",
            "acao_codigo",
            "acao_nome",
            "fonte_recurso_codigo",
            "fonte_recurso_nome",
            "empenho_ano",
            "empenho_modalidade_nome",
            "empenho_modalidade_codigo",
            "empenho_numero",
            "subempenho",
            "indicador_subempenho",
            "credor_codigo",
            "credor_nome",
            "modalidade_licitacao_codigo",
            "modalidade_licitacao_nome",
            "valor_empenhado",
            "valor_liquidado",
            "valor_pago"]

#print(headers)

of = listdir()

#print(of)

for f in of:
    if f.split('.')[1] == 'csv':
        df = pd.read_csv(f, sep=';')
        print(df)

        