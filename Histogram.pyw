import numpy as np
import matplotlib.pyplot as plt

cat = ['Высокий уровень', 'Средний уровень', 'Низкий уровень']

group1 = [4, 10, 6]
group2 = [4, 9, 7]
group3 = [1, 3, 16]
group4 = [13, 7, 1]

width = 0.3

x = np.arange(len(cat))

fig, ax = plt.subplots()

ax.bar(x - width/2, group1, width, label='ЭГ')
ax.bar(x + width/2, group2, width, label='КГ')

ax.set_title('Умение ставить цель исследования')
ax.set_xticks(x)
ax.set_xticklabels(cat)
ax.legend()
plt.show()
