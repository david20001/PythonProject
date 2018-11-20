
import numpy as np
from scipy.integrate import quad,dblquad,nquad

print(quad(lambda x: np.exp(-x), 0, np.inf))
print(dblquad(lambda t, x: np.exp(-x*t)/t**3, 0, np.inf, lambda x: 1, lambda x: np.inf))
print('hello')
print('test')
