import random

def fill(arr, n):
    for i in range(n):
        k = random.randint(0, 100)
        if k % 2 == 0:
            arr.append(1)
        else:
            arr.append(-1)

def print_list(a):
    for k in a:
        print(k, end=' ')
    print()

def invite_more_women(arr):
    count_men = 0
    for k in arr:
        if k == 1:
            count_men += 1
    if count_men > len(arr)//2:
        return True
    else:
        return False

def main():
    n = 4
    a = []
    fill(a, n)
    print_list(a)
    check = invite_more_women(a)
    if check:
        print('yes')
    else:
        print('no')

main()