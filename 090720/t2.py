#Вывести числа меньше n в ряд по горизонтали и вертикали
def main():
    n = int(input('n = '))

    for j in range(n-1, -1, -1):
        for i in range(j+1):
            print(j-i, end=' ')
        print()


if __name__ == '__main__':
    main()