#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df_aluno = pd.read_csv('Base de Alunos9.csv', sep = ';')
df_dengue = pd.read_csv('Base de Dengue9.csv', sep = ';')


# In[4]:


df_dengue.head()


# In[5]:


df_aluno.head()


# In[6]:


#colocar numa lista os nomes apenas que tiveram dengue

nomes_dengue = df_dengue["Nome"].tolist()
nomes_dengue


# In[7]:


#filtrar os alunos que não tiveram dengue

alunos_frequentaram_escola = df_aluno[~df_aluno["Nome"].isin(nomes_dengue)]
alunos_frequentaram_escola


# In[8]:


# Selecionar o id, nome, Data para disposição

informacoes_alunos = alunos_frequentaram_escola[["ID", "Nome", "Data de Nascimento"]]
informacoes_alunos

