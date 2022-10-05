import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from pkg_resources import yield_lines

y_vt = np.array([247.394558, 247.394558, 254.704174, 252.944478, 254.895956, 248.776840, 246.731277, 254.680096, 250.731632])
x_vt = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

y_vk = np.array([381.160702, 243.206897, 183.364407, 145.950376, 122.617780, 105.611456, 93.279504, 83.760765])
x_vk = np.array([2, 3, 4, 5, 6, 7, 8, 9])

label_t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
label_k = [2, 3, 4, 5, 6, 7, 8, 9]

aux_x = [3, 3, 3, 3, 3, 3, 3, 3, 3]
aux_y = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

x = np.array([3, 3, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, 3, 3, 3, 3, 3]) #k
y = np.array([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9,]) #t
z = np.array([247.394558, 247.394558, 381.160702, 243.206897, 243.206897, 145.950376, 122.61778, 105.611456, 93.279504, 83.760765,
                254.704174, 252.944478, 254.895956, 248.776840, 246.731277, 254.680096, 250.731632])

z = np.arange(len(x)*len(y)).reshape(len(x), len(y))
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, z, rstride=1, cstride=1, cmap='plasma', edgecolor='none')

ax.set_zlabel('Time (s)')
ax.set_ylabel('Values of t')
ax.set_xlabel('Values of k')

# x_vt, y_vt = np.meshgrid(x_vt, y_vt)

# plt.plot(x_vt, y_vt, color='magenta', marker='*', label='Varying t with k = 3', markersize=8)
# ax = plt.gca()
# ax.contour3D(x_vt, y_vt, z_vt, 50, cmap='binary')
# for i, txt in enumerate(label_t):
#     ax.text(aux_x, x_vt, y_vt, txt, size=15, zorder=1, color='k')

# x_vk, y_vk = np.meshgrid(x_vk, y_vk)

# plt.plot(x_vk, y_vk, color='green', marker='.', label='Varying k with t = 0.2', markersize=10)
# ax = plt.gca()
# ax.contour3D(x_vk, y_vk, z_vk, 50, cmap='binary')
# for i, txt in enumerate(label_k):
#     ax.text(x_vk, aux_y, y_vk, txt, size=15, zorder=1, color='k')

# ax.get_xaxis().set_visible(False)

# plt.zticks(fontsize=14)
# plt.zlabel('Time (s)', fontsize=18)
plt.title('Processing time of t-Closeness')
fig.colorbar(surf, shrink=0.5, aspect=10, pad=0.15)
# plt.legend(bbox_to_anchor=(0.98, 0.97), loc='upper right', borderaxespad=0, fontsize=18)
plt.show()
# plt.savefig('t-closeness_3dtime' + '.pdf')