from scipy.spatial import Delaunay, ConvexHull
import numpy as np
from matplotlib import cm

def in_hull(p, hull):
    """
    Test if points in `p` are in `hull`

    `p` should be a `NxK` coordinates of `N` points in `K` dimensions
    `hull` is either a scipy.spatial.Delaunay object or the `MxK` array of the 
    coordinates of `M` points in `K`dimensions for which Delaunay triangulation
    will be computed
    """

    if not isinstance(hull,Delaunay):
        hull = Delaunay(hull)

    return hull.find_simplex(p)>=0

def test_func_convex_hull():

    import matplotlib.pyplot as plt

    points = np.random.uniform(0, 10, size=(4000, 3) )  # Random points in 2-D

    points_check = np.random.uniform(0, 15, size=(100, 3) )

    hull = ConvexHull(points)
    
    check_interior = in_hull(points_check,points[hull.vertices])
    

    int_points = points_check[check_interior]
    ext_points = points_check[~check_interior]

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3), subplot_kw=dict(projection="3d"))

    for ax in (ax1, ax2):
        ax.plot(points[:, 0], points[:, 1], points[:, 2], '.', color='k')
        if ax == ax1:
            ax.set_title('Given points')
        else:
            ax.set_title('Convex hull')
            for simplex in hull.simplices:
                ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'c')
            ax.plot(points[hull.vertices, 0], points[hull.vertices, 1], points[hull.vertices, 2], 'o', mec='m', color='none', lw=1, markersize=5)
            ax.plot(int_points[:, 0], int_points[:, 1], int_points[:, 2], 'x', mec='g', color='none', lw=1, markersize=10)
            ax.plot(ext_points[:, 0], ext_points[:, 1], ext_points[:, 2], 'x', mec='r', color='none', lw=1, markersize=10)
        ax.set_xticks(range(15))
        ax.set_yticks(range(15))
    plt.show()

    # print(points)

    # print(in_hull(points_1,hull.simplices))

def test_func_stock():

    from read_hrm import hrm_Reader
    import matplotlib.pyplot as plt

    base_path = "utilities/GeomProcessor/meshes/"
    hrm = hrm_Reader(base_path + "convex_hull_test.hrm")

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3), subplot_kw=dict(projection="3d"))

    point_cloud = hrm.cart_points_np
    # print(len(point_cloud))
    # for i in point_cloud:
    #     print(i.shape)
    stack = np.vstack(point_cloud)
    # print(stack.shape)
    
    # hull = ConvexHull(stack)
    # delauney_rep = Delaunay(stack)
   
    fuselage = point_cloud[0]
    wing_1 = point_cloud[1]
    hull = Delaunay(fuselage)
    mask = in_hull(wing_1,hull)
    
    wing_1_fix = wing_1[~ mask]
    

    for ax in (ax1, ax2):

        ax.scatter(fuselage[:, 0], fuselage[:, 1], fuselage[:, 2],
                   marker='o', color='g', s=4)
        
        
        if ax == ax1:
            ax.scatter(wing_1[:,0],wing_1[:,1],wing_1[:,2],
                    marker='o', color = 'b', s=4)
            ax.set_title('Direct Import with Convex Hull')

            # for simplex in hull.simplices:
            #     ax.plot(fuselage[simplex, 0], fuselage[simplex, 1], fuselage[simplex, 2], 'c')

            for simplex in hull.simplices:
                ax.plot(fuselage[simplex, 0], fuselage[simplex, 1], fuselage[simplex, 2],
                        'o', mec='m', color='none', lw=1, markersize=5)
            
            # ax.plot_trisurf(stack[:,0],stack[:,1], stack[:,2], cmap = cm.inferno, linewidth=0)
            
        else:
            ax.scatter(wing_1_fix[:,0],wing_1_fix[:,1],wing_1_fix[:,2],
                    marker='o', color = 'b', s=4)
            ax.set_title('With Delauney Subtraction')

            # for simplex in wing_1_del.simplices:
            #     ax.plot(wing_1_fix[simplex, 0], wing_1_fix[simplex, 1], wing_1_fix[simplex, 2], 'c')
            
        ax.set_xlabel('X Length')
        ax.set_ylabel('Y Length')
        ax.set_zlabel('Z Length')

        ax.set_xlim3d(0, 14)
        ax.set_ylim3d(-3, 3)
        ax.set_zlim3d(-3, 3)

    plt.show()

    # print(point_cloud)
    
# test_func_convex_hull()
test_func_stock()




