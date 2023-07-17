import csv
import pandas as pd
import matplotlib.pyplot as plt
#Задача1
#Чтение файла ts_00.csv, ts_03.csv и ts_laba.csv
data_df1 = pd.read_csv('ts_00.csv')
data_df2 = pd.read_csv('ts_03.csv')
data_df3 = pd.read_csv('ts_laba.csv')
#Задача5
csv_file1 = "ts_00.csv"
def plot_function(csv_file1):
 data_df1 = pd.read_csv(csv_file1)
 return data_df1
x_y = data_df1
#Построение графика функции
print(plt.plot(x_y))
print(plt.xlabel('x'))
print(plt.ylabel('y'))
print(plt.title('График функции'))
print(plt.show())
csv_file2 = "ts_03.csv"
def plot_function(csv_file2):
 data_df2 = pd.read_csv(csv_file2)
 return data_df2
x1_y1 = data_df2
print(plt.plot(x1_y1))
print(plt.xlabel('x1'))
print(plt.ylabel('y1'))
print(plt.show())
csv_file3 = "ts_laba.csv"
def plot_function(csv_file3):
 data_df3 = pd.read_csv(csv_file3)
 return data_df3
x2_y2 = data_df3
print(plt.plot(x2_y2))
print(plt.xlabel('x2'))
print(plt.ylabel('y2'))
print(plt.title('График функции'))
print(plt.show())
plot_function('ts_00.csv')
plot_function('ts_03.csv')
plot_function('ts_laba.csv')