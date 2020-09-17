file = open("syn.txt", 'r')
n = int(file.readline())
m = {}
for i in range(n):
    row = file.readline().split()
    m[row[0]] = row[1]
    m[row[1]] = row[0]

c = file.readline()
file.close()
print(m[c])