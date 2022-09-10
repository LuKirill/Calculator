from fractions import Fraction
import my_ui


def fraction_2():
    c = int(input("Делитель_2: "))
    d = int(input("Делимое_2: "))
    if c == 0 and d == 0:
        my_ui.write_line("nan")
        exit()
    elif d == 0:
        my_ui.write_line("∞")
        exit()
    f2 = Fraction(c, d)
    return f2