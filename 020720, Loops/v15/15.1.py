#1. Начав тренировки, лыжник в первый день пробежал 10 км.
# Каждый следующий день он увеличивал пробег на 10% от пробега предыдущего дня. Определить:
#а) пробег лыжника за второй, третий, ..., десятый день тренировок;
#б) какой суммарный путь он пробежал за первые 7 дней тренировок.
#Решить задачу используя циклическую конструкцию for.
s_i = 10
i = 1
for i in range(2, 11):
    s_i = s_i + 0.1*s_i
    print(i, s_i)
s = 10
sum = 10
for j in range(2, 8):
    s = s + 0.1*s
    sum = sum + s
print(sum)


