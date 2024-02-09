import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
t = np.linspace(0, 2*np.pi, 100)
f = np.cos(t)
g = np.sin(t)

line2 = ax.plot(f[0], g[0])[0]
ax.set(xlim=[0, 3], ylim=[-4, 10])



def update(frame):
    # for each frame, update the data stored on each artist.
    x = f[:frame]
    y = g[:frame]
    # update the line plot:
    line2.set_xdata(f[:frame])
    line2.set_ydata(g[:frame])
    return (line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
ani.save('test2dplot.gif', writer='imagemagick')
plt.show()