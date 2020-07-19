#Требуется ввести размер файлов по порядку и объем диска и посчитать, сколько файлов вместится на диске
def save(sizes, hd):
    sum = 0
    i = 0
    while i < len(sizes) and sum <= hd:
        sum = sum + sizes[i]
        if sum <= hd:
            i += 1
    return i


def main():
    n = 50
    a = [ ]
    quant = save(a, n)
    print(quant)

main()

