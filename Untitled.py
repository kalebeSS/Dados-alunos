#!/usr/bin/env python
# coding: utf-8



import pandas as pd


df_aluno = pd.read_csv('Base de Alunos9.csv', sep = ';')
df_dengue = pd.read_csv('Base de Dengue9.csv', sep = ';')


df_dengue.head()


df_aluno.head()


#colocar numa lista os nomes apenas que tiveram dengue

nomes_dengue = df_dengue["Nome"].tolist()
nomes_dengue


#filtrar os alunos que não tiveram dengue

alunos_frequentaram_escola = df_aluno[~df_aluno["Nome"].isin(nomes_dengue)]
alunos_frequentaram_escola


# Selecionar o id, nome, Data para disposição

informacoes_alunos = alunos_frequentaram_escola[["ID", "Nome", "Data de Nascimento"]]
informacoes_alunos

