#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
#%%
x = np.array([65,
65,
65,
75,
75,
75,
85,
85,
85])
y = np.array([3.91315,
3.5124,
3.6472,
5.7205,
2.7184,
2.84415,
3.6459,
3.6895,
3.65665])
z = np.array([2.227,
2.0375,
2.1225,
3.2015,
1.5685,
1.618,
2.0035,
2.059,
2.0515])
#%%
triang = mtri.Triangulation(x, y)
isBad = np.where((x<1) | (x>99) | (y<1) | (y>99), True, False)

mask = np.any(isBad[triang.triangles],axis=1)
triang.set_mask(mask)
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_trisurf(triang, z, cmap='jet')
ax.scatter(x,y,z, marker='.', s=10, c="black", alpha=0.5)
ax.view_init(elev=60, azim=-45)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#%%
