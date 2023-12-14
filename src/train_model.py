__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

from dataSet import DataSet
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
import numpy as np
import matplotlib.pyplot as plt


# Building a CNN-based face recognition model
def plot_training_history(history):
    # Plotting loss values and accuracies during training
    plt.figure(figsize=(12, 4))

    # Plotting training loss values
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='loss')
    plt.title('Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # Plotting training accuracy
    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.title('Training Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.show()


class Model(object):
    FILE_PATH = "../model/model.h5"  # Where models are stored and read
    IMAGE_SIZE = 128  # The face image accepted by the model must be 128*128

    def __init__(self):
        self.model = None

    # Read the instantiated DataSet class as a data source for training.
    def read_trainData(self, dataset):
        self.dataset = dataset

    # Build a CNN model with one layer of convolution, one layer of pooling, one layer of convolution, one layer of pooling, full linking after smoothing, and finally classification
    def build_model(self):
        self.model = Sequential()
        self.model.add(
            Convolution2D(
                filters=32,
                kernel_size=(5, 5),
                padding='same',
                data_format='channels_first',  
                input_shape=self.dataset.X_train.shape[1:]
            )
        )

        self.model.add(Activation('relu'))
        self.model.add(
            MaxPooling2D(
                pool_size=(2, 2),
                strides=(2, 2),
                padding='same'
            )
        )

        # The second convolutional layer eliminates the need to specify the input shape and data format
        self.model.add(Convolution2D(filters=64, kernel_size=(5, 5), padding='same'))
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'))

        self.model.add(Flatten())
        self.model.add(Dense(512))
        self.model.add(Activation('relu'))

        self.model.add(Dense(self.dataset.num_classes))
        self.model.add(Activation('softmax'))
        self.model.summary()

    # Functions for model training, specific optimizer, loss can be different choices
    def train_model(self):
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])
        # epochs、batch_size is an adjustable parameter
        history = self.model.fit(self.dataset.X_train, self.dataset.Y_train, epochs=30, batch_size=30)
        plot_training_history(history)

    def evaluate_model(self):
        print('\nTesting---------------')
        loss, accuracy = self.model.evaluate(self.dataset.X_test, self.dataset.Y_test)

        print('test loss;', loss)
        print('test accuracy:', accuracy)

    def save(self, file_path=FILE_PATH):
        print('Model Saved.')
        self.model.save(file_path)

    def load(self, file_path=FILE_PATH):
        print('Model Loaded.')
        self.model = load_model(file_path)

    def predict(self, img):
        # Make sure that the input img is grayed out (channel=1) and has a size of IMAGE_SIZE.
        # (samples, height, width, channels)
        img = img.reshape((1, self.IMAGE_SIZE, self.IMAGE_SIZE, 1))
        img = img.astype('float32')
        img = img / 255.0

        result = self.model.predict(img)  # Measure the probability that the img belongs to a certain label
        max_index = np.argmax(result)  # Find the most probable

        return max_index, result[0][max_index]  # The first parameter is the index of the label with the highest probability, the second parameter is the corresponding probability


def train():
    dataset = DataSet('../img/picTest')
    model = Model()
    model.read_trainData(dataset)
    model.build_model()
    model.train_model()
    model.evaluate_model()
    model.save()


if __name__ == '__main__':
    train()
