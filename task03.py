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