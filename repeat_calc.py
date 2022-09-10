def repeat():
    while True:
        f = input('ещё раз?\n')
        if f == 'y':
            simple_calc()
        elif f == 'n':
            write_line("Chao!")
            exit()
        else:
            write_line("Выберите "'y'" или "'n'"")