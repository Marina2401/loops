def main():
    n = int(input('Введите число '))
    for j in range(n, n-5, -1):
        for i in range(j-3):
            print(j, end='')
        print()

if __name__ == '__main__':
    main()