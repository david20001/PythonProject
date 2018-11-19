#encoding=utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 512, endpoint=True)
c, s = np.cos(x), np.sin(x)
plt.figure()
plt.plot(x, c)
plt.plot(x, s)
plt.show()




