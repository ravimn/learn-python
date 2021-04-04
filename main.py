import fibo
import matplotlib.pyplot as plt


def plotFib(i=1000, x=0, y=1):
    res = fibo.fib()

    n = len(res)
    print(n)
    x = list(range(n))
    print(x)

    plt.plot(x, res)

    plt.show()


if __name__ == '__main__':
    print('Hello World')
    plotFib()
