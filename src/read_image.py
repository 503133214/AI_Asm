__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import os
import cv2

#根据输入的文件夹绝对路径，将该文件夹下的所有指定suffix的文件读取存入一个list
#该list的第一个元素是该文件夹的名字
def read_AllImg(path,*suffix):
    try:

        s = os.listdir(path)
        resultArray = []
        fileName = os.path.basename(path)
        resultArray.append(fileName)

        for i in s:
            if i.endswith(suffix):
                document = os.path.join(path, i)
                img = cv2.imread(document)
                resultArray.append(img)
    except IOError:
        print("Error")

    else:
        print("Successfully read")
        return resultArray

