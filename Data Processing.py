#!/usr/bin/env python
# coding: utf-8

# In[39]:


import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d

import os

import unicodedata

import codecs

import csv

import re
from statistics import mean 


# In[40]:


file_path = 'C:\\Users\\Schokri\\Desktop\\mocap\\rec12_data_noapp.csv' 
with open(file_path,'r') as file:
    lines = file.readlines()
    print(len(lines))
    frame_fields = re.split(',',lines[3][:-3].replace(',,,',',')) # collect the data-id's [:-3] to delete the last-\n entry
    frames = {}
    for frame in lines [6:100]: # skip the informative lines 1-5 until the frames begin 
        values = [float(x) if x!='' else 0 for x in re.split(',',frame.strip())] # empty values equal to zero for now!
        frameObj = {}
        for i, field in enumerate(frame_fields):
            frameObj[field] = values [i]
        frames[frameObj['Frame#']] = frameObj


# In[41]:


x_pos_1 =mean([frames[frame]['tobii1:c1']for frame in frames.keys()])
y_pos_1 =mean([frames[frame]['tobii1:c2']for frame in frames.keys()])
z_pos_1 =mean([frames[frame]['tobii1:c3']for frame in frames.keys()])
#w_pos_1 =mean([frames[frame]['tobii1:c4']for frame in frames.keys()])

x_pos_2 =mean([frames[frame]['tobii2:d1']for frame in frames.keys()])
y_pos_2 =mean([frames[frame]['tobii2:d2']for frame in frames.keys()])
z_pos_2 =mean([frames[frame]['tobii2:d3']for frame in frames.keys()])
#w_pos_2 =mean([frames[frame]['tobii2:d4']for frame in frames.keys()])

x_pos_3 =mean([frames[frame]['tobii3:e1']for frame in frames.keys()])
y_pos_3 =mean([frames[frame]['tobii3:e2']for frame in frames.keys()])
z_pos_3 =mean([frames[frame]['tobii3:e3']for frame in frames.keys()])
#w_pos_3 =mean([frames[frame]['tobii3:e4']for frame in frames.keys()])

x_pos = [x_pos_1,x_pos_2,x_pos_3]
y_pos = [y_pos_1,y_pos_2,y_pos_3]
z_pos = [z_pos_1,z_pos_2,z_pos_3]


# In[42]:


x_gaze_1 = [frames[frame]['g1l:l1']for frame in frames.keys()]
y_gaze_1 = [frames[frame]['g1r:l2']for frame in frames.keys()]
z_gaze_1 = [frames[frame]['g1c:l3']for frame in frames.keys()]

x_gaze_2 = [frames[frame]['g2l:m1']for frame in frames.keys()]
y_gaze_2 = [frames[frame]['g2r:m2']for frame in frames.keys()]
z_gaze_2 = [frames[frame]['g2c:m3']for frame in frames.keys()]

x_gaze_3 = [frames[frame]['g3l:n1']for frame in frames.keys()]
y_gaze_3 = [frames[frame]['g3r:n2']for frame in frames.keys()]
z_gaze_3 = [frames[frame]['g3c:n3']for frame in frames.keys()]


# In[43]:


fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.scatter3D(gaze_L_1, gaze_R_1, gaze_C_1,s=10,color ='lightblue')
ax.scatter3D(gaze_L_2, gaze_R_2, gaze_C_2,s=10,color ='lightcoral')
ax.scatter3D(gaze_L_3, gaze_R_3, gaze_C_3,s=10,color ='lightgreen')

ax.scatter3D(x_pos_1, y_pos_1, z_pos_1,s=500,color ='b')
ax.scatter3D(x_pos_2, y_pos_2, z_pos_2,s=500,color ='r')
ax.scatter3D(x_pos_3, y_pos_3, z_pos_3,s=500,color ='g')
ax.view_init(elev = 90,azim=90)


# In[ ]:




