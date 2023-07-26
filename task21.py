# Открываем файл ts.csv и считываем его
with open('ts_00.csv', 'r') as file:
    data = file.read()
    # Разделяем данные на строки
    lines = data.split('\n')
    #Разделяем строки на элементы
    rows = [line.split(',') for line in lines]
    #Посчитаем количество нулевых элементов в массиве
    count_zeroes = 0
    for row in rows:
        for element in row:
            try:
                #Проверяем, равен ли элемент нулю
                if float (element) == 0:
                    count_zeroes += 1
            except ValueError:
                pass
            #Выводим количество нулевых элементов
                print("Количество нулевых элементов :", count_zeroes)
                # Повторим
                with open('ts_03.csv', 'r') as file:
                    data = file.read()
                    lines = data.split('\n')
                    rows = [line.split(',') for line in lines]
                    count_zeroes = 0
                    for row in rows:
                        for element in row:
                            try:
                                if float (element) == 0:
                                    count_zeroes += 1
                            except ValueError:
                                pass
                                print("Количество нулевых элементов:", count_zeroes)
                                with open('ts_laba.csv', 'r') as file:
                                    data = file.read()
                                    lines = data.split('\n')
                                    rows = [line.split(',') for line in lines]
                                    count_zeroes = 0
                                    for row in rows:
                                        for element in row:
                                            try:
                                                if float (element) == 0:
                                                    count_zeroes += 1
                                            except ValueError:
                                                pass
                                                print("Количество нулевых элементов:", count_zeroes)