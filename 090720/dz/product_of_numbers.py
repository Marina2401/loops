#Требуется выполнить произведение всех четных чисел, меньших заданного числа.
def even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def main():
    n = int(input('Введите число n '))
    a = 1
    for i in range(1, n+1):
        if even(i):
            a = a * i
    print(a)
main()