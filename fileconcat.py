'''
 Python Script:
  Combine/Merge multiple CSV files using the Pandas library
'''
from os import listdir
from glob import glob
import pandas as pd
#import csv as csv

select_col = 'acao_codigo'
col_values = [1012, 1563, 2023, 2143, 2510, 2541]

colunas = ['ano_movimentacao',
            'mes_movimentacao',
            'orgao_codigo',
            'orgao_nome',
            'unidade_codigo',
            'unidade_nome',
            'categoria_economica_codigo',
            'categoria_economica_nome',
            'grupo_despesa_codigo',
            'grupo_despesa_nome',
            'modalidade_aplicacao_codigo',
            'modalidade_aplicacao_nome',
            'elemento_codigo',
            'elemento_nome',
            'subelemento_codigo',
            'subelemento_nome',
            'funcao_codigo',
            'funcao_nome',
            'subfuncao_codigo',
            'subfuncao_nome',
            'programa_codigo',
            'programa_nome',
            'acao_codigo',
            'acao_nome',
            'fonte_recurso_codigo',
            'fonte_recurso_nome',
            'empenho_ano',
            'empenho_modalidade_nome',
            'empenho_modalidade_codigo',
            'empenho_numero',
            'subempenho',
            'indicador_subempenho',
            'credor_codigo',
            'credor_nome',
            'modalidade_licitacao_codigo',
            'modalidade_licitacao_nome']

# Produce a single CSV after combining all files
def produceOneCSV(list_of_files, file_out):
   # Consolidate all CSV files into one object
   #panda_obj = pd.read_csv(readlist_of_files[0], sep=';')[1]

   df = pd.DataFrame({'A' : []})

   for file in list_of_files:
      data = pd.read_csv(file, sep=';', decimal=',')
      for coluna in colunas:
         data[coluna] = data[coluna].astype('category')
      for value in col_values:
         query = data[select_col] == value
         selected_data = data[query]
         df = pd.concat([df, selected_data])
      #print(selected_data.shape)

      #result_obj = pdlib.concat(pdlib.read_csv(file))
   # Convert the above object into a csv file and export
   df.drop(columns=['A'], inplace=True)
   df.to_csv(file_out, sep=';', index=False, encoding='utf-8')

# List all CSV files in the working dir
file_pattern = '.csv'
#list_of_files = [file for file in glob('*.{}'.format(file_pattern))]
list_of_all_files = listdir()

list_of_files = []

for f in list_of_all_files:
   if f.split('.')[1] == 'csv':
      list_of_files.append(f)

#print(list_of_files)

file_out = 'ConsolidateOutput.csv'
produceOneCSV(list_of_files, file_out)