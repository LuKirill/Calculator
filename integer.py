import div, mult, diff, sum

def integer():
    write_line("Приступим к вычислению челых чисел!")
    num1 = int(input("x: "))
    act_list = ['-', '+', '*', '/']
    act = input("Выберите знак: '+', '-', '*', '/': ")
    if act not in act_list:
        write_line("Выберите знак: '+', '-', '*', '/'")
    num2 = float(input("y: "))
    if act == "+":
        write_line(sum.sum(num1, num2))
    elif act == "-":
        write_line(diff.diff(num1, num2))
    elif act == "*":
        write_line(mult.mult(num1, num2))
    elif act == "/":
        if num2 == 0:
            write_line("∞")
        elif num2 == 0 and num1 == 0:
            write_line("nan")
        else:
            write_line(div.div(num1, num2))