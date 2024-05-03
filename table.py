import pandas as pd

input_filename = "Parprog_lab1/test.txt"

# Чтение данных из текстового файла
df = pd.read_csv(input_filename)

# Вывод таблицы
print(df)