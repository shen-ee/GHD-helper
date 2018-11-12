# -*- coding: utf-8 -*-
"""
Created on Thursday, 2018/10/30
This script is to convert the YOLO txt output of frames to useful, structed data.

@author: Yuning Zhu
Email: zhuyunin@gmail.com
"""

import os
from os import walk, getcwd
from PIL import Image
from shutil import copyfile
import argparse

classes = ["stump_gunner", "snowflake", "tesla", "laser", "dj", "teleport", "tina", "petey", "compy", "bruno", "red_boss", "Bomb"]
monster_classes = ["tina", "petey", "compy", "bruno", "red_boss"]
tower_classes = ["stump_gunner", "snowflake", "tesla", "laser", "dj", "teleport"]
power_tower = {"stump_gunner":1, "snowflake":1.5, "tesla":2, "laser":2, "dj":2.5, "teleport":1.3}
power_monster = {"tina":1, "petey":0.5, "compy":0.5, "bruno":2, "red_boss":5}
""" Configure Paths"""   
parser = argparse.ArgumentParser(description="REPLACE WITH DESCRIPTION",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--inputpath", "-i", type=str, default = "data/1-17/" ,help="raw input file")
parser.add_argument("--outputpath", "-o", type=str, default = "data/1-17/" ,help="raw input file")
try:
    args = parser.parse_args()
except IOError as msg:
    parser.error(str(msg))
# wd = getcwd()


mypath = args.inputpath
outpath = args.outputpath
outfile = "data.csv"
outfile2 = "number_t_m.csv"
outfile3 = "power_t_m.csv"

""" Get input text file list """
def asce(x,y):
    if int(x.split("_")[1].split(".")[0]) > int(y.split("_")[1].split(".")[0]):
        return 1
    if int(x.split("_")[1].split(".")[0]) < int(y.split("_")[1].split(".")[0]):
        return -1
    return 0
    
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
print "Input texts include:"
txt_name_list.sort(asce)
print  txt_name_list

""" Process """
with open(outpath+outfile, "w") as p:
    for k in classes[:-1]:
        p.write(k+",")
    p.write(classes[-1]+"\n")

with open(outpath+outfile2, "w") as p:
    p.write("tower,monster\n")

with open(outpath+outfile3, "w") as p:
    p.write("power_of_tower,power_of_monster\n")

for txt_name in txt_name_list:    
    """ Open input text files """
    txt_path = mypath + txt_name
    with open(txt_path, 'r') as f:
        cnt_dic = {}
        cnt_tower = 0
        cnt_monster = 0
        cnt_tower_power = 0
        cnt_monster_power = 0
        for c in classes:
            cnt_dic[c] = 0
        for lines in f:
            elems = lines.split(",")[0][1:].strip("\'")
            print elems
            cnt_dic[elems]+=1
            if elems in monster_classes:
                cnt_monster += 1
                cnt_monster_power += power_monster[elems] 
            if elems in tower_classes:
                cnt_tower += 1
                cnt_tower_power += power_tower[elems] 

        # print cnt_dic

        with open(outpath+outfile, "a") as p:
            for k in classes[:-1]:
                p.write(str(cnt_dic[k]) + ",")
            p.write(str(cnt_dic[classes[-1]]) + "\n")
        with open(outpath+outfile2, "a") as p:
            p.write(str(cnt_tower) + ","+ str(cnt_monster) + "\n")
        with open(outpath+outfile3, "a") as p:
            p.write(str(cnt_tower_power) + ","+ str(cnt_monster_power) + "\n")   
