import fibo
import scope
import matplotlib.pyplot as plt


def plotFib(i=1000, x=0, y=1):
    try:
        print("plotFib i = " + str(i) + " x = [" + str(x) + "] y = [" + str(y) + ']')
        res = fibo.fib(i, x, y)

        n = len(res)
        print(n)
        x = list(range(n))
        print(x)
        print(res)

        plt.plot(x, res)

        plt.show()
    finally:
        pass

if __name__ == '__main__':
    print("Hello World")
    while True:
        try:
            i = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Not a valid number.  Try again...")
    print ("Value of i is " + str(i))
    #plotFib(i)

    #scope_test
    scope.scope_test()
    print("In global scope:", scope.spam, "Type of scope is ", type(scope))
