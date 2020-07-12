# Дано число. Следует выяснить, есть ли в нём повторяющиеся цифры.

def prov(n):
    while n != 0:
        a = n % 10
        n = n//10
        check = povt(n, a)
        if check == True:
            return True
    return False

def povt(n, a):
    while n != 0:
        b = n % 10
        if b == a:
            return True
        n = n//10
    return False



def main():
    n = int(input('Введите число '))
    k = prov(n)
    if k == True:
        print('Есть повторяющиеся цифры')
    else:
        print('Нет повторяющихся цифр')
main()
