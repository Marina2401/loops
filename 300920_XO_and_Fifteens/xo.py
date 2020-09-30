
N = 3
M = 3

def create():
    a = []
    for i in range(N):
        b = []
        for j in range(M):
            b.append('.')
        a.append(b)
    return a

def print_game(a):
    for i in range(N):
        for j in range(M):
            print(a[i][j], end=' ')
        print()
    print()

def check_win(a, current_player):
    return True

def check_draw(a):
    return True

def funk(a):

    while True:
        row = int(input('Введите номер строки '))
        column = int(input('Введите номер столбца '))
        if 1 <= row <= N and 1 <= column <= M and a[row-1][column-1] == '.':
            break
        else:
            print('Некорректный ход, введите заново')
    return row-1, column-1


def main():
    a = create()
    print_game(a)
    current_player = "X"
    while True:
        print(f'Ход {current_player}: ')
        row, column = funk(a)
        a[row][column] = current_player
        print_game(a)
        if check_win(a, current_player) == True:
            print(f'{current_player} выиграл')
            break
        elif check_draw(a):
            print('ничья')
            break
        else:
            if current_player == 'X':
                current_player = '0'
            else:
                current_player = 'X'



