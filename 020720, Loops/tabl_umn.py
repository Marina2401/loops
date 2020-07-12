#Вывести таблицу умножения для чисел от 1 до 10

# a = 1
# while a <= 10:
#     i = 1
#     while i <= 10:
#         print(f'{a} * {i} = {a * i}')
#         i += 1
#     print()
#     a += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')
    print()