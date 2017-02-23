import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ax.scatter(x,y,z,c='r',marker='o')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")
plt.show()
