#!/bin/python

import shutil    # For CopyFile
import os        # GetFileSize and Check if File exist
import sys       # For CLi Arguments

if(len(sys.argv) < 4):
    print("mission arguments Usage ")
    exit(1)

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size
    logfile_size = logfile_size / 1024

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFILEnumber in range (logsnumber, 1, -1):
                src = file_name + "_" + str(currentFILEnumber-1)
                dst = file_name + "_" + str(currentFILEnumber)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + "   to" + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()


