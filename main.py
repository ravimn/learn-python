import fibo
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('Hello World')
    i = 1000000
    res = fibo.fib(i)

    n = len(res)
    print(n)
    x = list(range(n))
    print(x)

    plt.plot(x, res)

    plt.show()





