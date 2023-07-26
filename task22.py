#Чтение содержимого файлов во временной ряд
with open('ts_00.csv') as f:
    ts_00 = [float(line) for line in f]
    with open('ts_03.csv') as f:
     ts_03 = [float(line) for line in f]
     with open('ts_laba.csv') as f:
      ts_laba = [float(line) for line in f]
      # Объединение временного ряда
      combined_ts = ts_00 + ts_03 + ts_laba
      # Пузырковая сортировка по возрастанию
      n = len(combined_ts)
      for i in range(n-1):
        for j in range(0, n-i-1):
          if combined_ts[j] > combined_ts[j+1]:
            combined_ts[j], combined_ts[j+1] = combined_ts[j+1], combined_ts[j]
            # Вывод отсортированного временного ряда по возрастанию
            for value in combined_ts:
              print(value)