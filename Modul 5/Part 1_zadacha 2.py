def Number (начало, конец):
    for число in range(начало, конец + 1):
        if число % 2 == 0:
            print(число)

начало = 10
конец = 20
Number (начало, конец)
