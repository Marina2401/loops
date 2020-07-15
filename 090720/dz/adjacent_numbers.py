#Требуется проверить прыгающее число: если все смежные цифры в нём отличаются на 1, то да.
def adj(n):
    while n // 10 > 0:
        a = n % 10
        n = n // 10
        b = n % 10
        if b != (a + 1) and b != (a - 1):
            return False
    return True
def main():
    n = int(input('Введите n '))
    check = adj(n)
    if check == True:
        print('Yes')
    else:
        print('No')

main()