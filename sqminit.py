fin = open("in.txt")
var = []
var = fin.readline().split()
print(var)
print(var[0])
print(var[1])
a = []
A = []
for j in range(6):    # this is a count of raws
    for i in range(7):    # and this is a count of strings
        a.append(fin.readline(1).split())
    A.append(a)
    a = []
print('\n')
print(A)
print('\n')
print(A[2])    # print second string in matrix
print(A[2][0])    # print element in second string zerouth raw
fout = open("out.txt", "w")    # open file for writing
fout.close()
fin.close()