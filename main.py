from game import inLine

def choose_col(game):
    try:
        col_input = int(input(f'Jugador {game.player} ingrese un número del 0 al 6: '))
        try:
            game.throw_coin(col_input)
            inLine.print_tablero(game)
        except TypeError:
            print('Columna llena')
    except ValueError:
        print('El valor ingresado no es correcto')
    except IndexError:
        print('Por favor, seleccione una columna del 0 al 6')    


if __name__ == '__main__':
    game = inLine()
    inLine.print_tablero(game)
    while True:
        choose_col(game)
        if game.check_winner() == True:
            print(f'El juego ha terminado. Felicitaciones jugador {game.winner}, has ganado')
            break
 