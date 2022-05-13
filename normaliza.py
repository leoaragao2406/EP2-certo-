def normaliza(x):
    nd={}
    for cont,pais in x.items():
        for pais,dados in pais.items():
            nd[pais]=dados
            nd[pais]['continente']=cont
    return nd
    
