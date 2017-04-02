# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the odd-valued terms.

def fiboOddSum(s):   # sum all the odd terms less than 's'
    OddSum=0
    x=[0,1]
    while x[-1] < s:
        x.append(x[-2]+x[-1])

    for i in range(len(x)):
        if x[i]%2 != 0:
            OddSum=OddSum+x[i]
    return OddSum
