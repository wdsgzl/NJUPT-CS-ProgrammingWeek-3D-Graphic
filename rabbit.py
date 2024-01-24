import io

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def read_off(file):
    if 'OFF' != file.readline().strip():
        raise('Not a valid OFF header')
    n_verts, n_faces, n_dontknow = map(int, file.readline().strip().split(' '))
    #print(n_verts,n_faces, n_dontknow)
    verts = [[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(n_verts)]
    #print(verts)
    faces = [[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)]
    #print(faces)
    verts = np.array(verts)
    faces = np.array(faces)
    return verts, faces

with open('Bunny.off', 'r') as f:
    verts, faces = read_off(f)




def draw(verts,faces):
    scale_factor = 2.0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    ax.add_collection3d(Poly3DCollection(verts[faces],facecolors='b'))
    plt.show()





#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.add_collection3d(Poly3DCollection(verts[dian.wby]))




