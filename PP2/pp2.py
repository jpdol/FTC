def matriz_transposta(matriz):
    transposta=[]
    for i in range (len(matriz[0])):
        linha=[]
        for j in range (len(matriz)):
            linha.append(matriz[j][i])
        transposta.append(linha)
    return transposta

def multiplica_matrizes(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    if num_colunas_A==num_linhas_B:
        produto = []
        for linha in range (num_linhas_A):
            produto.append([])
            for coluna in range (num_colunas_B):
                produto[linha].append(0)
                for k in range(num_colunas_A):
                    produto[linha][coluna]+=A[linha][k]*B[k][coluna]
        return produto





entrada = input()
j=0
automato = dict()
while (entrada[j]!='}'):
    chave = ""
    while (entrada[j]!= ':' and entrada[j]!= '}'):
        if entrada[j]!= ' ' and entrada[j]!= '{' :
            chave = chave + entrada[j]
        j+=1
    if chave== '"estados"' or chave == '"inicial"':
        valor=''
        j+=1
        while (entrada[j]!=',' and entrada[j]!='}'):
            if entrada[j] != ' ':
                valor = valor + entrada[j]
            j+=1
        if chave == '"estados"':
            automato["estados"] = int(valor)
        else:
            automato["inicial"] = int(valor)

    elif chave=='"final"':
        j+=1
        str_estados =''
        while(entrada[j]!= ']' and entrada != '}'):
            if entrada[j]!=' ':
                str_estados = str_estados + entrada[j]
            j+=1
        if entrada[j]==']':
            str_estados = str_estados + entrada[j]
            j+=1
        while(entrada==' '):
            j+=1
        lista_estados=[]
        i=0
        estado=''
        while (str_estados[i]!=']'):
            if str_estados[i]!='[' and str_estados!=" ":
                if str_estados[i]!=",":
                    estado= estado+str_estados[i]
                else:
                    lista_estados.append(int(estado))
                    estado=''
            i += 1
        if estado!='':    
            lista_estados.append(int(estado))
        automato["final"]=lista_estados

    elif chave== '"delta"':
        j += 1
        str_delta = ''
        while entrada[j] != '}':
            if entrada[j] != ' ':
                str_delta = str_delta + entrada[j]
            j += 1

        while entrada == ' ':
            j += 1

        delta = []
        k = 0
        for i in range(automato["estados"]):
            linha=[]
            transicao=''
            while(str_delta[k]!="]"):
                if str_delta[k]!='[' and str_delta[k]!=',':
                    transicao= transicao + str_delta[k]
                elif(str_delta[k]==','):
                    linha.append(int(transicao))
                    transicao=''
                k+=1
            if transicao != '':
                linha.append(int(transicao))
            delta.append(linha)
            k+=2 # k vai para a posicao de indexacao depois do próximo '[' ou entao chega em '}'
        automato["delta"] = delta
    if entrada[j]!= '}':
        j+=1


pi= []
for i in range (automato["estados"]):
    if i==automato["inicial"]:
        pi.append([1])
    else:
        pi.append([0])

eta=[]
for i in range(automato["estados"]):
    eta.append([0])

for i in range (len(automato["final"])):
    eta[automato["final"][i]]=[1]

x_a=[]
x_b=[]
for i in range(automato["estados"]):
    linha=[]
    for j in range(automato["estados"]):
        linha.append(0)
    x_a.append(linha)

for i in range(automato["estados"]):
    linha=[]
    for j in range(automato["estados"]):
        linha.append(0)
    x_b.append(linha)

for i in range (automato["estados"]):
    x_a[i][automato["delta"][i][0]] = 1

for i in range (automato["estados"]):
    x_b[i][automato["delta"][i][1]] = 1


num_testes=int(input())

for i in range(num_testes):
    teste= str(input())
    if (teste[0] == 'a' ):
        x_w = x_a.copy()
    if (teste[0] == 'b'):
        x_w = x_b.copy()
   

    j=1 
    while j< len(teste):
        if teste[j]=='a':
            x_w=multiplica_matrizes(x_w,x_a)
        elif teste[j]=='b':
            x_w=multiplica_matrizes(x_w,x_b)
        j+=1
     
    if (multiplica_matrizes(multiplica_matrizes((matriz_transposta(pi)),x_w), eta))==[[1]]:
        print("ACEITA")
    else:
        print("REJEITA")
