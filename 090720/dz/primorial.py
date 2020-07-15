#Требуется представить число в виде произведения простых множителей.
def simple(c):
    i = 2
    while i < c:
        if c % i == 0:
            return False
        i = i+1
    return True

def main():
    n = int(input('Введите n '))
    for j in range(2, n+1):
        while n % j == 0 and simple(j) == True:
            if n//j == 1:
                print(j)
            else:
                print(j, end='*')
            n = n//j
main()