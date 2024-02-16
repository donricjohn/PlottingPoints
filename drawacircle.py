import numpy as np
import matplotlib.pyplot as plt

angle = np.linspace(0, 2 * np.pi, 150)

radius = 0.4

x1 = radius * np.cos(angle)
z1 = radius * np.sin(angle)
y1 = np.zeros(150)
#l_hand = np.array([x1], [y1], [z1])


x2 = radius * np.cos(angle) + 0.4
z2 = radius * np.sin(angle)
y2 = np.zeros(150)
#r_hand = np.array([x2], [y2], [z2])

figure, axes = plt.subplots(1)
plt.xlabel('x(forward direction)')
plt.ylabel('z(upward direction')
axes.plot(x1, z1, color='orange')
axes.plot(x2, z2, color='blue')
axes.set_aspect(1)

plt.title('Circle')
plt.show()
print('l_hand coordinates', 'x',x1, 'y', y1, 'z', z1)
print('r_hand coordinates', 'x', x1, 'y', y1, 'z',z1)

