def readfile():
    file = open("input.txt", 'r')
    size = int(file.readline())
    a = []
    for line in file:
        b = line.split()
        for i in range(len(b)):
            b[i] = int(b[i])
        a.append(b)
    file.close()
    return a

def checkrow(a: list):
    n = len(a)
    for row in a:
        for el in row:
            if el < 1 or el > n or row.count(el) > 1:
                return False
    return True

def checkcolumn(a: list):
    n = len(a)
    for j in range(n):
        c = []
        for i in range(n):
            c.append(a[i][j])
        for el in c:
            if el < 1 or el > n or c.count(el) > 1:
                return False
    return True








def main():
    a = readfile()



