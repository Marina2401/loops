#2. Одномерный массив из 10-и целых чисел заполнить с клавиатуры,
# определить сумму тех чисел, которые >5.

def sum5(a):
    sum = 0
    i = 0
    while i < 10:
        if a[i] > 5:
            sum = sum + a[i]
        i += 1
    return sum


def main():
    a = []
    for i in range(10):
        a.append(int(input('Введите элемент списка ')))
    print(a)
    s = sum5(a)
    if s == 0:
        print('нет элементов больше 5')
    else:
        print('Сумма элементов больше 5', s)

main()