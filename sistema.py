from random import choice
import string
from time import sleep

def Arquivo_Existe(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def Criar_Arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('houve um erro')


def Adicionar_Arquivo(nome_arquivo,senha):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('houve um erro')
    else:
        try:
            a.write(f'{senha}\n')
        except:
            print('erro ao inserir dado')
        else:
            print('adicionando senha...')
            sleep(1)
            print(f'{senha} adicionado com sucesso')


def Ler_Arquivo(nome_arquivo):
    global dado
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('houve algum erro')
    else:
        for linha in a:
            dado = linha
            print(f'{dado}')
    finally:
        a.close()


def Menu(lista):
    print('-' * 42)
    print('Gerador de senha'.center(42))
    print('-' * 42)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('-' * 42)
    escolha = int(input('opção: '))
    return escolha




def Gerador_Senha(valor):
    senha =''
    for c in range(1, 9):
        senha += choice(valor)
    return senha

arq = 'senhas.txt'
if not Arquivo_Existe(arq):
    Criar_Arquivo(arq)
while True:
    escolha = Menu(['ver senhas', 'gerar nova senha', 'sair do sistema'])
    if escolha == 2:
        print('-' * 42)
        Adicionar_Arquivo(arq, Gerador_Senha(string.ascii_letters + string.digits))
    elif escolha == 1:
        Ler_Arquivo(arq)
    elif escolha == 3:
        break
