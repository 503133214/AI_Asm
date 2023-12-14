__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

from read_data import read_file
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.utils import np_utils
import random

class DataSet(object):
    def __init__(self, path):
        self.num_classes = None
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None
        self.img_size = 128
        self.extract_data(path)

    def extract_data(self, path):
        # Read out the number of images, tags and categories according to a specified path
        imgs, labels, counter = read_file(path)

        # Disrupting the dataset into randomized groups
        X_train, X_test, y_train, y_test = train_test_split(imgs, labels, test_size=0.2, random_state=random.randint(0, 100))

        # Reformatting and standardization
        # Based on tensorflow backend，data format:(samples, height, width, channels)
        X_train = X_train.reshape(X_train.shape[0], self.img_size, self.img_size, 1) / 255.0
        X_test = X_test.reshape(X_test.shape[0], self.img_size, self.img_size, 1) / 255.0

        X_train = X_train.astype('float32')
        X_test = X_test.astype('float32')

        # Covert labels to binary class matrices
        Y_train = np_utils.to_categorical(y_train, num_classes=counter)
        Y_test = np_utils.to_categorical(y_test, num_classes=counter)

        # Assigning formatted data to class properties
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        self.num_classes = counter

    def check(self):
        print('num of dim:', self.X_test.ndim)
        print('shape:', self.X_test.shape)
        print('size:', self.X_test.size)

        print('num of dim:', self.X_train.ndim)
        print('shape:', self.X_train.shape)
        print('size:', self.X_train.size)
