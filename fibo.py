def fib(n):
    res =[]
    a,b = 0, 1
    while (a < n):
        #print (a, end=' ')
        res.append(a)
        a, b = b, a+b
    return res
