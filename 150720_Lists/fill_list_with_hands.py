#ручное заполнение списка по возрастающей
def check_up(a):
    for i in range(len(a)):
        if a[i+1] < a[i]:
            return False
    return True

