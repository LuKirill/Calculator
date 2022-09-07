def repeat():
    while True:
        f = input('ещё раз?\n')
        if f == 'y':
            simple_calc()
        elif f == 'n':
            print("Chao!")
            exit()
        else:
            print("Выберите "'y'" или "'n'"")