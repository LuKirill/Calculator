import div, mult, diff, sum
import fraction_1, fraction_2


def calc_fraction():
    write_line("Приступим к вычислению рациональных чисел!")
    act_list = ['-', '+', '*', '/']
    act = input("Выберите знак: '+', '-', '*', '/': ")
    if act not in act_list:
        write_line("Выберите знак: '+', '-', '*', '/'")
    if act == "+":
        write_line(sum.sum(fraction_1.fraction_1(), fraction_2.fraction_2()))
    elif act == "-":
        write_line(diff.diff(fraction_1.fraction_1(), fraction_2.fraction_2()))
    elif act == "*":
        write_line(mult.mult(fraction_1.fraction_1(), fraction_2.fraction_2()))
    elif act == "/":
        write_line(div.div(fraction_1.fraction_1(), fraction_2.fraction_2()))