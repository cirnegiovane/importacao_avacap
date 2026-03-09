# importacao

import pandas as pd
from utils import get_disciplinas, set_nome_breve
geral = pd.read_csv('geral.csv',skiprows=1)
atual = pd.read_csv('base.csv')

#INSTITUTO = 'FIS'
INSTITUTO = str(input('Digite exatamente o codigo do instituto em questão (ex.: FIS, IEFD): '))
SENHA_PADRAO = '123'
# filtragem


geral_filtrada = geral[geral['Instituto'] == INSTITUTO].reset_index()

# reconhecendo materias 

dict_nome_breve = get_disciplinas(geral_filtrada)
print(f'Faça um txt "nome_breve_em_ordem_{INSTITUTO}.txt" nessa ordem:\n')
for disc in dict_nome_breve.keys():
    print(disc)

# pegando nome breve de nome_breve_em_ordem_{INSTITUTO}.txt 

se = str(input((f'\nJa salvou um arquivo nome_breve_em_ordem_{INSTITUTO}.txt ?? [s/n]\n')))
while se != 's':
    print('TENTA DNV')
    se = str(input((f'\nJa salvou um arquivo nome_breve_em_ordem_{INSTITUTO}.txt ?? [s/n]\n')))


path = f'nome_breve_em_ordem_{INSTITUTO}.txt'
set_nome_breve(dict_nome_breve, path)

# ------username,password,email,firstname,lastname,course1,role1 ---------

# matricula

atual['username'] = geral_filtrada['Matrícula']

# senha

atual['password'] = SENHA_PADRAO

# email

atual['email'] = geral_filtrada['E-mail']


# nomes

atual['firstname'] = geral_filtrada['Nome'].str.split(' ').str[0]
atual['lastname'] = geral_filtrada['Nome'].str.split(' ',n=1).str[1]

# disciplina

coluna_isolada = geral_filtrada['Disciplina'].map(dict_nome_breve)
atual['course1'] = coluna_isolada

# role
atual['role1'] = 5 # 5 para alunos


# salva_csv
#atual.drop(atual.columns[0], axis=1, inplace=True)
atual.to_csv(F'preparacao/{INSTITUTO}.csv',index=False)



# debug

print(dict_nome_breve)
print(len(dict_nome_breve))
print()

#geral_filtrado = geral['']