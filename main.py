import random

#Variables
#-----------------------------
isPlaying = True #Variable bool para ver si estamos jugando
isPlayingMatch = True #Variable bool para ver si esta en una partida
isHavingTurn = True #Variable bool para ver si estas en tu turno
dealerPasado = False #Variable bool que dice si el dealer se paso

barajaCartas = [11, 11, 11, 11, 
                10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                9, 9, 9, 9,
                8, 8, 8, 8,
                7, 7, 7, 7,
                6, 6, 6, 6,
                5, 5, 5, 5,
                4, 4, 4, 4,
                3, 3, 3, 3,
                2, 2, 2, 2,
                1, 1, 1, 1] #Baraja con todas las cartas de un set de cartas

deck = [] #Lista que contiene tu deck
deckDealer = [] #Lista que contiene el deck del dealer

puntos = 0 #Variable que almacena los puntos del jugador
puntosDealer = 0 #Variable que almacena los puntos del dealer

#------------------------------

def MezclarCartas(barajaCartas):
    #Añadiendo lista
    #barajaCartas = barajaCartas TEMPORAL --------------------
    barajaMezclada = []

    #Usando algoritmo Fisher-Yates para mezclar
    #Mientras que la baraja de cartas tenga mas que 0 cartas
    while len(barajaCartas) > 0:

        #Se escoge un numero random entre 0 y el tamaño de la lista original
        numeroRandom = random.randint(0, len(barajaCartas) - 1)

        #El valor en la posicion escogida, se quita de la lista original y se coloca en la nueva
        barajaMezclada.append(barajaCartas[numeroRandom])
        barajaCartas.remove(barajaCartas[numeroRandom])
    
    return barajaMezclada

#Metodo que da una carta de una baraja a otra
def DarCarta(Baraja1, Baraja2):
    #Tomar primera carta de la baraja y ponerla en un deck
    Baraja1.append(Baraja2[0])
    Baraja2.remove(Baraja2[0])
    return Baraja1

#Metodo para imprimir lista
def ImprimirCartas(Cartas):
    for carta in Cartas:
        print(carta)

#Metodo que evalua las cartas y calcula cuantos puntos tienes
def EvaluarPuntos(deck):
    puntos = 0
    for carta in deck:
        puntos += carta
    return puntos

#Codigo del dealer
def Dealer(deckDealer, baraja, puntosDealer, dealerPasado):
    dealerPasado = False
    puntosDealer = EvaluarPuntos(deckDealer)

    print(f"Cartas del dealer: {deckDealer}")

    #Si el dealer tiene 15 o menos puntos, pedira una carta
    while puntosDealer <= 15:

        DarCarta(deckDealer, baraja)
        puntosDealer = EvaluarPuntos(deckDealer)

        print("El dealer coje una carta")
        print(f"El dealer tiene {puntosDealer} puntos")

    #Si el dealer se pasa
    if puntosDealer > 21:

        dealerPasado = True
        print(f"El dealer se paso, con {puntosDealer} puntos")
    else:

        print(f"El dealer se queda, con {puntosDealer} puntos")
    
#---------------------------------
#Jugar Blackjack
while isPlaying == True:

    #Preguntar si quieres jugar
    wantsToPlay = input("Quieres jugar un juego de BlackJack? Y/N")

    if wantsToPlay.upper() == "Y":
        isPlaying = True
        print("Intenta ganar entonces")

    elif wantsToPlay.upper() == "N":
        isPlaying = False
        print(":(")
        break

    else:
        isPlaying = True
        print("Papa que me estas diciendo, ponte a jugar carajo")
    
    #Si el deck tiene mas de una carta antes de empezar el juego, tomamos las cartas del deck y las ponemos en la baraja
    if len(deck) > 0:
        for i in range(0, len(deck)):
            barajaCartas.append(deck[0])
            deck.remove(deck[0])

    if len(deckDealer) > 0:
        for i in range(0, len(deckDealer)):
            barajaCartas.append(deckDealer[0])
            deckDealer.remove(deckDealer[0])
    
    #Mezclar la baraja principal
    barajaCartas = MezclarCartas(barajaCartas)

    #Dar dos cartas al deck del jugador
    DarCarta(deck, barajaCartas)
    DarCarta(deck, barajaCartas)
    isPlayingMatch = True

    #Dar dos cartas al dealer
    DarCarta(deckDealer, barajaCartas)
    DarCarta(deckDealer, barajaCartas)

    while isPlayingMatch == True:

        isHavingTurn = True

        #Ver cuanto valen las cartas
        puntos = EvaluarPuntos(deck)

        #Mirar a ver si hay un blackjack
        if puntos == 21:
            print("BlackJack!")
            isPlayingMatch = False
            isHavingTurn = False

        while isHavingTurn == True:

            puntos = EvaluarPuntos(deck)

            #Imprimir las cartes que tenemos en el deck
            print("Tus cartas son:")
            ImprimirCartas(deck)

            #Mirar para ver si hay un blackjack o si uno se paso de puntos
            if puntos == 21:
                print("BlackJack!")
                isPlayingMatch = False
                isHavingTurn = False

                #Dealer juega
                Dealer(deckDealer, barajaCartas, puntosDealer, dealerPasado)
                break
            
            elif puntos > 21:
                print(f"Te pasaste, con {puntos} puntos")

                isPlayingMatch = False
                isHavingTurn = False

                #Dealer juega
                Dealer(deckDealer, barajaCartas, puntosDealer, dealerPasado)
                break

            #Interaccion con el jugador
            print("S para Quedarse/Stand")
            print("P para Pedir")
            choice = input()
            choice = choice.upper()

            #Si uno no pide cartas o pide
            if choice == "S":
                print(f"Conseguiste un total de {puntos} puntos")
                isHavingTurn = False
                isPlayingMatch = False

                #Dealer juega
                Dealer(deckDealer, barajaCartas, puntosDealer, dealerPasado)

            #Si vas a coger una carta
            elif choice == "P":
                DarCarta(deck, barajaCartas)

