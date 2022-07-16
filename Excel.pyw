from openpyxl import load_workbook
import numpy as np
import matplotlib.pyplot as plt

wb = load_workbook('2021-2022.xlsx', data_only=True)
sheet = wb.active

print(f'Размеры загруженной таблицы -> {sheet.dimensions}')


def cols_to_lst(name_cell, start, fin):
    cells_lst = []
    cols_name = sheet[f'{name_cell}{start}:{name_cell}{fin}']
    for i in range(fin - start + 1):
        cur_cell = cols_name[i][0].value
        cells_lst.append(cur_cell)
    return cells_lst


x = cols_to_lst('A', 2, 17)
y = cols_to_lst('G', 2, 17)

fig, ax = plt.subplots()
color_rec = np.random.rand(16, 3)  # Генерируем 16 троек чисел между 0 и 1
ax.bar(x, y, color=color_rec)

ax.set_facecolor('Seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(20)  # ширина Figure
fig.set_figheight(6)  # высота Figure

plt.show()
