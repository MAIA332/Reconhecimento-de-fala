
version = "1.4.0"

def intro():

    msg = "Assistente - version {}/ by: Lukas Maia".format(version)
    print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg))

lista_erros = ["Não entendi nada","desculpe não entendi","repita novamente por favor"]

conversas = {

    "Olá": "oi tudo bem? ",
    "Sim e você": "Estou bem e você",

}

comandos = {
    
    "desligar" : "desligando",
    "Reiniciar": "Reiniciando"

} 


def verifica_nome(user_name):
    if user_name.startwith("Meu nome é"):
        user_name = user_name.replace("Meu nome é", "")
    elif user_name.startwith(" Eu me chamo"):
        user_name = user_name.replace("Eu me chamo", "")
    elif user_name.startwith("Eu sou o"):
        user_name = user_name.replace("Eu sou o", "")
    elif user_name.startwith("Eu sou a"):
        user_name = user_name.replace("Eu sou a", "")

    return user_name

def verifica_nome_existe(nome):
    dados = open("dados/nomes.txt", "r")
    nome_list = dados.readlines()

    if not nome_list:
        vazio = open("dados/nomes.txt", "r")
        conteudo = vazio.readlines()
        conteudo.append("{}".format(nome))
        vazio = vazio = dados = open("dados/nomes.txt", "w")
        vazio.writelines(conteudo)
        vazio.close()

        return "Olá {}, prazer em te conhecer!".format(nome)
    
    for linha in nome_list:
        if linha == nome:
            return "Olá {} ".format(nome)

    vazio = open("dados/nomes.txt", "r")
    conteudo = vazio.readlines()
    conteudo.append("\n{}".format(nome))
    vazio = vazio = dados = open("dados/nomes.txt", "w")
    vazio.writelines(conteudo)
    vazio.close()

    return "Oi {}".format(nome)


def name_list():

    try:
        nomes = open("dados/nomes.txt", "r")
        nomes.close()

        
    except FileNotFoundError:
        nomes = open("dados/nomes.txt", "w")
        nomes.close()

