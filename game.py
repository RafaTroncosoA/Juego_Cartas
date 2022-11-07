from classes.deck import Deck

victorias_pc=0
victorias_user = 0
while True:
    alfa = input('Desea empezar a jugar: Si/No:')
    if alfa=="Si":
        bicycle = Deck()
        carta_pc = bicycle.repartir_carta()
        print('La carta del PC es: ')
        carta_pc.card_info()
        valor_pc = carta_pc.point_val
        carta_usuario = bicycle.repartir_carta()
        print('La carta del usuario es: ')
        print(carta_usuario.card_info())
        valor_usr = carta_usuario.point_val

        if valor_pc == valor_usr:
            print('empate')
            print('Pinta PC: '+ carta_pc.suit)
            print('Pinta user: '+carta_usuario.suit)
            if carta_pc.valor_pinta() > carta_usuario.valor_pinta():
                print('Gana el PC')
            else:
                print('Gano el usuario')

        elif valor_pc > valor_usr:
            print('Gano el pc')
            victorias_pc+=1
            print('En total has ganado: {}, y la computadora: {}'.format(victorias_user,victorias_pc))
        
        else:
            print('Gana el usuario')
            victorias_user+=1
            print(f'En total has ganado: {victorias_user}, y la computadora: {victorias_pc}')

    else:
        print('Ok chaolin')
        break









