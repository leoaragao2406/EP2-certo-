import disthaversine
import estanalista
import normaliza
import ordenando
import sorteialetra
import sorteiapais
import basepaises
RED   = "\033[0;31m"
YELLOW   = "\033[0;33m"   
BLUE  = "\033[0;34m"
CYAN  = "\033[0;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

i=0
normalizado = normaliza.normaliza(basepaises.DADOS)
chances = 20
tentativas = []
acab=False
palp=False
listadica=[]
listadica1=[]
listadica2=[]
while acab==False:
    paisescolhido = sorteiapais.sorteia_pais(normalizado)
    palp=False
    chances = 20
    tentativas = []
    listadica=[]
    listadica1=[]
    listadica2=[]
    i=0
    while palp==False:
        if chances==0:
            print('Você perdeu! O país escolhido era:{}'.format(paisescolhido))
            palp=True
            break
        else:
            chute = input('qual o seu palpite')
        if chute in normalizado:
            esta=estanalista.esta_na_lista(chute,tentativas)
            if chute == paisescolhido:
                print(GREEN+'parabens! você acertou!'+RESET)
                palp=True
            elif esta==True:
                print('Você ja tentou esse país')
            else:
                dist = disthaversine.haversine(basepaises.EARTH_RADIUS, normalizado[paisescolhido]['geo']['latitude'],normalizado[paisescolhido]['geo']['longitude'], normalizado[chute]['geo']['latitude'], normalizado[chute]['geo']['longitude'])
                parada=ordenando.adiciona_em_ordem(chute,dist,tentativas)
                for i in range(len(parada)):
                    if parada[i][1]<3500:
                        print(RED+"{},{:.3f} km".format(parada[i][0],parada[i][1])+RESET)
                    elif parada[i][1]<8000:
                        print(YELLOW+"{},{:.3f} km".format(parada[i][0],parada[i][1])+RESET)
                    elif parada[i][1]<12000:
                        print(CYAN+"{},{:.3f} km".format(parada[i][0],parada[i][1])+RESET)
                    else:
                        print(BLUE+"{},{:.3f} km".format(parada[i][0],parada[i][1])+RESET)


                chances -= 1
    
        elif chute =='dica':
            print('escolha uma dica:')
            print('1: Cores da bandeira do país - custa 4 tentativas ')
            print('2: Letras de sua capital - custa 3 tentativas')
            print('3: População - custa 6 tentativas')
            print('4: Área - custa 5 tentativas')
            print('5: Continente - custa 7 tentativas')
            print('0: Sem dica')
            numdica=input('Escolha sua opção [0|1|2|3|4|5]: ')
        
            if numdica == '1' and chances>4:
                for info,numb in normalizado[paisescolhido].items():
                    if info == 'bandeira':
                        for cor,quantidade in numb.items():
                            if quantidade>0 and cor not in listadica1:
                                listadica1.append(cor)
                                print(cor)
                                chances-=4
                                break
            elif numdica== '2' and chances>3:
                letradica=sorteialetra.sorteia_letra(normalizado[paisescolhido]['capital'],listadica2)
                if len(letradica)<1:
                    print('dica não disponivel')
                else:
                    chances-=3
                    listadica2.append(letradica)
                    print(letradica)
            elif numdica=='3' and chances>6:
                if 3 in listadica:
                    print('Dica indisponivel')
                else:
                    for info,numb in normalizado[paisescolhido].items():
                        if info == 'populacao':
                            print('{}: {} habitantes'.format(info,numb))
                            listadica.append(3)
                            chances-=6
            elif numdica=='4' and chances>5:
                if 4 in listadica:
                    print('Dica indisponivel')
                else:
                    for info,numb in normalizado[paisescolhido].items():
                        if info == 'area':
                            print('{}: {} km2'.format(info,numb))
                            listadica.append(4)
                            chances-=5
            elif numdica=='5' and chances>7:
                if 5 in listadica:
                    print('Dica indisponivel')
                else:
                    for info,numb in normalizado[paisescolhido].items():
                        if info == 'continente':
                            print('{}: {}'.format(info,numb))
                            listadica.append(5)
                            chances-=7
            else:
                print('Dica inválida/indisponivel')
        

                            
        else:
            print('País inválido')
    novo=input('Você deseja jogar novamente?[s/n]')
    if novo == 'n':
        acab=True