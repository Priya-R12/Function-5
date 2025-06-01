def isFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
factorial=isFactorial(5)
print(factorial)    