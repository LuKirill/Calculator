# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.
import draw_board, div, mult, diff, sum, repeat_calc
def simple_calc():
    draw_board.draw_board(draw_board.board)
    while True:
        num1 = float(input("x: "))
        act_list = ['-', '+', '*', '/']
        act = input()
        if act not in act_list:
            print("Выберите знак: '+', '-', '*', '/'")
        num2 = float(input("y: "))
        if act == "+":
            print(sum.sum(num1, num2))
        elif act == "-":
            print(diff.diff(num1, num2))
        elif act == "*":
            print(mult.mult(num1, num2))
        elif act == "/":
            if num2 == 0:
                print("∞")
            elif num2 == 0 and num1 == 0:
                print("nan")
            else:
                print(div.div(num1, num2))
        break
    repeat_calc.repeat()


simple_calc()
