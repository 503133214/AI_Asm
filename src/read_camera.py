__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import cv2
from train_model import Model
from read_data import read_name_list


class Camera_reader(object):
    IMG_SIZE = 128
    PROB_THRESHOLD = 0.7

    # Build the model when initializing the camera and load the already trained model
    def __init__(self):
        self.model = Model()
        self.model.load()

    def build_camera(self):
        # Location of the face cascade file in the opencv file, used to help recognize faces in images or video streams
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Retrieve subfolder names under dataset dataset
        name_list = read_name_list('../img/picTest')
        # Record the number of times a face is recognized
        counter = 0
        # Recording of recognized face records
        result_list = []
        # Turn on the camera and start reading the screen
        cameraCapture = cv2.VideoCapture(0)
        success, frame = cameraCapture.read()
        while success and cv2.waitKey(1) == -1:
            success, frame = cameraCapture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Graying of images
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # face recognition
            for (x, y, w, h) in faces:
                if x < 0 or y < 0 or w <= 0 or h <= 0 or (x + w) > gray.shape[1] or (y + h) > gray.shape[0]:
                    continue
                ROI = gray[y:y + h, x:x + w]
                if ROI.size == 0:
                    continue
                ROI = cv2.resize(ROI, (self.IMG_SIZE, self.IMG_SIZE), interpolation=cv2.INTER_LINEAR)
                label, prob = self.model.predict(ROI)  # Comparison of faces recognized by cv2 using models
                if prob > self.PROB_THRESHOLD:  # If the model considers the probability to be higher than 70% then it is shown as a label already in the model
                    show_name = name_list[label]
                else:
                    show_name = 'Stranger'
                cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # Show Name
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a square out of the face area
                result_list.append(show_name)
                counter += 1
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break
            if counter >= 30:
                break
        for i in range(0, counter):
            result = max(set(result_list), key=result_list.count)
        cameraCapture.release()
        cv2.destroyAllWindows()
        return result

if __name__ == '__main__':
    camera = Camera_reader()
    result = camera.build_camera()
    print(result)
