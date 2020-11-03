import random

def read_file():
    with open("words.txt", "r", encoding="UTF-8") as file:
        a = file.read().splitlines()
        questions = []
        for i in range(0, len(a), 2):
            questions.append([a[i], a[i+1]])
    return questions

def main():
    questions = read_file()
    question = random.choice(questions)
    name, answer = question
    print(name)

    secret = "*" * len(answer)
    print(secret)
    while '*' in secret:
        c = input('Введите букву: ')
        if c in answer:
            print('Есть такая буква')
            for i in range(len(answer)):
                if answer[i] == c:
                    secret = secret[:i] + c + secret[i+1:]
            print(secret)


main()