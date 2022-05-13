def esta_na_lista(pais,lista1):
    for lista in lista1:
        if pais == lista[0]:
            return True
    else:
        return False