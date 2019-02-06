import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import data
data = pd.read_csv('./mpg.csv')

data_fwd = data.loc[data.drv == 'f']
data_rwd = data.loc[data.drv == 'r']
data_4wd = data.loc[data.drv == '4']

fig, axes = plt.subplots(2, 2, figsize=(15, 15))
fig.text(0.5, 0.9, "City fuel economy versus engine displacement", ha="center", fontsize=20)

axes[0, 0].scatter(data_fwd.displ, data_fwd.cty, s = 60, label = 'FWD', c='gold')
axes[0, 0].scatter(data_rwd.displ, data_rwd.cty, s = 60, label = 'RWD', c='lightblue')
axes[0, 0].scatter(data_4wd.displ, data_4wd.cty, s = 60, label = '4WD', c='black')
axes[0, 0].legend(title = 'drive train')
axes[0, 0].set_ylabel('fuel economy (mpg)', fontsize = 16)
axes[0, 0].set_xlabel('displacement (I)', fontsize = 16)

axes[0, 1].scatter(data_fwd.displ, data_fwd.cty, s = 60, label = 'FWD', c='gold', alpha = 0.5, edgecolor = 'gold')
axes[0, 1].scatter(data_rwd.displ, data_rwd.cty, s = 60, label = 'RWD', c='lightblue', alpha = 0.5, edgecolor = 'lightblue')
axes[0, 1].scatter(data_4wd.displ, data_4wd.cty, s = 60, label = '4WD', c='black', alpha = 0.5, edgecolor = 'k')
axes[0, 1].legend(title = 'drive train')
axes[0, 1].set_ylabel('fuel economy (mpg)', fontsize = 16)
axes[0, 1].set_xlabel('displacement (I)', fontsize = 16)

def jitter(rg, data):
    rn = [np.random.randint(min(data)-np.mean(data), max(data)-np.mean(data))*rg for _ in range(len(data))]
    return np.asarray(data) + np.asarray(rn)
       
axes[1, 0].scatter(jitter(0.03, data_fwd.displ), jitter(0.03, data_fwd.cty), s = 60, label = 'FWD', c='gold', alpha = 0.5, edgecolor = 'gold')
axes[1, 0].scatter(jitter(0.03, data_rwd.displ), jitter(0.03, data_rwd.cty), s = 60, label = 'RWD', c='lightblue', alpha = 0.5, edgecolor = 'lightblue')
axes[1, 0].scatter(jitter(0.03, data_4wd.displ), jitter(0.03, data_4wd.cty), s = 60, label = '4WD', c='black', alpha = 0.5, edgecolor = 'k')
axes[1, 0].legend(title = 'drive train')
axes[1, 0].set_ylabel('fuel economy (mpg)', fontsize = 16)
axes[1, 0].set_xlabel('displacement (I)', fontsize = 16)

axes[1, 1].scatter(jitter(0.15, data_fwd.displ), jitter(0.15, data_fwd.cty), s = 60, label = 'FWD', c='gold', alpha = 0.5, edgecolor = 'gold')
axes[1, 1].scatter(jitter(0.15, data_rwd.displ), jitter(0.15, data_rwd.cty), s = 60, label = 'RWD', c='lightblue', alpha = 0.5, edgecolor = 'lightblue')
axes[1, 1].scatter(jitter(0.15, data_4wd.displ), jitter(0.15, data_4wd.cty), s = 60, label = '4WD', c='black', alpha = 0.5, edgecolor = 'k')
axes[1, 1].legend(title = 'drive train')
axes[1, 1].set_ylabel('fuel economy (mpg)', fontsize = 16)
axes[1, 1].set_xlabel('displacement (I)', fontsize = 16)

plt.savefig('task23.png')
