import pandas as pd
import matplotlib.pyplot as plt

income_data = pd.read_csv("students.csv", sep=";", header=None)
income_data.columns = ['prep', 'group', 'marks']
gr1 = income_data.groupby(['prep', 'marks'])['prep'].count().unstack('marks').fillna(0)
gr2 = income_data.groupby(['group', 'marks'])['group'].count().unstack('marks').fillna(0)
ax = gr1.plot(kind='bar', stacked=True, rot=0)
plt.savefig('preps.png')
bx = gr2.plot(kind='bar', stacked=True, rot=0)
plt.savefig('groups.png')
plt.show()
