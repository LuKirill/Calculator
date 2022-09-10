import div, mult, diff, sum, my_ui


def integer():
    my_ui.write_line("Приступим к вычислению челых чисел!")
    num1 = int(input("x: "))
    act_list = ['-', '+', '*', '/']
    act = input("Выберите знак: '+', '-', '*', '/': ")
    if act not in act_list:
        my_ui.write_line("Выберите знак: '+', '-', '*', '/'")
    num2 = float(input("y: "))
    if act == "+":
        my_ui.write_line(sum.sum(num1, num2))
    elif act == "-":
        my_ui.write_line(diff.diff(num1, num2))
    elif act == "*":
        my_ui.write_line(mult.mult(num1, num2))
    elif act == "/":
        if num2 == 0:
            my_ui.write_line("∞")
        elif num2 == 0 and num1 == 0:
            my_ui.write_line("nan")
        else:
            my_ui.write_line(div.div(num1, num2))