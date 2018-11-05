#!/usr/bin/python3.6

import os 
from graph_class import Graph_Frame
from graph_class import Graph

#START OF PROGRAM#



os.chdir(r"/usr/local/RVMD/Python_Scripts/Graph_Gen/GenCh0/")



##
#CREATE GRAPH FRAME OBJECTS THAT WILL STORE THE GRAPH OBJECTS
##

frame_0 = Graph_Frame(r'/usr/local/RVMD/GUI/Ch0_Graphs/')
frame_1 = Graph_Frame(r'/usr/local/RVMD/GUI/Ch1_Graphs/')
frame_2 = Graph_Frame(r'/usr/local/RVMD/GUI/Ch2_Graphs/')
frame_3 = Graph_Frame(r'/usr/local/RVMD/GUI/Ch3_Graphs/')


#graph_X = Graph(ID, *kwargs)

##
#CREATE GRAPH OBJECTS FOR FRAME_0
##

graph_1_f0 = Graph('Ch0_AVG',has_cbar=True,has_gradient=True)
graph_2_f0 = Graph('Ch0_AVG',has_cbar=True,has_gradient=True)
graph_3_f0 = Graph('Ch0_AVG',has_cbar=True,has_gradient=True)
graph_4_f0 = Graph('Ch0_AVG',has_cbar=True,has_gradient=True)

graph_5_f0 = Graph('Ch0_LOOSE',fill_color='lightsteelblue')
graph_6_f0 = Graph('Ch0_LOOSE',fill_color='lightsteelblue')
graph_7_f0 = Graph('Ch0_LOOSE',fill_color='lightsteelblue')
graph_8_f0 = Graph('Ch0_LOOSE',fill_color='lightsteelblue')

graph_9_f0 = Graph('Ch0_MISA',fill_color='lightsteelblue')
graph_10_f0 = Graph('Ch0_MISA',fill_color='lightsteelblue')
graph_11_f0 = Graph('Ch0_MISA',fill_color='lightsteelblue')
graph_12_f0 = Graph('Ch0_MISA',fill_color='lightsteelblue')

graph_13_f0 = Graph('Ch0_BEAR',fill_color='lightsteelblue')
graph_14_f0 = Graph('Ch0_BEAR',fill_color='lightsteelblue')
graph_15_f0 = Graph('Ch0_BEAR',fill_color='lightsteelblue')
graph_16_f0 = Graph('Ch0_BEAR',fill_color='lightsteelblue')

graph_17_f0 = Graph('Ch0_GEARS',fill_color='lightsteelblue')
graph_18_f0 = Graph('Ch0_GEARS',fill_color='lightsteelblue')
graph_19_f0 = Graph('Ch0_GEARS',fill_color='lightsteelblue')
graph_20_f0 = Graph('Ch0_GEARS',fill_color='lightsteelblue')

graph_21_f0 = Graph('Ch0_OTHER',fill_color='lightsteelblue')
graph_22_f0 = Graph('Ch0_OTHER',fill_color='lightsteelblue')
graph_23_f0 = Graph('Ch0_OTHER',fill_color='lightsteelblue')
graph_24_f0 = Graph('Ch0_OTHER',fill_color='lightsteelblue')

##
#CREATE GRAPH OBJECTS FOR FRAME_1
##

graph_1_f1 = Graph('Ch1AVG',has_cbar=True,has_gradient=True)
graph_2_f1 = Graph('Ch1_AVG',has_cbar=True,has_gradient=True)
graph_3_f1 = Graph('Ch1_AVG',has_cbar=True,has_gradient=True)
graph_4_f1 = Graph('Ch1_AVG',has_cbar=True,has_gradient=True)

graph_5_f1 = Graph('Ch1_LOOSE',fill_color='lightsteelblue')
graph_6_f1 = Graph('Ch1_LOOSE',fill_color='lightsteelblue')
graph_7_f1 = Graph('Ch1_LOOSE',fill_color='lightsteelblue')
graph_8_f1 = Graph('Ch1_LOOSE',fill_color='lightsteelblue')

graph_9_f1 = Graph('Ch1_MISA',fill_color='lightsteelblue')
graph_10_f1 = Graph('Ch1_MISA',fill_color='lightsteelblue')
graph_11_f1 = Graph('Ch1_MISA',fill_color='lightsteelblue')
graph_12_f1 = Graph('Ch1_MISA',fill_color='lightsteelblue')

graph_13_f1 = Graph('Ch1_BEAR',fill_color='lightsteelblue')
graph_14_f1 = Graph('Ch1_BEAR',fill_color='lightsteelblue')
graph_15_f1 = Graph('Ch1_BEAR',fill_color='lightsteelblue')
graph_16_f1 = Graph('Ch1_BEAR',fill_color='lightsteelblue')

graph_17_f1 = Graph('Ch1_GEARS',fill_color='lightsteelblue')
graph_18_f1 = Graph('Ch1_GEARS',fill_color='lightsteelblue')
graph_19_f1 = Graph('Ch1_GEARS',fill_color='lightsteelblue')
graph_20_f1 = Graph('Ch1_GEARS',fill_color='lightsteelblue')

graph_21_f1 = Graph('Ch1_OTHER',fill_color='lightsteelblue')
graph_22_f1 = Graph('Ch1_OTHER',fill_color='lightsteelblue')
graph_23_f1 = Graph('Ch1_OTHER',fill_color='lightsteelblue')
graph_24_f1 = Graph('Ch1_OTHER',fill_color='lightsteelblue')

##
#CREATE GRAPH OBJECTS FOR FRAME_2
##

graph_1_f2 = Graph('Ch2_AVG',has_cbar=True,has_gradient=True)
graph_2_f2 = Graph('Ch2_AVG',has_cbar=True,has_gradient=True)
graph_3_f2 = Graph('Ch2_AVG',has_cbar=True,has_gradient=True)
graph_4_f2 = Graph('Ch2_AVG',has_cbar=True,has_gradient=True)

graph_5_f2 = Graph('Ch2_LOOSE',fill_color='lightsteelblue')
graph_6_f2 = Graph('Ch2_LOOSE',fill_color='lightsteelblue')
graph_7_f2 = Graph('Ch2_LOOSE',fill_color='lightsteelblue')
graph_8_f2 = Graph('Ch2_LOOSE',fill_color='lightsteelblue')

graph_9_f2 = Graph('Ch2_MISA',fill_color='lightsteelblue')
graph_10_f2 = Graph('Ch2_MISA',fill_color='lightsteelblue')
graph_11_f2 = Graph('Ch2_MISA',fill_color='lightsteelblue')
graph_12_f2 = Graph('Ch2_MISA',fill_color='lightsteelblue')

graph_13_f2 = Graph('Ch2_BEAR',fill_color='lightsteelblue')
graph_14_f2 = Graph('Ch2_BEAR',fill_color='lightsteelblue')
graph_15_f2 = Graph('Ch2_BEAR',fill_color='lightsteelblue')
graph_16_f2 = Graph('Ch2_BEAR',fill_color='lightsteelblue')

graph_17_f2 = Graph('Ch2_GEARS',fill_color='lightsteelblue')
graph_18_f2 = Graph('Ch2_GEARS',fill_color='lightsteelblue')
graph_19_f2 = Graph('Ch2_GEARS',fill_color='lightsteelblue')
graph_20_f2 = Graph('Ch2_GEARS',fill_color='lightsteelblue')

graph_21_f2 = Graph('Ch2_OTHER',fill_color='lightsteelblue')
graph_22_f2 = Graph('Ch2_OTHER',fill_color='lightsteelblue')
graph_23_f2 = Graph('Ch2_OTHER',fill_color='lightsteelblue')
graph_24_f2 = Graph('Ch2_OTHER',fill_color='lightsteelblue')

##
#CREATE GRAPH OBJECTS FOR FRAME_3
##

graph_1_f3 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)
graph_2_f3 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)
graph_3_f3 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)
graph_4_f3 = Graph('Ch3_AVG',has_cbar=True,has_gradient=True)

graph_5_f3 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')
graph_6_f3 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')
graph_7_f3 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')
graph_8_f3 = Graph('Ch3_LOOSE',fill_color='lightsteelblue')

graph_9_f3 = Graph('Ch3_MISA',fill_color='lightsteelblue')
graph_10_f3 = Graph('Ch3_MISA',fill_color='lightsteelblue')
graph_11_f3 = Graph('Ch3_MISA',fill_color='lightsteelblue')
graph_12_f3 = Graph('Ch3_MISA',fill_color='lightsteelblue')

graph_13_f3 = Graph('Ch3_BEAR',fill_color='lightsteelblue')
graph_14_f3 = Graph('Ch3_BEAR',fill_color='lightsteelblue')
graph_15_f3 = Graph('Ch3_BEAR',fill_color='lightsteelblue')
graph_16_f3 = Graph('Ch3_BEAR',fill_color='lightsteelblue')

graph_17_f3 = Graph('Ch3_GEARS',fill_color='lightsteelblue')
graph_18_f3 = Graph('Ch3_GEARS',fill_color='lightsteelblue')
graph_19_f3 = Graph('Ch3_GEARS',fill_color='lightsteelblue')
graph_20_f3 = Graph('Ch3_GEARS',fill_color='lightsteelblue')

graph_21_f3 = Graph('Ch3_OTHER',fill_color='lightsteelblue')
graph_22_f3 = Graph('Ch3_OTHER',fill_color='lightsteelblue')
graph_23_f3 = Graph('Ch3_OTHER',fill_color='lightsteelblue')
graph_24_f3 = Graph('Ch3_OTHER',fill_color='lightsteelblue')

##
#READ THE COLLECTED DATA FROM THE MASTER FILE AND WRITE
#IT INTO ITS RESPECTIVE GRAPH
##

graph_1_f0.read_file('master_mem.txt',0,7,7)
graph_2_f0.read_file('master_mem.txt',0,7,31)
graph_3_f0.read_file('master_mem.txt',0,7,93)
graph_4_f0.read_file('master_mem.txt',0,7,186)

graph_5_f0.read_file('master_mem.txt',2,7,7)
graph_6_f0.read_file('master_mem.txt',2,7,31)
graph_7_f0.read_file('master_mem.txt',2,7,93)
graph_8_f0.read_file('master_mem.txt',2,7,186)

graph_9_f0.read_file('master_mem.txt',3,7,7)
graph_10_f0.read_file('master_mem.txt',3,7,31)
graph_11_f0.read_file('master_mem.txt',3,7,93)
graph_12_f0.read_file('master_mem.txt',3,7,186)

graph_13_f0.read_file('master_mem.txt',4,7,7)
graph_14_f0.read_file('master_mem.txt',4,7,31)
graph_15_f0.read_file('master_mem.txt',4,7,93)
graph_16_f0.read_file('master_mem.txt',4,7,186)

graph_17_f0.read_file('master_mem.txt',5,7,7)
graph_18_f0.read_file('master_mem.txt',5,7,31)
graph_19_f0.read_file('master_mem.txt',5,7,93)
graph_20_f0.read_file('master_mem.txt',5,7,186)

graph_21_f0.read_file('master_mem.txt',6,7,7)
graph_22_f0.read_file('master_mem.txt',6,7,31)
graph_23_f0.read_file('master_mem.txt',6,7,93)
graph_24_f0.read_file('master_mem.txt',6,7,186)



graph_1_f1.read_file('master_mem.txt',0,7,7)
graph_2_f1.read_file('master_mem.txt',0,7,31)
graph_3_f1.read_file('master_mem.txt',0,7,93)
graph_4_f1.read_file('master_mem.txt',0,7,186)

graph_5_f1.read_file('master_mem.txt',2,7,7)
graph_6_f1.read_file('master_mem.txt',2,7,31)
graph_7_f1.read_file('master_mem.txt',2,7,93)
graph_8_f1.read_file('master_mem.txt',2,7,186)

graph_9_f1.read_file('master_mem.txt',3,7,7)
graph_10_f1.read_file('master_mem.txt',3,7,31)
graph_11_f1.read_file('master_mem.txt',3,7,93)
graph_12_f1.read_file('master_mem.txt',3,7,186)

graph_13_f1.read_file('master_mem.txt',4,7,7)
graph_14_f1.read_file('master_mem.txt',4,7,31)
graph_15_f1.read_file('master_mem.txt',4,7,93)
graph_16_f1.read_file('master_mem.txt',4,7,186)

graph_17_f1.read_file('master_mem.txt',5,7,7)
graph_18_f1.read_file('master_mem.txt',5,7,31)
graph_19_f1.read_file('master_mem.txt',5,7,93)
graph_20_f1.read_file('master_mem.txt',5,7,186)

graph_21_f1.read_file('master_mem.txt',6,7,7)
graph_22_f1.read_file('master_mem.txt',6,7,31)
graph_23_f1.read_file('master_mem.txt',6,7,93)
graph_24_f1.read_file('master_mem.txt',6,7,186)



graph_1_f2.read_file('master_mem.txt',0,7,7)
graph_2_f2.read_file('master_mem.txt',0,7,31)
graph_3_f2.read_file('master_mem.txt',0,7,93)
graph_4_f2.read_file('master_mem.txt',0,7,186)

graph_5_f2.read_file('master_mem.txt',2,7,7)
graph_6_f2.read_file('master_mem.txt',2,7,31)
graph_7_f2.read_file('master_mem.txt',2,7,93)
graph_8_f2.read_file('master_mem.txt',2,7,186)

graph_9_f2.read_file('master_mem.txt',3,7,7)
graph_10_f2.read_file('master_mem.txt',3,7,31)
graph_11_f2.read_file('master_mem.txt',3,7,93)
graph_12_f2.read_file('master_mem.txt',3,7,186)

graph_13_f2.read_file('master_mem.txt',4,7,7)
graph_14_f2.read_file('master_mem.txt',4,7,31)
graph_15_f2.read_file('master_mem.txt',4,7,93)
graph_16_f2.read_file('master_mem.txt',4,7,186)

graph_17_f2.read_file('master_mem.txt',5,7,7)
graph_18_f2.read_file('master_mem.txt',5,7,31)
graph_19_f2.read_file('master_mem.txt',5,7,93)
graph_20_f2.read_file('master_mem.txt',5,7,186)

graph_21_f2.read_file('master_mem.txt',6,7,7)
graph_22_f2.read_file('master_mem.txt',6,7,31)
graph_23_f2.read_file('master_mem.txt',6,7,93)
graph_24_f2.read_file('master_mem.txt',6,7,186)



graph_1_f3.read_file('master_mem.txt',0,7,7)
graph_2_f3.read_file('master_mem.txt',0,7,31)
graph_3_f3.read_file('master_mem.txt',0,7,93)
graph_4_f3.read_file('master_mem.txt',0,7,186)

graph_5_f3.read_file('master_mem.txt',2,7,7)
graph_6_f3.read_file('master_mem.txt',2,7,31)
graph_7_f3.read_file('master_mem.txt',2,7,93)
graph_8_f3.read_file('master_mem.txt',2,7,186)

graph_9_f3.read_file('master_mem.txt',3,7,7)
graph_10_f3.read_file('master_mem.txt',3,7,31)
graph_11_f3.read_file('master_mem.txt',3,7,93)
graph_12_f3.read_file('master_mem.txt',3,7,186)

graph_13_f3.read_file('master_mem.txt',4,7,7)
graph_14_f3.read_file('master_mem.txt',4,7,31)
graph_15_f3.read_file('master_mem.txt',4,7,93)
graph_16_f3.read_file('master_mem.txt',4,7,186)

graph_17_f3.read_file('master_mem.txt',5,7,7)
graph_18_f3.read_file('master_mem.txt',5,7,31)
graph_19_f3.read_file('master_mem.txt',5,7,93)
graph_20_f3.read_file('master_mem.txt',5,7,186)

graph_21_f3.read_file('master_mem.txt',6,7,7)
graph_22_f3.read_file('master_mem.txt',6,7,31)
graph_23_f3.read_file('master_mem.txt',6,7,93)
graph_24_f3.read_file('master_mem.txt',6,7,186)

##
#ADD EACH GRAPH TO THEIR RESPECTIVE FRAMES
##

frame_0.add_graph(graph_1_f0)
frame_0.add_graph(graph_2_f0)
frame_0.add_graph(graph_3_f0)
frame_0.add_graph(graph_4_f0)
frame_0.add_graph(graph_5_f0)
frame_0.add_graph(graph_6_f0)
frame_0.add_graph(graph_7_f0)
frame_0.add_graph(graph_8_f0)
frame_0.add_graph(graph_9_f0)
frame_0.add_graph(graph_10_f0)
frame_0.add_graph(graph_11_f0)
frame_0.add_graph(graph_12_f0)
frame_0.add_graph(graph_13_f0)
frame_0.add_graph(graph_14_f0)
frame_0.add_graph(graph_15_f0)
frame_0.add_graph(graph_16_f0)
frame_0.add_graph(graph_17_f0)
frame_0.add_graph(graph_18_f0)
frame_0.add_graph(graph_19_f0)
frame_0.add_graph(graph_20_f0)
frame_0.add_graph(graph_21_f0)
frame_0.add_graph(graph_22_f0)
frame_0.add_graph(graph_23_f0)
frame_0.add_graph(graph_24_f0)


frame_1.add_graph(graph_1_f1)
frame_1.add_graph(graph_2_f1)
frame_1.add_graph(graph_3_f1)
frame_1.add_graph(graph_4_f1)
frame_1.add_graph(graph_5_f1)
frame_1.add_graph(graph_6_f1)
frame_1.add_graph(graph_7_f1)
frame_1.add_graph(graph_8_f1)
frame_1.add_graph(graph_9_f1)
frame_1.add_graph(graph_10_f1)
frame_1.add_graph(graph_11_f1)
frame_1.add_graph(graph_12_f1)
frame_1.add_graph(graph_13_f1)
frame_1.add_graph(graph_14_f1)
frame_1.add_graph(graph_15_f1)
frame_1.add_graph(graph_16_f1)
frame_1.add_graph(graph_17_f1)
frame_1.add_graph(graph_18_f1)
frame_1.add_graph(graph_19_f1)
frame_1.add_graph(graph_20_f1)
frame_1.add_graph(graph_21_f1)
frame_1.add_graph(graph_22_f1)
frame_1.add_graph(graph_23_f1)
frame_1.add_graph(graph_24_f1)


frame_2.add_graph(graph_1_f2)
frame_2.add_graph(graph_2_f2)
frame_2.add_graph(graph_3_f2)
frame_2.add_graph(graph_4_f2)
frame_2.add_graph(graph_5_f2)
frame_2.add_graph(graph_6_f2)
frame_2.add_graph(graph_7_f2)
frame_2.add_graph(graph_8_f2)
frame_2.add_graph(graph_9_f2)
frame_2.add_graph(graph_10_f2)
frame_2.add_graph(graph_11_f2)
frame_2.add_graph(graph_12_f2)
frame_2.add_graph(graph_13_f2)
frame_2.add_graph(graph_14_f2)
frame_2.add_graph(graph_15_f2)
frame_2.add_graph(graph_16_f2)
frame_2.add_graph(graph_17_f2)
frame_2.add_graph(graph_18_f2)
frame_2.add_graph(graph_19_f2)
frame_2.add_graph(graph_20_f2)
frame_2.add_graph(graph_21_f2)
frame_2.add_graph(graph_22_f2)
frame_2.add_graph(graph_23_f2)
frame_2.add_graph(graph_24_f2)


frame_3.add_graph(graph_1_f3)
frame_3.add_graph(graph_2_f3)
frame_3.add_graph(graph_3_f3)
frame_3.add_graph(graph_4_f3)
frame_3.add_graph(graph_5_f3)
frame_3.add_graph(graph_6_f3)
frame_3.add_graph(graph_7_f3)
frame_3.add_graph(graph_8_f3)
frame_3.add_graph(graph_9_f3)
frame_3.add_graph(graph_10_f3)
frame_3.add_graph(graph_11_f3)
frame_3.add_graph(graph_12_f3)
frame_3.add_graph(graph_13_f3)
frame_3.add_graph(graph_14_f3)
frame_3.add_graph(graph_15_f3)
frame_3.add_graph(graph_16_f3)
frame_3.add_graph(graph_17_f3)
frame_3.add_graph(graph_18_f3)
frame_3.add_graph(graph_19_f3)
frame_3.add_graph(graph_20_f3)
frame_3.add_graph(graph_21_f3)
frame_3.add_graph(graph_22_f3)
frame_3.add_graph(graph_23_f3)
frame_3.add_graph(graph_24_f3)

##
#BUILD THE COLOUR MAPS FOR ALL OF THE GRAPHS IN EACH GRAPH FRAME
#
#FINALLY, BUILD THE GRAPHS (this will save them to their predefined storage directories)
##

frame_0.build_colormaps()
frame_0.build_graphs()

frame_1.build_colormaps()
frame_1.build_graphs()

frame_2.build_colormaps()
frame_2.build_graphs()

frame_3.build_colormaps()
frame_3.build_graphs()

#END OF PROGRAM#









