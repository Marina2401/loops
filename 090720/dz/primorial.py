#Требуется представить число в виде произведения простых множителей.
n = int(input('Введите n '))
for i in range(1, n+1):
    if n % i == 0:
        a = n % i
        count = 0
        for j in range(1, a+1):
            if a % j == 0:
                count = count + 1
                if count <= 2:
                    print(a)