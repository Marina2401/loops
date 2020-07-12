def main():
    n = int(input('Введите число '))
    for i in range(n):
        for j in range(i+1):
            print(i+1, end='')
        print()
        for j in range(i+1):
            print(0, end='')
        print()


if __name__ == '__main__':
    main()