#!/bin/python

import os, shutil, string

path = "/mnt/data/tt/collect-test/pc/"
extentions = (".jpg", ".jpeg", ".JPG")

# Delete all jpg in path folder
filelist = [ f for f in os.listdir(path) if f.endswith(".jpg")]
for f in filelist:
    os.remove(path + f)
    print "Remove: " + f

# Delete all JPG in path folder
filelist = [ f for f in os.listdir(path) if f.endswith(".JPG")]
for f in filelist:
    os.remove(path + f)
    print "Remove: " + f

# Sort file names with path
file_list = os.listdir(path + "or")
full_list = [os.path.join(path + "or", i) for i in file_list]
time_sorted_list = sorted(full_list, key = os.path.getmtime)
# print time_sorted_list

# Only file names
sorted_filename_list = [os.path.basename(i) for i in time_sorted_list]
# print sorted_filename_list

# Rename files and copy
sourcedir = path + "or"
number_digits = 5
extentions = (".jpg", ".jpeg", ".JPG")
count = 0

for item in sorted_filename_list:
    if item.endswith(extentions):
      name = item.split(".")
      count = count + 1

      n = "_" + string.zfill(count,5) + ".jpg"
      # newname = item + n
      newname = "img" + n
      print newname

      # shutil.copy(sourcedir + "/" + item, path + newname)

      # Run bash
      # convert = "convert " + path + newname + " -resize 1920x1060 " + path + newname
      # print convert
      # os.system(convert)
      #



cmd = 'ls -al'
# os.system(cmd)






