import csv
import pandas as pd
#Задача1
#Чтение файла ts_00.csv, ts_03.csv и ts_laba.csv
data_df1 = pd.read_csv('ts_00.csv')
data_df2 = pd.read_csv('ts_03.csv')
data_df3 = pd.read_csv('ts_laba.csv')
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