import misc


def print_spam(s):
    print(s)


def print_one_letter(l):
    print(l, end='')


def do_twice(f, s):
    f(s)
    f(s)


def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)


def patternOf(a):
    def patternOfX(x):
        print_one_letter(a)
        do_four(print_one_letter, x)
        print_one_letter(a)
        do_four(print_one_letter, x)
        print_one_letter(a)
        print()

    return patternOfX

if __name__ == "__main__":
    fplus = patternOf('+')
    fpipe = patternOf('|')

    fplus('-')
    do_four(fpipe, ' ')
    fplus('-')
    do_four(fpipe, ' ')
    fplus('-')

    pass
