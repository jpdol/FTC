import re


def verifica_autor(autor):
    padrao = re.search(r'^[a-zA-Z][[a-zA-Z0-9]*$', autor)
    if padrao:
        lista_numeros = re.findall(r'\d', autor)
        numeros = len(lista_numeros)
        letras = len(autor) - numeros
        return letras > numeros
    return False


def verifica_senha(senha):
    formato = re.search(r'^([0-9A-F]){2}\.[0-9A-F]{2}\.[0-9A-F]{2}\.[0-9A-F]{2}$', senha)
    bloco = ""
    flag = 0
    if formato:
        senha = senha + " "
        for i in range(len(senha)):
            if senha[i] == '.' or senha[i] == " ":
                padrao = re.search(r'^[0-9][A-F]$|^[A-F][0-9]$|^[0-9][0-9]$', bloco)

                if padrao:
                    if bloco[0] != bloco[1]:
                        flag += 1
                bloco = ""
            else:
                bloco = bloco + senha[i]
    if flag == 4:
        return True
    return False


def verifica_IP(IP):
    formato = re.search(r'^\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}$', IP)
    bloco = ""
    flag = 0
    if formato:
        IP = IP + " "
        for i in range(len(IP)):
            if (IP[i] == '.' or IP[i] == " "):
                if (bloco==""):
                    flag += 1
                else:
                    padrao = re.search(r'^[0-9]$|^[0-9][0-9]$|^1[0-9][0-9]$|^2[0-4][0-9]$|^25[0-5]$', bloco)
                    if padrao:
                        flag += 1
                bloco = ""
            else:
                bloco = bloco + IP[i]

    if flag == 4:
        return True
    return False


def verifica_email(email):
    padrao = re.search(r'^[a-z][^@]*@[^@]*\.+[^@]*$', email)
    if padrao:
        return True
    return False


def verifica_transacao(transacao):
    padrao = re.search(r'(\bpull\b)|(\bpush\b)|(\bstash\b)|(\bfork\b)|(\bpop\b)', transacao)
    if (padrao):
        return True
    return False


def verifica_hash(hash):
    if len(hash) == 32:
        padrao = re.search(r'^[0-9a-f]{32}$', hash)
        if padrao:
            return True
    return False


def verifica_repositorio(repositorio):
    padrao = re.search(r'^([a-z0-9]*[_]?[a-z0-9]*)*$', repositorio)
    if padrao:
        return True
    return False


def verifica_entrada(entrada):
    bloco = ""
    entrada_formatada = []
    for i in (entrada):
        if (i != " "):
            bloco = bloco + i
        else:
            entrada_formatada.append(bloco)
            bloco = ""

    entrada_formatada.append(bloco)

    # entrada_formatada[0] == Autor
    # entrada_formatada[1] == Senha
    # entrada_formatada[2] == IP do Autor
    # entrada_formatada[3] == Email do Autor
    # entrada_formatada[4] == Tipo da Transação
    # entrada_formatada[5] == Repositório
    # entrada_formatada[6] == Hash

    if len(entrada_formatada) == 7:
        if verifica_autor(entrada_formatada[0]):
            if verifica_senha(entrada_formatada[1]):
                if verifica_IP(entrada_formatada[2]):
                    if verifica_email(entrada_formatada[3]):
                        if verifica_transacao(entrada_formatada[4]):
                            if verifica_repositorio(entrada_formatada[5]):
                                if verifica_hash(entrada_formatada[6]):
                                    return True

    return False


if __name__=='__main__':

    try:
        entrada = input()

        if verifica_entrada(entrada):
            print('True')
        else:
            print('False')

    except:
        print('False')