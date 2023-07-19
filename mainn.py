import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Математическое ожидание и дисперсия
mean = 4.262510
std = 72.485693
# Интервал времени
t1 = np.arange(0,133)
# Нормальное распределение
process1 = np.random.normal(mean, np.sqrt(std), len(t1))
# Отобразим график изображения случайного процесса с помощью matplotlib
mean = 4.262510
t2 = np.arange(0,133)
# Критерий Пуассона
process2 = np.random.poisson(mean, len(t2))
#Чтение файла ts_00.csv
data_df1 = pd.read_csv('ts_00.csv')
mean = np.mean(data_df1)
std = np.std(data_df1)
t3 = np.arange(0,133)
process3 = np.random.normal(mean, np.sqrt(std), len(t3))
# Математическое ожидание и дисперсия
mean = 39.568241
std = 193.837652
# Интервал времени
t4 = np.arange(0,105)
# Нормальное распределение
process4 = np.random.normal(mean, np.sqrt(std), len(t4))
# Отобразим график изображения случайного процесса с помощью matplotlib
mean = 39.568241
t5 = np.arange(0,105)
# Критерий Пуассона
process5 = np.random.poisson(mean, len(t5))
#Чтение файла ts_00.csv
data_df2 = pd.read_csv('ts_03.csv')
mean = np.mean(data_df2)
std = np.std(data_df2)
t6 = np.arange(0,105)
process6 = np.random.normal(mean, np.sqrt(std), len(t6))
# Математическое ожидание и дисперсия
mean = 380.117351
std = 695.170918
# Интервал времени
t7 = np.arange(0,98)
# Нормальное распределение
process7 = np.random.normal(mean, np.sqrt(std), len(t7))
# Отобразим график изображения случайного процесса с помощью matplotlib
mean = 380.117351
t8 = np.arange(0,98)
# Критерий Пуассона
process8 = np.random.poisson(mean, len(t8))
#Чтение файла ts_00.csv
data_df3 = pd.read_csv('ts_laba.csv')
mean = np.mean(data_df3)
std = np.std(data_df3)
t9 = np.arange(0,98)
process9 = np.random.normal(mean, np.sqrt(std), len(t9))
print(plt.plot(t1, process1))
print(plt.plot(t2, process2))
print(plt.plot(t3, process3))
print(plt.plot(t4, process4))
print(plt.plot(t5, process5))
print(plt.plot(t6, process6))
print(plt.plot(t7, process7))
print(plt.plot(t8, process8))
print(plt.plot(t9, process9))
print(plt.xlabel('Время'))
print(plt.ylabel('Сигнал'))
print(plt.legend(['data_df1', 'puasson1', 'gauss1','data_df2', 'puasson2', 'gauss2', 'data_df3', 'puasson3', 'gauss3' ]))
print(plt.title('Случайный процесс УФ сигнала'))
print(plt.show())