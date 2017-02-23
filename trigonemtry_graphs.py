from matplotlib import pyplot as plt
import numpy as np
from math import cos,sin
import pandas as pd

x = np.arange(0.1, 14, 0.1)
plt.plot(x, np.cos(x), 'r--')
plt.plot(x, np.sin(x), 'r--',color='black')
plt.axis([0, 14, -1, 1])
plt.show()

