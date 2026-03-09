import pandas as pd

def get_disciplinas(df):
    # corrido é um dicionario {'disciplina':, NULL}
    return dict.fromkeys(df['Disciplina'].unique())


def set_nome_breve(dict,path):
    with open(path, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
        
        # lista de chaves atuais
        chaves = list(dict.keys())
        
        # chaves e linhas simultaneamente
        for i in range(len(chaves)):
            chave_atual = chaves[i]
            nome_breve = linhas[i].strip()
            dict[chave_atual] = nome_breve