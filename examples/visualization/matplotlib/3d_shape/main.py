import random
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# u = np.linspace(0, 2 * np.pi, 100)
u = np.array([[i + random.uniform(-0.3, 0.3) for i in np.linspace(0, 2 * np.pi, 50)]])
# v = np.linspace(0, np.pi, 100)
v = np.array([[i + random.uniform(-0.3, 0.3) for i in np.linspace(0, np.pi, 50)]])
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z)
ax.set_aspect('equal')
plt.show()
