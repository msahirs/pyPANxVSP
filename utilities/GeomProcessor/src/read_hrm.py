import os
import numpy as np
from volumetrics import in_hull
from matplotlib import pyplot as plt


GLOBAL_KEYS = ["NUMBER OF COMPONENTS"]

GROUP_KEYS = ["GROUP NUMBER", "TYPE",
              "CROSS SECTIONS", "PTS/CROSS SECTION"]
N_DIM = 3

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

def get_blocks(file):

    blocks = []
    line_locs = []

    fo = open(file, "r")
    fp = fo.readlines()

    line_prev = " _init"

    for i, line in enumerate(fp):
        if not line_prev[0] == " " and \
                line[0] == " " and \
                not line_prev == "\n":
            
            blocks.append(line_prev.strip())
            line_locs.append(i-1)
    
        line_prev = line

    assert len(blocks) == int(fp[2].split("=")[1].strip()), \
        "Mismatch in explicit component number field and number parsed"

    grp_num = []
    type_num = []
    sections = []
    pts_per_section = []
    cart_points = []

    for i in line_locs:

        grp_num.append(int(fp[i+1].split("=")[1].strip()))

        type_num.append(int(fp[i+2].split("=")[1].strip()))
        # print(type_num)
        # raise "Error"
        sections.append(int(fp[i+3].split("=")[1].strip()))
        # print(sections)
        # raise "Error"
        pts_per_section.append(int(fp[i+4].split("=")[1].strip()))
        # print(pts_per_section)
        # raise "Error"
        total_pts = pts_per_section[-1] * sections[-1]

        points_string = ("".join(fp[i+5 : i+5 + total_pts])).split(" ")
        # points_string = [x for x in points_string if x != '']
        # print(points_string)
        # raise "Error"
        b = list(map(str.strip, points_string))
        # print(b)
        points_float = [float(x) for x in b if x != '']
        

        assert len(points_float) == total_pts * N_DIM, \
            "Mismatch in explicit point number field and number parsed"
        
        cart_points.append(points_float)

    fo.close()

    return blocks, line_locs, grp_num, type_num, sections, pts_per_section, cart_points

class hrm_Reader():

    def __init__(self, filename) -> None:

        check_file_exists(filename)
        check_file_ext(filename)

        self.rel_path = filename

        values = get_blocks(self.rel_path)

        self.block_names = values[0]
        self.line_locs = values[1]
        self.group_num = values[2]
        self.type_num = values[3]
        self.sections_num = values[4]
        self.points_per_sec = values[5]
        self.cart_points = values[6]

        self.cart_points_np = self.get_cart_points_as_np()

        self.cull_intersects()

    def get_cart_points_as_np(self):

        np_cart_stack = []

        for i in self.cart_points:
            np_cart_pc = np.array(i).reshape(-1,3)
            np_cart_stack.append(np_cart_pc)

        return np_cart_stack
    
    def cull_intersects(self):

        tot_comp_num = len(self.block_names)
        tot_comp_num = 7

        for i in range(tot_comp_num):
            for j in range(i+1):
                if i is not j:
                    print(f'({i},{j})', end = '  ')
            print()
    
        
### TEST FUNC DEFS ###

def test_constructor():

    # print(check_file_exists("GeomParser/meshes/test_hermite.hrm"))

    # mem_file = open("GeomParser/meshes/test_hermite.hrm","r")

    # print(type(mem_file.read()))

    # print(check_file_ext("GeomParser/meshes/test_hermite.hrm", ".hrm"))

    # block = get_blocks("GeomParser/meshes/eeee.hrm")

    # print(block[0])
    # print(block[1])
    # print(block[3])

    base_path = "utilities/GeomProcessor/meshes/"
    hrm = hrm_Reader(base_path + "convex_hull_test.hrm")

def test_plot_func():

    base_path = "utilities/GeomProcessor/meshes/"
    hrm = hrm_Reader(base_path + "convex_hull_test.hrm")

    point_cloud = hrm.get_cart_points_as_np()
    fuselage = point_cloud[0]
    wing_1 = point_cloud[1]

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.scatter(fuselage[:,0],fuselage[:,1],fuselage[:,2],
               marker='o', color = 'g')

    ax.scatter(wing_1[:,0],wing_1[:,1],wing_1[:,2],
               marker='o', color = 'b')

    ax.set_xlabel('X Length')
    ax.set_ylabel('Y Length')
    ax.set_zlabel('Z Length')

    ax.set_xlim3d(-2, 8)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)

    plt.show()


# test_plot_func()
test_constructor()