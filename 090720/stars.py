
def main():
    n = int(input('n = '))

    for j in range(n):
        for i in range(j+1):
            print('*', end='')
        print()


if __name__ == '__main__':
    main()