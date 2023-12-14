__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import os
import cv2
import numpy as np


# Input a file path, read the images in each folder under it, and give a different Label to each folder.
# Return a list of imgs, return a list of corresponding labels, return how many folders (how many labels) there are.

def read_file(path):
    img_list = []
    label_list = []
    dir_counter = 0
    IMG_SIZE = 128

    # Read all the jpg files in all the subfolders under the path and store them in a list.
    for child_dir in os.listdir(path):
        child_path = os.path.join(path, child_dir)

        for dir_image in os.listdir(child_path):
            if dir_image.endswith('.jpg'):
                img = cv2.imread(os.path.join(child_path, dir_image))
                resized_img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                recolored_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
                img_list.append(recolored_img)
                label_list.append(dir_counter)

        dir_counter += 1

    # The returned img_list is converted to the np.array format
    img_list = np.array(img_list)
    return img_list, label_list, dir_counter


# Read the folders of the training dataset and return their names to a list
def read_name_list(path):
    name_list = []
    for child_dir in os.listdir(path):
        name_list.append(child_dir)
    return name_list


if __name__ == '__main__':
    img_list, label_list, counter = read_file('../img/dataset')
    print(counter)
