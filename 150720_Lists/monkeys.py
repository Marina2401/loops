#Требуется посчитать обезьян по одной
def monkey_count(n):
    a = []
    for k in range(1, n+1):
        a.append(k)
    return a

def index(n):
    a = []
    for i in range(0, n):
        a.append(i)
    return a

def main():
    n = int(input('Введите число n '))
    m = monkey_count(n)
    print(m)
    j = index(n)
    print
main()