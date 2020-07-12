def main():
    n = int(input('n = '))
    for j in range(n):
        if j % 2 == 0:
            print(7*'*', end='')
        else:
            print((4)*'*', end='')
        print()


if __name__ == '__main__':
    main()