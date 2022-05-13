import random
def sorteia_letra(x,lista):
    y=['.', ',', '-', ';', ' ']
    nlista=[]
    for carac in lista:
        carac=carac.lower()
    for letra in x:
        letra=letra.lower()
        if letra in lista or letra in y:
            lista=lista
        else:
            nlista.append(letra)
    if len(nlista)>0:
        resp=random.choice(nlista)
        return resp
    else:
        return nlista