#посчитать кол-во дней с максим темпер
#посчитать кол-во дней с температурой попадающей в указанный диапазон (от 15 до 20) вводим сами с клавиатуры

import random
import sys

def fill_list(a:list, n):
    for i in range(n):
        a.append(random.randint(10, 40))

def print_list(a):
    for k in a:
        print(k, end=' ')
    print()

def find_max(a):
    max = -sys.maxsize
    for k in a:
        if k > max:
            max = k
    return max

def find_average(a):
    sum = 0
    for k in a:
        sum += k
    avg = sum / len(a)
    return avg

def change_list(a):
    for i in range(len(a)):
        a[i] -= 2

# def read_file(a):
#     with open('file.csv') as file:
#         for line in file:
#             b = line.split(';')
#             for c in b:
#                 a.append(int(c))


def main():
    count_days = int(input('Введите кол-во дней: '))
    a = []
    fill_list(a, count_days)
    print_list(a)
    max = find_max(a)
    print(f'Максим тем-ра = {max}')
    avg = find_average(a)
    print(f'Средняя = {avg}')
    change_list(a)
    print_list(a)

main()

