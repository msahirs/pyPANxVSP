from scipy.spatial import Delaunay, ConvexHull
import matplotlib.pyplot as plt
import numpy as np

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

    points = np.random.uniform(0, 10, size=(200, 3) )  # Random points in 2-D

    hull = ConvexHull(points)

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3), subplot_kw=dict(projection="3d"))

    for ax in (ax1, ax2):
        ax.plot(points[:, 0], points[:, 1], points[:, 2], '.', color='k')
        if ax == ax1:
            ax.set_title('Given points')
        else:
            ax.set_title('Convex hull')
            for simplex in hull.simplices:
                ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'c')
            ax.plot(points[hull.vertices, 0], points[hull.vertices, 1], points[hull.vertices, 2], 'o', mec='r', color='none', lw=1, markersize=10)
        ax.set_xticks(range(10))
        ax.set_yticks(range(10))
    plt.show()

    points_1 = np.random.uniform(0, 15, size=(40, 3) )

    # print(points)

    print(in_hull(points_1,hull.simplices))

def test_func_stock():

    from read_hrm import hrm_Reader

    base_path = "utilities/GeomProcessor/meshes/"
    hrm = hrm_Reader(base_path + "convex_hull_test.hrm")

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3), subplot_kw=dict(projection="3d"))

    point_cloud = hrm.get_cart_points_as_np()
    fuselage = point_cloud[0]
    wing_1 = point_cloud[1]

    mask = in_hull(wing_1,fuselage)
    wing_1_fix = wing_1[~ mask]

    for ax in (ax1, ax2):

        ax.scatter(fuselage[:, 0], fuselage[:, 1], fuselage[:, 2],
                   marker='o', color='g', s=4)

        if ax == ax1:
            ax.scatter(wing_1[:,0],wing_1[:,1],wing_1[:,2],
                    marker='o', color = 'b', s=4)
            ax.set_title('Direct Import')
        else:
            ax.scatter(wing_1_fix[:,0],wing_1_fix[:,1],wing_1_fix[:,2],
                    marker='o', color = 'b', s=4)
            ax.set_title('With Delauney Subtraction')
            
        ax.set_xlabel('X Length')
        ax.set_ylabel('Y Length')
        ax.set_zlabel('Z Length')

        ax.set_xlim3d(10, 14)
        ax.set_ylim3d(-5, 5)
        ax.set_zlim3d(-5, 5)

    plt.show()

    # print(point_cloud)
    

    
    

# test_func_convex_hull()
test_func_stock()




