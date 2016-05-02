infile = open("input.txt")
n = infile.readline().split()
number = int(n[0])
Matrix = []
isyet = False
for i in range(number):
    word = infile.readline().split()
    a = [ord(word[0][0]) - 97, ord(word[0][-1]) - 97]
    #a0+=a[0]
    if(Matrix):

        for j in Matrix:
            #print j
            if( a[0] == j[0]):
                j.append(a[1])
                isyet = True
                break
        if(isyet == False):
            Matrix.append(a)
        else:
            isyet = False
    else:
        Matrix.append(a)
print Matrix
