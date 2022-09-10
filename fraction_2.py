from fractions import Fraction


def fraction_2():
    c = int(input("Делитель_2: "))
    d = int(input("Делимое_2: "))
    if c == 0 and d == 0:
        print("nan")
        exit()
    elif d == 0:
        print("∞")
        exit()
    f2 = Fraction(c, d)
    return f2