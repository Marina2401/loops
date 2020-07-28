import random
import math
import sys

def fill_list(a, n):
    for i in range(n):
        a.append(random.randint(10, 40))

def print_list(a):
    for k in a:
        print(k, end=' ')
    print()


def average_by_weeks(a):
    weeks = []
    count_week = math.ceil(len(a) / 7)
    for i in range(count_week):
        start = i * 7
        end = start + 7
        if end > len(a):
            end = len(a)
        sum = 0
        max = -sys.maxsize
        for j in range(start, end):
            sum += a[j]
            if a[j] > max:
                max = a[j]
        avg = round(sum / (end - start), 2)
        weeks.append(avg)
        weeks.append(max)
    return weeks


def main():
    count_day = int(input('кол-во дней: '))
    temps = []
    fill_list(temps, count_day)
    print_list(temps)
    avg_weeks = average_by_weeks(temps)
    print_list(avg_weeks)

main()

