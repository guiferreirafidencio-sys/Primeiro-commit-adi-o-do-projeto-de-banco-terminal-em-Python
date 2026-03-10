import json
from cadastro import *
from datetime import datetime
import os
import time
with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)

def hub(indice):
    print(f'seja bem vindo {dados[indice]['nome']}')
    if dados[indice]['log'] == 0:     
        dados[indice]['saldo'] = 1000
        print(f'Voce ganhou R$:{dados[indice]['saldo']}')
        dados[indice]['log'] += 1 
    with open("dados.json", "w") as arq:
     json.dump(dados, arq, indent=4)
    print(f'seu saldo atual:{dados[indice]['saldo']}')
    return dados[indice]['saldo']


def ver_saldo(indice):
    print(f"R${dados[indice]['saldo']}")
    return

def pedir_user():   
    print('escreva nome do user que voce deseja transeferir')
    user = input('digite aqui - ')
    for x in range(len(dados)):
        if dados[x]['nome'] == user:
            carregar('Analisando')
            print('usuario encontrado')
            return x
def amarzenar_historico(indice, valor, user):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    dados[indice]['historico'].append(f'{data} - voce enviou R${valor} para {dados[user]['nome']}')

def amarzenar_historico_recebido (indice,valor,user):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    dados[indice]['historico'].append(f'{data} - voce recebeu R${valor} do {dados[user]['nome']}')
    
def exbir_historico(indice):
    if not dados[indice]['historico']:
        dados[indice]['historico'] = []
        print('voce nao possui historico ')
    
    for x  in dados[indice]['historico']:
        print(x)
def carregar_dados():
  with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
    return

def confirmação():
    print('deseja realmente enviar s/n')
    while True:    
        res = input('-')
        
        if res == 's':
            return True
            break    
            
        elif res == 'n':
            print('não foi enviado')
            break
            return False
        else:
            print('digite uma das opcões')

def  traço(valor):
    print('-'*valor)

def carregar(TEXT):
    for x in range(20):
        import time
        tex = '█'
        print(f'{TEXT}[{tex*x}{'-'*(20-x)}]%{x*5}', end='\r')
        time.sleep(0.01)
        
def enviado(indice,valor):
    dados[indice]['saldo'] += valor 
    return dados
def tirando_saldo(indice,valor):
    dados[indice]['saldo'] -= valor 
    return dados

def pedir_valor(indice):
    print('seu saldo R$ - ', dados[indice]['saldo'])
    while True:
        
        try:
            valor = int(input('digite o valor quer enviar'))
        except ValueError:
            print('digite apenas numeros')
            
        if valor > dados[indice]['saldo']:
            print('valor maior que seu saldo')
        else:
            return(valor)
            break

def limpar_terminal():
    os.system('cls')
    return
while True:    
    traço(25)
    resposta = login_apresentação()


    if resposta == 1:
        limpar_terminal()
        traço(25)
        infor = usuario_existente()
        traço(25)
        indice_do_user = verificar_login(infor)
        if isinstance(indice_do_user,int):
       
            carregar('ENTRANDO')
            hub( indice_do_user )
            
        while True:
            try:
                
                limpar_terminal()
                print('\n1 para ver historico \n2 para transferir dinheiro para alguem \n3 para ver  seu saldo  \n4 para sair\n')
                respota = int(input('-'))
                traço(25)
                if respota == 1:
                    exbir_historico(indice_do_user)
                    traço(25)
                    time.sleep(3)
                    print('voltando..')
                elif respota == 2:
                    user = pedir_user()
                    valor = pedir_valor(indice_do_user)
                    confirm = confirmação()
                    traço(25)
                    if confirm:
                        enviado(user , valor)
                        tirando_saldo(indice_do_user, valor)
                        carregar("enviando")
                        amarzenar_historico(indice_do_user, valor,user)
                        amarzenar_historico_recebido(user , valor,indice_do_user)
                        carregar_dados()
                        print('feita a trasnferencia voltando ao hub')
                        time.sleep(1.5)
                        traço(25)
                elif respota == 3:
                    ver_saldo(indice_do_user)
                    traço(25)
                    time.sleep(3)
                    print('voltando..')
                elif respota == 4:
                    print('saindo')
                    traço(25)
                    break
                else:
                    print('digite um dos numeros mostrado')
                    traço(25)
            except:
                print('digite um numero não caracter')
                traço(25)
            
                
                  
    elif resposta == 2:
        cadastro = novo_usuario()
        guardar_login(cadastro)

    elif resposta == 3:
        carregar('fechando sistema')
        break




          
          
          
        