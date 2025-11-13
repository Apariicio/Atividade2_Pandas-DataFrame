import pandas as pd
from pandas import Flags

jogadores = pd.read_csv('C:\\Users\\Acer\\Documents\\UNA_CIÊNCIAS DA COMPUTAÇÃO\\4 semestre\\Reinaldo - Terça Feira\\Atividade 2\\Jogadores.csv', encoding='UTF-8', delimiter=';')

df = pd.DataFrame(jogadores)
#print(df)
#salario_maior_de_200mil = df[df['salario_do_jogador'] > 200000.00][['nome_do_jogador', 'nome_time_jogador']]
#print(salario_maior_de_200mil)
#nome_salario_de_mg = df[df['nome_estado_jogador'] == 'MG'][['nome_do_jogador', 'salario_do_jogador']]
#print(nome_salario_de_mg)
#nome_jogador_contem_letra_u = df[df['nome_do_jogador'].str.contains('u', case=False, na=False)][['nome_do_jogador', 'nome_time_jogador']]
#print(nome_jogador_contem_letra_u)
#salario_ordem_decre = df.sort_values(by='salario_do_jogador', ascending=False)[['nome_do_jogador', 'salario_do_jogador', 'nome_time_jogador']]
#print(salario_ordem_decre)
#time_cres_salario_decres = df.sort_values(by=['nome_time_jogador', 'salario_do_jogador'], ascending=[True, False, ])[['nome_do_jogador', 'salario_do_jogador', 'nome_time_jogador']]
#print(time_cres_salario_decres)
#qnt_jogador_por_time = df['nome_time_jogador'].value_counts()
#print("Quantidade de jogadores por time")
#print(qnt_jogador_por_time)
#media_salario_por_time = df.groupby('nome_time_jogador')['salario_do_jogador'].mean()
#print("Média salarial por time")
#print(media_salario_por_time)