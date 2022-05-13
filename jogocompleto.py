import disthaversine
import estanalista
import normaliza
import ordenando
import sorteialetra
import sorteiapais
import basepaises

i=0
normalizado = normaliza.normaliza(basepaises.DADOS)
chances = 20
tentativas = []
paisescolhido = sorteiapais.sorteia_pais(normalizado)
while chances > 0:
    chute = input('qual o seu palpite')
    if chute in normalizado:
        if chute == paisescolhido:
            print('parabens! você acertou!')
            chances=0
        else:
            dist = disthaversine.haversine(basepaises.EARTH_RADIUS, normalizado[paisescolhido]['geo']['latitude'],normalizado[paisescolhido]['geo']['longitude'], normalizado[chute]['geo']['latitude'], normalizado[chute]['geo']['longitude'])
            dist=('{:.3f}'.format(dist))
            tentativas.append(ordenando.adiciona_em_ordem(chute,dist,tentativas))
            for i in range(len(tentativas)-2):
                print(tentativas[i])
                i+=1
            chances -= 1
    if chute =='dica':
        numdica=input('escolha uma dica: /n 1:Cores da bandeira do país /n 2:Letras de sua capital /n 3:População /n 4:Área /n 5:Continente /n Escolha sua opção [0|1|2|3|4|5]: ')
        if numdica == 1:
            chances=chances
