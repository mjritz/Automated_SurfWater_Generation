#Add information on script**

#!/usr/bin/env python

import os
import sys
import numpy as np


os.system('python PF.py > PF.txt' )

in_file = open('PF.txt', 'r') #Open in readable format
#Reading packing fraction file and recording the packing fraction. 
for lines in in_file.readlines():
    PF_data = (lines.split())
    PF = float(PF_data[3])


print PF

in_file_2 = open('trimmed_info.txt', 'r')
for sentence in in_file_2.readlines():
    if sentence.startswith('top'):
        info = sentence.split()
        num_surf= int(info[3])
print num_surf


os.system('python Test_Area.py > TA.txt' )

TA_in_file = open('TA.txt', 'r') #Open in readable format
#Reading packing fraction file and recording the packing fraction. 
for TA_lines in TA_in_file.readlines():
     if TA_lines.startswith('gamma'):
        TA_data = (TA_lines.split())
        TA = float(TA_data[2])
print TA 
