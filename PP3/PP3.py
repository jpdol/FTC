def q0(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        cabeca1+=1
        fita3[cabeca3] = 'I'
        return q0(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== 'I'):
        cabeca1+=1
        return q0(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== '#' and fita2[cabeca2]== ' ' and fita3[cabeca3]== 'I'):
        fita1[cabeca1]=' '
        cabeca1+=1
        return q1(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"


def q1(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== 'I'):
        fita2[cabeca2]= 'I'
        cabeca2+=1
        fita1[cabeca1] = ' '
        cabeca1+=1
        fita3[cabeca3] = ' '
        return q1(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        fita2[cabeca2]= 'I'
        cabeca2+=1
        fita1[cabeca1] = ' '
        cabeca1+=1
        return q1(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== ' ' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        return q2(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q2(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== ' ' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        cabeca1-=1
        return q2(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif(fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        cabeca1-=1
        cabeca2-=1
        return q3(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q3(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]== ' '):
        cabeca1-=1
        return q3(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== ' ' and fita2[cabeca2]== 'I' and fita3[cabeca3]== ' '):
        cabeca1+=1
        cabeca2-=1
        return q4(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q4(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if(fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I'):
        cabeca2-=1
        return q4(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' '):
        cabeca2+=1
        return q5(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q5(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]== ' '):
        fita1[cabeca1] = ' '
        cabeca1+=1
        cabeca2+=1
        return q6(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q6(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]== ' '):
           fita1[cabeca1]= ' '
           cabeca1+=1
           cabeca2+=1
           return q6(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]=='I'):
        cabeca1+=1
        cabeca2+=1
        return q6(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        cabeca2-=1
        return q9(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== 'I'):
        cabeca2-=1
        return q9(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== ' ' and fita2[cabeca2]== 'I' and fita3[cabeca3]== 'I'):
        fita2[cabeca2] = ' '
        cabeca2 -= 1
        fita3[cabeca3] = ' '
        cabeca3 += 1
        return q7(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q7(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== ' ' and fita2[cabeca2]== 'I' and fita3[cabeca3]== ' '):
        cabeca2-=1
        fita3[cabeca3]= 'I'
        cabeca3+=1
        return  q7(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== ' ' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        return  q8(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def  q8(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    return "ACEITA"

def q9(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]== ' '):
        cabeca2-=1
        return q9(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]== 'I'):
        cabeca2-=1
        return q9(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== ' '):
        cabeca2+=1
        fita3[cabeca3]= 'I'
        return q10(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    elif (fita1[cabeca1]== 'I' and fita2[cabeca2]== ' ' and fita3[cabeca3]== 'I'):
        cabeca2+=1
        return q10(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"

def q10(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3):
    if (fita1[cabeca1]== 'I' and fita2[cabeca2]== 'I' and fita3[cabeca3]== 'I'):
        fita1[cabeca1]= ' '
        cabeca1+=1
        cabeca2+=1
        return q6(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
    else:
        return "REJEITA"




entrada = str(input())
fita1=[' ']
for i in range (len(entrada)):
    fita1.append(entrada[i])
fita1.append(' ')
fita2=[]
fita3=[]
for i in range (len(fita1)):
    fita2.append(' ')
    fita3.append(' ')

cabeca1, cabeca2, cabeca3 = 1, 1, 1

saida = q0(fita1, cabeca1, fita2, cabeca2, fita3, cabeca3)
mod = ""
if saida == "ACEITA":
    for i in range (len(fita3)):
        if (fita3[i]=='I'):
            mod+= fita3[i]
    entrada+='='
    entrada+=mod
    print(entrada, saida)
else:
    entrada += '='
    entrada += mod
    entrada+= saida
    saida = entrada
    print (saida)