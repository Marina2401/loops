a = [4, 2, 10, 7]

a.append(10)
a.append(20)
print(a)

a.remove(10)
print(a)

a.pop(1)
print(a)

a.insert(1, 100)
print(a)

for i in a:
    if i < 10:
        a.remove(i)
print(a)