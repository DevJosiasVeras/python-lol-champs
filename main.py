import requests, os
from bs4 import BeautifulSoup
from champs import *

def menu():
    print('''
    1. Ver nivel do jogador.
    2. Ver elo do jogador.
    3. Ver build campeão.
    4. Runas campeão.
    5. Sair.
    ''')
def nome_player(nome):
    try:
        url, headers = f'https://br.op.gg/summoners/br/{nome}', {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.65'}
        #Entrando no site
        r = requests.get(url, headers=headers)
        #Coletando informação 
        nivel = BeautifulSoup(r.content, 'html.parser').find('span', class_='level')
        #Printando informação
        print(f'O nivel do jogador é {nivel.text}')
    except AttributeError:
        print('Nome invalido !')
def elo_player(nome):
    try:
        url, headers = f'https://br.op.gg/summoners/br/{nome}', {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.65'}
        #Entrando no site
        r = requests.get(url, headers=headers)
        #Coletando informação 
        elo = BeautifulSoup(r.content, 'html.parser').find('div', class_='tier-rank')
        #Printando informação
        print(f'O Elo do jogador é {elo.text}')
    except (AttributeError):
        print('Jogador sem elo ou inexistente!')
def main(opc):
    
    if opc == 1:
            nome = input('Digite o nome do jogador -> ')
            nome_player(nome)
    elif opc == 2:
        nome = input('Digite o nome do jogador -> ')
        elo_player(nome)
    elif opc == 3:
        nome = input('Digite o nome do champ -> ')
        build.build_champ(nome)
    elif opc == 4:
        nome = input('Digite o nome do champ -> ')
        runas.runas_champ(nome)
    elif opc == 5:
        pass
    else:
        print('Digite uma opção valida !')
        return opc
while True:
    menu()
    try:
        opc = int(input('Escolha a opção -> '))
        main(opc)   
        if opc == 5:
            os.system('cls')            
            break
        else:
            os.system('pause')
            os.system('cls')
    except ValueError:
        print('Digite uma opção valida !')   
        os.system('pause')
        os.system('cls')