#encoding=utf-8
##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)
plt.figure()
plt.plot(x, c, color='blue', linewidth=1.0, linestyle='-', label='cos', alpha=0.5)
plt.plot(x, s, 'r-', label='sin')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.title('cos and sin')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.legend(loc='upper right')
plt.grid()

plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color='green', alpha=0.25)

plt.show()




