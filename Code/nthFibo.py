# Find the nth fibonacci number

def fibonum(n):   
    x=[0,1]
    for i in range(2,n):
        x.append(x[i-2]+x[i-1])
    print(x[n-1])
