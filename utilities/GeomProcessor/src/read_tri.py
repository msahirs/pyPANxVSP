import os
import numpy as np
# from volumetrics import in_hull
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.style as mplstyle
mplstyle.use(['dark_background'])
import trimesh
from matplotlib import cm

import time
import scipy.spatial as spa

# import tqdm

def check_file_exists(filename):

    assert os.path.isfile(filename) == True, \
        "File does not exist. Program Exited"

    return "File exists, continuing..."

def check_file_ext(filename, ext = ""):

    assert filename.lower().endswith(ext) == True, \
        "Invalid file extension. Program Exited"

    return "Valid file extension, continuing..."

def check_line_field(str_input, field):
    pass

def read_blocks(file):

    start = time.time()
    op_file = open(file, "r")
    data = op_file.readlines()
    
    N_verts, N_tris = map(int, data[0].split(" "))
    # print(N_verts, N_tris)
    
    verts = np.genfromtxt(data[1:1+N_verts],
                          dtype= np.float64)
    
    tri_verts = np.genfromtxt(data[1+N_verts:1+N_verts+N_tris],
                              dtype= np.int32) - 1
    
    comps = np.genfromtxt(data[1+N_verts+N_tris:1+N_verts+2*N_tris],
                          dtype= np.int32)
    end = time.time()

    return verts, tri_verts, comps

    # print(f"\nTotal execution time for single call = {(end-start):.5} seconds ",)
    # fig = plt.figure(figsize=(12,6))

    # ax = fig.add_subplot(1, 1, 1, projection='3d')
    # ax.plot_trisurf(verts[:,0],verts[:,1],verts[:,2],
    #                 triangles=tri_verts, cmap=plt.cm.inferno)
    # # ax.plot(verts[:,0],verts[:,1],verts[:,2],
    # #                 'o', mec='m', color='none', lw=1, markersize=5)
    
    # ax.set_xlabel('X Length')
    # ax.set_ylabel('Y Length')
    # ax.set_zlabel('Z Length')

    # ax.set_xlim3d(0, 20)
    # ax.set_ylim3d(-10, 10)
    # ax.set_zlim3d(-10, 10)
    # ax.set_aspect('auto')
    # plt.show()

    # mesh = trimesh.Trimesh(vertices=tri_verts,
    #                        faces=tri_verts)

class tri_Reader():

    """Reader class for `.tri` tesselation data format

    See below link for more info on data structuring https://www.nas.nasa.gov/publications/software/docs/cart3d/pages/cart3dTriangulations.html#2.%20Configuration%20file%20format

    """    

    def __init__(self, filename) -> None:

        check_file_exists(filename)
        check_file_ext(filename)

        self.rel_path = filename


def test_read():

    base_path = "utilities/GeomProcessor/meshes/"
    verts, tri_verts, comps = read_blocks(base_path + "trii_ex.tri")

def test_trimesh(): 

    base_path = "utilities/GeomProcessor/meshes/"
    verts, tri_verts, comps = read_blocks(base_path + "trii_ex.tri")

    mesh = trimesh.Trimesh(vertices=verts,
                           faces=tri_verts)
    
    broke = trimesh.repair.broken_faces(mesh)

    viridis = mpl.colormaps['inferno'].resampled(100)
    print(viridis)
    col_map = viridis(np.linspace(0, 1, mesh.visual.face_colors.shape[0])) * 255
    color_x = np.array([0,20.3,100,75])
    # mesh.visual.face_colors = np.tile(color_x,(mesh.visual.face_colors.shape[0],1))
    mesh.visual.face_colors = col_map
    mesh.visual.face_colors[broke] = np.array([255,0,0,255])
    print(mesh.faces.shape)
    print(mesh.is_watertight)
    # print(mesh.visual.face_colors.shape)
    
    # color_y = np.array([255,0,0,0])
    # mesh.visual.face_colors = np.tile(color_x,(mesh.visual.face_colors.shape[0],1))
    # points = trimesh.PointCloud(vertices=mesh.vertices,
    #                              colors=np.tile(color_y,(mesh.visual.face_colors.shape[0],1)))
    scene = trimesh.Scene([
                       mesh])
    
    scene.show(flags={'axis': True})


# test_read()
test_trimesh()
