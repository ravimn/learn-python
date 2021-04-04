def fib(n=1000, a=0, b=1) -> list:
    res =[]
    while (a < n):
        #print (a, end=' ')
        res.append(a)
        a, b = b, a+b
    return res
