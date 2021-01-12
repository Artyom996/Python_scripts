import os
import time

days = 0  # Max age of file to stay, older wiil be deleted
folders = ["/home/art/Desktop/musor"]

total_deleted_size = 0  # statistika on size
total_deleted_file = 0  # statistika on file
total_deleted_dirs = 0  # statistika on dirs

nowTime = time.time()   # Get Current time in SECOND
ageTime = nowTime - 60*60*24*days   # Minus days in SECONDS

def delete_old_files(folder):
    global total_deleted_file
    global total_deleted_size
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                total_deleted_size += sizeFile
                total_deleted_file += 1
                print("deleting file: " + str(fileName))
                os.remove(fileName)

def delete_empty_dir(folder):
    global total_deleted_dirs
    empty_folders = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            total_deleted_dirs += 1
            empty_folders += 1
            print("deleting empty dir: " + str(path))
            os.rmdir(path)
    if empty_folders > 0:
        delete_empty_dir(folder)

# ==============================MAIN===============================

starttime = time.asctime()

for folder in folders:
    delete_old_files(folder)
    delete_empty_dir(folder)

finishtime = time.asctime()
print ("--------------------------------------")
print("Start time: " + str(starttime))
print("Total deleted size: " + str(int(total_deleted_size/1024/1024)) + "MB")
print("Total deleted files: " + str(total_deleted_file))
print("Total deleted folders: " + str(total_deleted_dirs))
print("Finish time: " + str(finishtime))
print("---------------EOF---------------------")
