import random

def sorteia_pais(x):
    lista=[]
    for pais in x.keys():
        lista.append(pais)
    pais=random.choice(lista)
    return pais