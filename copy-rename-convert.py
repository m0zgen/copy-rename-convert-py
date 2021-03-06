#!/bin/python

import os, shutil, string
from PIL import Image # pip install Pillow
from multiprocessing import Pool
# from threading import Thread
import threading

SIZE = (1920, 1060)

# Path to converted images and videos
path = "/mnt/data/tt/collect-test/pc/"

# Path to original source images
sourcedir = path + "or"

extentions = (".jpg", ".jpeg", ".JPG")

pool = Pool()

# Sort file names with path contains original images
file_list = os.listdir(sourcedir)
full_list = [os.path.join(sourcedir, i) for i in file_list]
time_sorted_list = sorted(full_list, key = os.path.getmtime)
# print time_sorted_list

# Sort only file names (without path to file)
sorted_filename_list = [os.path.basename(i) for i in time_sorted_list]
# print sorted_filename_list

def remove(f):
  os.remove(f)
  # print "Remove: " + file

# Remove renamed files from "path" folder
def removeFiles():

  # Delete all jpg / JPG in path folder
  files = os.listdir(path)
  for file in files:
    if file.endswith(extentions):
      # os.remove(path + file)
      # print "Remove: " + file
      t = threading.Thread(target=remove, args=(path + file,))
      t.start()
      t.join()



def cc(n):
  convert = "convert " + n + " -resize 1920x1060 " + n
  os.system(convert)

def renameAndConvert():

  # Counting
  number_digits = 5
  count = 0

  # Rename files and copy to "path"
  for item in sorted_filename_list:
      if item.endswith(extentions):
        name = item.split(".")
        count = count + 1

        n = "_" + string.zfill(count,5) + ".jpg"
        # newname = item + n
        newname = "img" + n
        print newname

        shutil.copy(sourcedir + "/" + item, path + newname)

        # t = Thread(target=cc, args=(path + newname,))
        # t.start()
        # t.join()


        # Run bash
        convert = "convert " + path + newname + " -resize 1920x1060 " + path + newname
        # print convert
        os.system(convert)
        #

removeFiles()
# renameAndConvert()
#
#
threads = []
t = threading.Thread(target=renameAndConvert, args=())

threads.append(t)
t.start()
# t.join()















cmd = 'ls -al'
# os.system(cmd)






