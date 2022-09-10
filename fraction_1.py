from fractions import Fraction
import my_ui


def fraction_1():
    a = int(input("Делитель_1: "))
    b = int(input("Делимое_1: "))
    if b == 0 and a == 0:
        my_ui.write_line("nan")
        exit()
    elif b == 0:
        my_ui.write_line("∞")
        exit()
    f1 = Fraction(a, b)
    return f1
