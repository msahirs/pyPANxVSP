import os
from read_hrm import hrm_Reader

def create_block(data):
    
    block_name, grp_id, no_pts, \
        no_secs, points_list, config = data
    
    block =   create_rec_2_from_hrm(block_name) \
            + "\n" \
            + create_rec_3_from_hrm(grp_id,no_pts,no_secs,config) \
            + "\n" \
            + create_rec_4_from_hrm(points_list,no_pts,no_secs)
    
    return block


class writer_lawgs():

    def __init__(self, metadata_line,
            config = [0,11,11,0,0,0,0,0,0,0,1,1,1,0]) -> None:
        
        self.metadata_line = metadata_line
        self.config = config
    
    def hrm2lawgs(self,input_file,output_file):

        hrm = hrm_Reader(input_file)

        f = open(output_file, "w")

        f.write("%s\n" % (self.metadata_line,))
        
        for i in range(len(hrm.group_num)):

            block = create_block([hrm.block_names[i],
                                hrm.group_num[i],
                                hrm.points_per_sec[i],
                                hrm.sections_num[i],
                                hrm.cart_points[i],
                                self.config])
            f.write(block)

        f.close()

def create_rec_2_from_hrm(obj_name):
    
    return " '%s'" % (obj_name,)

def create_rec_3_from_hrm(grp_id,no_pts,no_secs,config):
    
    config[0] = grp_id
    config[1] = no_secs
    config[2] = no_pts

    return "    " + "    ".join([str(x) for x in config])

def create_rec_4_from_hrm(points_list,no_pts,no_secs):

    block_string = "  "
    

    for i in range(no_secs):
        for j in range(no_pts*3):
            
            float_str= f"{points_list[i*no_pts*3 + j]:.4E}"
            block_string += (float_str + "     ")
        # print(i)
            # print(j+1)
            if (j+1) % (6) == 0:
                # print("trigger_line at",i)
                block_string += ("\n" + "  ")
        
        if i < no_secs-1:
            block_string += ("\n" + "  ")
        else:
            block_string += ("\n")
            
    return block_string
        

def test_func():
    # hrm = hrm_Reader("hrm_parser/meshes/test_54.hrm")

    # head = create_rec_2_from_hrm(hrm.block_names[0])
    # print(head)
    b = writer_lawgs("Created by sahir hrm parsing tool")
    b.hrm2lawgs("utilities/hrm_parser/meshes/space_ship_fixed.hrm",
                "utilities/hrm_parser/exports/ss2_fixed.wgs")

# test_func()


# config_2 = create_rec_3_from_hrm(hrm.group_num[0],
#                             hrm.points_per_sec[0],
#                             hrm.sections_num[0],
#                             [0,11,11,0,0,0,0,0,0,0,1,1,1,1])



# fin = create_rec_4_from_hrm(hrm.cart_points[0],
#                             hrm.points_per_sec[0],
#                             hrm.sections_num[0])
    


# print(fin)