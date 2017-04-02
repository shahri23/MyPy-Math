# Produce n-terms of fibonacci series

def fiboterms(n):  
    x=[0,1]
    for i in range(2,n):
        x.append(x[i-2]+x[i-1])
    for j in range(n):
        print(x[j])
