# Открытие файла и чтение содержимого в список
with open('ts_00.csv', 'r') as file:
    data = file.readlines()
data = [int(float(x.strip())) for x in data]
# Сортировка списка
data.sort()
# Функция для двоичного поиска значения
def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Поиск значения в каждом из трех файлов
val = 18.0
result = binary_search(data, val)
# Выводим значение найдено в файле на позиции
if result != -1:
    print(f"Значение {val} найдено в файле ts_00.csv на позиции {result}")
else:
    # Выводим значение не найдено в файле
    print(f"Значение {val} не найдено в файле ts_00.csv")
    # Повторим
with open('ts_03.csv', 'r') as file:
    data = file.readlines()
data = [int(float(x.strip())) for x in data]
data.sort()
val = 24.0
result = binary_search(data, val)
if result != -1:
    print(f"Значение {val} найдено в файле ts_03.csv на позиции {result}")
else:
    print(f"Значение {val} не найдено в файле ts_03.csv")
with open('ts_laba.csv', 'r') as file:
    data = file.readlines()
data = [int(float(x.strip())) for x in data]
data.sort()
val = 30.0
result = binary_search(data, val)
if result != -1:
    print(f"Значение {val} найдено в файле ts_laba.csv на позиции {result}")
else:
    print(f"Значение {val} не найдено в файле ts_laba.csv")