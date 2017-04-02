# Check if a given number is prime number?
# Prime numbers are only divisible by its own value (or 1)

def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True
