#Требуется найти первое простое число после заданного
def simple(a):
    i = 2
    while i <= a//2:
        if a % i == 0:
            return False
        i += 1
    return True

def main():
    n = int(input('Введите число, больше которого нужно найти первое простое '))
    s = n
    j = 0
    while j < 10:
        s = s + j
        if simple(s):
            print(s)
            break
        j += 1

main()
