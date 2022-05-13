def adiciona_em_ordem(pais,dist,lista):
    nova_lista=[]
    lista_nomes=[]
    lista_distancias=[]
    adicionar=[pais,dist]
    if lista==nova_lista:
        lista.append(adicionar)
        return lista
    for paises in lista:
        lista_nomes.append(paises[0])
        lista_distancias.append(paises[1])
    if pais in lista_nomes:
        return lista
    
    if pais not in lista_nomes:
        for paises in lista:
            distancia=paises[1]
            if dist>distancia:
                nova_lista.append(paises)
            elif adicionar in nova_lista:
                nova_lista.append(paises)
            elif dist<distancia:
                nova_lista.append(adicionar)
                nova_lista.append(paises)
        if adicionar not in nova_lista:
            nova_lista.append(adicionar)
        return nova_lista