#вывести числа от 1 до n по горизонтали и вертикали в порядке увеличения количества и самих чисел
def main():
    n = int(input('n = '))

    for j in range(n):
        for i in range(j+1):
            print(i+1, end=' ')
        print()


if __name__ == '__main__':
    main()