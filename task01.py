import csv
import pandas as pd
import matplotlib.pyplot as plt
#Задача1
#Чтение файла ts_00.csv, ts_03.csv и ts_laba.csv
data_df1 = pd.read_csv('ts_00.csv')
data_df2 = pd.read_csv('ts_03.csv')
data_df3 = pd.read_csv('ts_laba.csv')
# Выводим на печать первые 10 значений из DataFrame. Мы можем использовать метод head()
print(data_df1.head(10), data_df2.head(10), data_df3.head(10))
#Задача2
csv_file1 = "ts_00.csv"
csv_file2 = "ts_03.csv"
csv_file3 = "ts_laba.csv"
#Принимаем функцию на вход путь файла
def get_first_five_values(csv_file1):
    data_df1 = pd.read_csv(csv_file1)
    return data_df1 #Инструкция - return
def get_first_five_values(csv_file2):
    data_df2 = pd.read_csv(csv_file2)
    return data_df2
def get_first_five_values(csv_file3):
    data_df3 = pd.read_csv(csv_file3)
    return data_df3
#Выводим на печать первые 5 значений
print(data_df1.head(5), data_df2.head(5),data_df3.head(5))
#Продемонстрируем работу на ts_00,ts_03 и ts_laba
print(get_first_five_values('ts_00.csv'))
print(get_first_five_values('ts_03.csv'))
print(get_first_five_values('ts_laba.csv'))
csv_files = ['ts_00.csv','ts_03.csv', 'ts_laba.csv']
#Задача3
csv_file1 = "ts_00.csv"
csv_file2 = "ts_03.csv"
csv_file3 = "ts_laba.csv"
def get_statistics(csv_file1):
    data_df1 = pd.read_csv(csv_file1)
    return data_df1
def get_statistics(csv_file2):
    data_df2 = pd.read_csv(csv_file2)
    return data_df2
def get_statistics(csv_file3):
    data_df3 = pd.read_csv(csv_file3)
    return data_df3
#Выводим на печать статистическую информацию. Используется метод describe
print(data_df1.describe(), data_df2.describe(), data_df3.describe())
get_statistics('ts_00.csv')
get_statistics('ts_03.csv')
get_statistics('ts_laba.csv')
csv_files = ['ts_00.csv','ts_03.csv', 'ts_laba.csv']
#Задача4
#Визуализация данных
csv_file1 = "ts_00.csv"
x_y = data_df1
data_df1 = pd.read_csv(csv_file1)
#Построение графика функции
print(plt.plot(x_y))
print(plt.xlabel('x'))
print(plt.ylabel('y'))
print(plt.title('График функции'))
print(plt.show())
csv_file2 = "ts_03.csv"
x1_y1 = data_df2
data_df2 = pd.read_csv(csv_file2)
print(plt.plot(x1_y1))
print(plt.xlabel('x1'))
print(plt.ylabel('y1'))
print(plt.show())
csv_file3 = "ts_laba.csv"
x2_y2 = data_df3
data_df3 = pd.read_csv(csv_file3)
print(plt.plot(x2_y2))
print(plt.xlabel('x2'))
print(plt.ylabel('y2'))
print(plt.title('График функции'))
print(plt.show())
#Задача5
csv_file1 = "ts_00.csv"
def plot_function(csv_file1):
    data_df1 = pd.read_csv(csv_file1)
    return data_df1
x_y = data_df1
csv_file2 = "ts_03.csv"
def plot_function(csv_file2):
    data_df2 = pd.read_csv(csv_file2)
    return data_df2
x1_y1 = data_df2
csv_file3 = "ts_laba.csv"
def plot_function(csv_file3):
    data_df3 = pd.read_csv(csv_file3)
    return data_df3
x2_y2 = data_df3
print(plt.plot(x_y))
print(plt.plot(x1_y1))
print(plt.plot(x2_y2))
print(plt.xlabel('x'))
print(plt.ylabel('y'))
print(plt.xlabel('x1'))
print(plt.ylabel('y1'))
print(plt.xlabel('x2'))
print(plt.ylabel('y2'))
print(plt.title('Объединенный график функции'))
print(plt.legend(['00','03','laba']))
print(plt.show())
plot_function('ts_00.csv')
plot_function('ts_03.csv')
plot_function('ts_laba.csv')
#Задача6
def plot_combined_graph(csv_files):
    fig = plt.figure(figsize =(10,5))
    ax = plt.subplots()
    for csv_file1 in csv_files:
        data_df1 = pd.read_csv(csv_file1)
        return data_df1
    x_y =data_df1
    for csv_file2 in csv_files:
        data_df2 = pd.read_csv(csv_file2)
        return data_df2
    x1_y1 =data_df2
    for csv_file3 in csv_files:
        data_df3 = pd.read_csv(csv_file3)
        return data_df3
    x2_y2 =data_df3
    print(ax.plot(x_y))
    print(ax.plot(x1_y1))
    print(ax.plot(x2_y2))
    print(ax.set_xlabel('x'))
    print(ax.set_ylabel('y'))
    print(ax.set_xlabel('x1'))
    print(ax.set_ylabel('y1'))
    print(ax.set_xlabel('x2'))
    print(ax.set_ylabel('y2'))
    print(ax.set.title('Объединенный график функции'))
    print(ax.legend())
    print(plt.show())
    plot_combined_graph('ts_00.csv', 'ts_03.csv', 'ts_laba.csv')