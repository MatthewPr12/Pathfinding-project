from math import sin
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import csv


def read_surf2plot(name):
    with open(f'{name}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        z = []
        for idx, row in enumerate(reader):
            if idx == 0:
                l, step = map(int, row)
                continue
            if idx == 1:
                A = tuple(map(int, row))
                continue
            if idx == 2:
                B = tuple(map(int, row))
                continue
            z.append(list(map(float, row)))
    lim = ((l - 1) // 2) * step

    x = [[- lim + i * step for j in range(l)] for i in range(l)]
    y = [[- lim + j * step for j in range(l)] for i in range(l)]

    return np.array(x), np.array(y), np.array(z), lim, A, B
            

def plot(x, y, z, lim, path=None, opacity=0.5):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_surface(x, y, z, cmap="viridis", edgecolor='none', alpha=opacity)
    ax.set_title('Surface plot')
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)

    if path:
        path_x = []
        path_y = []
        path_z = []
        for i, j in path:
            path_x.append(x[i][j])
            path_y.append(y[i][j]) 
            path_z.append(z[i][j] + 10)

        ax.plot(path_x, path_y, path_z, )

    plt.show()


if __name__ == "__main__":
    for filename in ["example1"]:
        x1, y1, z1, lim, A, B = read_surf2plot(f"examples/{filename}")
        # specify your path here
        with open("results.txt", "r", encoding="utf-8") as res_file:
            path = eval(res_file.read())
        plot(x1, y1, z1, lim, path)
