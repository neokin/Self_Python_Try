def go(flag, i, j, iamount, jamount):
    if(flag == 'U'):
        if(j - 1 >= 0):
            if (Matrix[i][j - 1] == ['0']):
                j = j - 1
                flag = 'R'
                return (flag, i, j)
        if (i + 1 < iamount):
            if (Matrix[i + 1][j] == ['0'] ):
                i = i + 1
                flag = 'U'
                return (flag, i, j)
        if (j + 1 < jamount):
            if (Matrix[i][j + 1] == ['0']):
                j = j + 1
                flag = 'L'
                return (flag, i, j)
        if (i - 1 >= 0):
            if (Matrix[i - 1][j] == ['0']):
                i = i - 1
                flag = 'D'
                return (flag, i, j)

    if(flag == 'R'):
        if (i - 1 >= 0):
            if (Matrix[i - 1][j] == ['0']):
                i = i - 1
                flag = 'D'
                return (flag, i, j)
        if (j - 1 >= 0):
            if (Matrix[i][j - 1] == ['0']):
                j = j - 1
                flag = 'R'
                return (flag, i, j)
        if (i + 1 < iamount):
            if (Matrix[i + 1][j] == ['0']):
                i = i + 1
                flag = 'U'
                return (flag, i, j)
        if (j + 1 < jamount):
            if (Matrix[i][j + 1] == ['0']):
                j = j + 1
                flag = 'L'
                return (flag, i, j)

    if(flag == 'D'):
        if (j + 1 < jamount):
            if (Matrix[i][j + 1] == ['0']):
                j = j + 1
                flag = 'L'
                return (flag, i, j)
        if (i - 1 >= 0):
            if (Matrix[i - 1][j] == ['0']):
                i = i - 1
                flag = 'D'
                return (flag, i, j)
        if (j - 1 >= 0):
            if (Matrix[i][j - 1] == ['0']):
                j = j - 1
                flag = 'R'
                return (flag, i, j)
        if (i + 1 < iamount):
            if (Matrix[i + 1][j] == ['0']):
                i = i + 1
                flag = 'U'
                return (flag, i, j)

    if(flag == 'L'):
        if (i + 1 < iamount):
            if (Matrix[i + 1][j] == ['0']):
                i = i + 1
                flag = 'U'
                return (flag, i, j)
        if (j + 1 < jamount):
            if (Matrix[i][j + 1] == ['0']):
                j = j + 1
                flag = 'L'
                return (flag, i, j)
        if (i - 1 >= 0):
            if (Matrix[i - 1][j] == ['0']):
                i = i - 1
                flag = 'D'
                return (flag, i, j)
        if (j - 1 >= 0):
            if (Matrix[i][j - 1] == ['0']):
                j = j - 1
                flag = 'R'
                return (flag, i, j)

def getResult():
    try:
        pairs = (0, 0)
        stack = []
        beg = [0, 0]
        for j in range(jamount):
            if Matrix[0][j] == ['0']:
                fl = 'U'
                iind = 0
                jind = j
                beg[0] = iind
                beg[1] = j
                stack.append(beg)
                psi = iamount - 1
                while(iind != psi):
                    fl, iind, jind = go(fl, iind, jind, iamount, jamount)
                    pairs = list(pairs)
                    pairs[0] = iind
                    pairs[1] = jind
                    if (pairs == stack[0]):
                        fl, pairs[0], pairs[1] = go(fl, pairs[0], pairs[1], iamount, jamount)
                        pairs = tuple(pairs)
                        if(pairs == stack[1]):
                            return "Impossible"
                    pairs = tuple(pairs)
                    stack.append(pairs)
                while(stack):
                    pairs = stack.pop()
                    Matrix[pairs[0]][pairs[1]] = ['1']
    except:
        return "Impossible"
    return "Possible"

fin = open("in.txt")
var = []
var = fin.readline().split()
a = []
Matrix = []
iamount = int(var[0])
jamount = int(var[1])
for i in range(iamount):    # this is a count of raws
    for j in range(jamount):    # and this is a count of strings
        a.append(fin.readline(1).split())
    Matrix.append(a)
    fin.readline(1)
    a = []

#for i in range(iamount):
 #   print(Matrix[i])

result = getResult()
#print(Matrix[2])    # print second string in matrix
#print(Matrix[2][3])    # print element in second string zerouth raw
fout = open("out.txt", "w")
fout.write(str(result))
fin.close()
fout.close()


