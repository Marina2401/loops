import random

def create_game():
    a = list(range(1, 16))
    random.shuffle(a)
    a.append(None)
    b = []
    k = 0
    for i in range(4):
        c = []
        for j in range(4):
            c.append(a[k])
            k += 1
        b.append(c)
    return b

def print_game(a):
    for row in a:
        for elem in row:
            if elem is None:
                print(' ', end='\t')
            else:
                print(elem, end='\t')
        print()
    print()



def main():
    b = create_game()
    print_game(b)
    row = 3
    column = 3
    while True:
        dir = int(input('1. Верх   2. Вниз  3. Влево   4. Вправо'))
        if dir == 1:



main()
