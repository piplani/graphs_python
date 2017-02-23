from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.xlabel('X axis -------->')
plt.ylabel('Y axis--------->')
plt.title('Graph Title')
plt.suptitle('Graph Super Title')

# plt.plot([1, 2, 3, 4])  # generates x from 0-len(list) and y as provided in list
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r--') # default color is red and r-- is for dotted line ro for round object
plt.axis([0, 6, 0, 20])
plt.show()
