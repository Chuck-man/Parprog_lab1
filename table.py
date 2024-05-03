import pandas as pd
import os
import dataframe_image as dfi

path_to_folder = "Parprog_lab1"
input_filename = "Parprog_lab1/test.txt"

# Чтение данных из текстового файла
df = pd.read_csv(input_filename)
df.columns.name = 'Time / Size'
first_row = df.iloc[0]
sorted_df = df[first_row.sort_values().index]
dfi.export(sorted_df, os.path.join(path_to_folder, "table.png"))


# Вывод таблицы
print(df)