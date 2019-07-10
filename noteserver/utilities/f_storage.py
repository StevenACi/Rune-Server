import sys
import glob
import os

currentPath = "error"
currentPath_index = 0
files = []


def gather_images(target_dir):
    global currentPath
    global files
    global currentPath_index
    for img in glob.glob(os.getcwd() + target_dir + '*.jpg'):
        img = os.path.basename(img)
        files.append(img)
    for img in glob.glob(os.getcwd() + target_dir + '*.png'):
        img = os.path.basename(img)
        files.append(img)
    for img in glob.glob("*.bmp"):
        img = os.path.basename(img)
        files.append(img)

    for img in glob.glob(os.getcwd() + target_dir + '*.gif'):
        img = os.path.basename(img)
        files.append(img)

    currentPath = files[0]
    currentPath_index = 0

    cc_files = []
    for file in files:
        # cc_files.append("{{ url_for('static',filename='" + file + "') }}")
        cc_files.append(target_dir + file)
    return cc_files


def display(index):
    return files[index]


def isvalidfile(length, filename, ftype):
    ext = filename[length-3:]

    if (ext == "jpg") or (ext == "gif") or (ext == "bmp") or (ext == "png"):
        if ftype == "image":
            return True

    if (ext == 'txt') or (ext == 'pdf'):
        if ftype == "text":
            return True
    if ftype == "video":
        return True
    return False
