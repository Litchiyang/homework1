#smooth? not the same shape?
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import data
data = pd.read_csv('./task21.csv')

fig, ax1 = plt.subplots(1, 1, figsize=(20, 10))
fig.text(0.5, 0.94, "Japanese passenger cars sold in the US\n", ha="center", fontsize=20,color="red")
fig.text(0.5, 0.915, "correlates with\n", ha="center", fontsize=15, color="gray")
fig.text(0.5,0.91,"Suicides by crashing of motor vehicle", ha="center", fontsize=20, color="black")
#plt.title('Japanese passenger cars sold in the US\n correlates with\n Suicides by crashing of motor vehicle', y=1.06, fontsize = 25)
plt.suptitle('Correlation:93.57% (r=0.935701)', y=0.9, fontsize=14)


line1, = ax1.plot(data.year, data.japanese_cars_sold, '-o', c = 'r')
ax1.set_ylabel("Japanese cars sold", fontsize = 14)
ax1.set_xticks(np.arange(1999, 2010, step=1))
#ax1.xaxis.set_tick_params(labeltop=True)
ax1.yaxis.label.set_color('red')
ax1.set_yticks(np.arange(600, 1201, step=200))
ax1.tick_params(axis='y', colors = 'r')
ax1.set_yticklabels(['600 thousand cars','800 thousand cars', '1000 thousand cars', '1200 thousand cars'], fontsize = 14)

ax2 = ax1.twinx()
line2, = ax2.plot(data.year, data.suicides_by_crashing, '-o', c = 'k')
ax2.set_ylabel("Suicides by crashing", fontsize = 14)
ax2.set_yticks(np.arange(80, 141, step=20))
ax2.set_yticklabels(['80 suicides','100 suicides', '120 suicides', '140 suicides'], fontsize = 14)

plt.grid(linestyle="--", color='grey')

ax2.legend((line2, line1), ("Suicides by crashing", "Japanese cars sold"), bbox_to_anchor=(0.65, -0.04), ncol = 2, fontsize = 14)
plt.savefig('task21.png')