__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import os
import cv2
import time
from read_image import read_AllImg
from read_data import read_name_list


def readPicSaveFace(sourcePath, objectPath, *suffix):
    try:
        # Read the photo, note that the first element is the filename.
        resultArray = read_AllImg(sourcePath, *suffix)

        # Check the list of images one by one, find the faces and write them to the target folder.

        count = 1
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        for i in resultArray:
            if type(i) != str:

                gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    listStr = [str(int(time.time())), str(count)]  # Timestamp and read sort as file name
                    fileName = ''.join(listStr)

                    f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
                    cv2.imwrite(objectPath + os.sep + '%s.jpg' % fileName, f)
                    count += 1

    except IOError:
        print("Error")

    else:
        print('Already read ' + str(count - 1) + ' Faces to Destination ' + objectPath)


def readPicSaveFace_Path(sourcePath, objectPath, *suffix):
    file_list = read_name_list(sourcePath)
    for file_name in file_list:
        directory = objectPath + os.sep + file_name
        if os.path.exists(directory):
            continue
        if not os.path.exists(directory):
            os.makedirs(directory)
        readPicSaveFace(sourcePath + os.sep + file_name, objectPath + os.sep + file_name, *suffix)


if __name__ == '__main__':
    readPicSaveFace_Path('../img/source', '../img/picTest', '.jpg', '.JPG', '.png', '.PNG')
