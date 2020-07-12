def count_digit(num, a):
    count = 0
    while num != 0:
        b = num % 10
        if a == b:
            count += 1
        num //= 10
    return count


def max_freq(num):
    max_count = 0
    while num != 0:
        a = num % 10
        count = count_digit(num, a)
        num //= 10
        if count > max_count:
            max_count = count
            max = a
    return max_count, max

def main():
    num = int(input('Введите число: '))
    max_count, max = max_freq(num)
    print(f'Самая часто встречающаяся цифра = {max}, частота = {max_count}')



if __name__ == '__main__':
    main()