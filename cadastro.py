import json


def login_apresentação():
    print('Pagina de login')
    print('responda com numeros')
    try:
        user = int(input('\n1- ja possui conta  \n2- deseja criar uma conta  \n3- para fechar o sistema\n'))
    except:
        print('digite numeros')
        return None

    return user


def usuario_existente():
    
    
    login = input('nome do usuario - ')
    senha = input('senha do usuario - ')
    
    return [login,senha]

def novo_usuario():
    
    login = input('crie um nome de usuario - ')
    senha = input('crie uma senha de usuario - ')
    
    return [login,senha]
   
   

def verificar_login(infor):
    import json

    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)

    for x in range(len(dados)):
        if dados[x]['nome'] == infor[0] and dados[x]['senha'] == infor[1]:
           print('entrando...')
           return x
    print("usuario nao existe")
    return None
            
     
    


def guardar_login(cadastro):
    dic = {
        'nome': cadastro[0],
        'senha': cadastro[1],
        'log': 0 ,
        'historico':[]
    }

    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
    except:
        dados = []

    dados.append(dic)

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print('cadastrado com sucesso')






