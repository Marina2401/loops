#добавить курс студентам и список оценок
#вывести всех студентов заданного курса
#вывести студентов хотя бы с одной двойкой

def main():
    students = []

    while True:
        print('1.Добавить студента')
        print('2.Удалить')
        print('3.Редактировать')
        print('4.Вывести')
        print('5.Кол-во студентов заданного возраста')
        print('6. Все студенты заданного курса: ')
        print('7. все студенты хотя бы с одной двойкой: ')

        oper = int(input())
        if oper == 1:
            name = input('Введите имя: ')
            age = int(input('Введите возраст: '))
            height = int(input('Введите рост: '))
            course = int(input('введите курс: '))

            n = int(input('Введите количество оценок: '))
            marks = []
            for i in range(1, n+1):
                m = int(input('Введите оценку: '))
                marks.append(m)
            student = [name, age, height, course, marks]
            students.append(student)
        elif oper == 2:
            name = input('Введите имя: ')
            for student in students:
                if student[0] == name:
                    students.remove(student)
        elif oper == 4:
            for student in students:
                for info in student:
                    print(info, end='\t')
                print()
        elif oper == 5:
            start_age = int(input('Начальный возраст: '))
            end_age = int(input('Конечный возраст: '))
            count = 0
            for student in students:
                if start_age < student[1] < end_age:
                    count += 1
            print(f'Кол-во = {count}')
        elif oper == 6:
            c = int(input('Введите курс: '))
            for student in students:
                if student[3] == c:
                    print(student)
        elif oper == 7:
            for student in students:
                if student[4].count(2) >= 1:
                    print(student)

main()

