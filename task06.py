import csv
import pandas as pd
#Задача1
#Чтение файла ts_00.csv, ts_03.csv и ts_laba.csv
data_df1 = pd.read_csv('ts_00.csv')
data_df2 = pd.read_csv('ts_03.csv')
data_df3 = pd.read_csv('ts_laba.csv')
# Выводим на печать первые 10 значений из DataFrame. Мы можем использовать метод head()
print(data_df1.head(10), data_df2.head(10), data_df3.head(10))