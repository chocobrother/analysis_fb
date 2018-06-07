#generater test

def squares(n=10):
   # data = []
    for i in range(n):
        #data.append(i,i**2)
        yield (i, i**2)



for x in squares(20):
    print(x)


