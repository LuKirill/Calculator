# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.

import draw_board, repeat_calc, integer, calc_fraction, my_ui


def simple_calc():
    draw_board.draw_board()
    while True:
        write_line("Выберите числовое множество для ввода: целое число 'I', рациональное 'R' или комплексное 'C'")
        set_sel = input("> ")
        if set_sel == "I":
            integer.integer()
        elif set_sel == "R":
            calc_fraction.calc_fraction()
        elif set_sel == "C":
            complex_num.complex_num()
        else:
            write_line("Жмакай 'I' или 'R' или 'C'")
        while True:
            f = input('ещё раз?\n')
            if f == 'y':
                simple_calc()
            elif f == 'n':
                write_line("Chao!")
                exit()
            else:
                write_line("Выберите "'y'" или "'n'"")


simple_calc()