__author__ = "Men Zhaolin,Zhang Zhou,Qi Yujun,Li Xingchen,Yang Yifan"
__copyright__ = "Copyright 2023, XiamenUniversity"

import cv2
from train_model import Model
from read_data import read_name_list


class Camera_reader(object):
    IMG_SIZE = 128
    PROB_THRESHOLD = 0.7

    # 在初始化camera的时候建立模型，并加载已经训练好的模型
    def __init__(self):
        self.model = Model()
        self.model.load()

    def build_camera(self):
        # opencv文件中人脸级联文件的位置，用于帮助识别图像或者视频流中的人脸
        global result
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # 读取dataset数据集下的子文件夹名称
        name_list = read_name_list('../img/picTest')
        # 记录识别人脸的次数
        counter = 0
        # 记录识别的人脸记录
        result_list = []
        # 打开摄像头并开始读取画面
        cameraCapture = cv2.VideoCapture(0)
        success, frame = cameraCapture.read()
        while success and cv2.waitKey(1) == -1:
            success, frame = cameraCapture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 图像灰化
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 识别人脸
            for (x, y, w, h) in faces:
                if x < 0 or y < 0 or w <= 0 or h <= 0 or (x + w) > gray.shape[1] or (y + h) > gray.shape[0]:
                    continue
                ROI = gray[y:y + h, x:x + w]
                if ROI.size == 0:
                    continue
                ROI = cv2.resize(ROI, (self.IMG_SIZE, self.IMG_SIZE), interpolation=cv2.INTER_LINEAR)
                label, prob = self.model.predict(ROI)  # 利用模型对cv2识别出的人脸进行比对
                if prob > self.PROB_THRESHOLD:  # 如果模型认为概率高于70%则显示为模型中已有的label
                    show_name = name_list[label]
                else:
                    show_name = 'Stranger'
                cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # 显示名字
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 在人脸区域画一个正方形出来
                result_list.append(show_name)
                counter += 1
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 键退出
                break
            if counter >= 30:
                break
        for i in range(0, counter):
            result = max(set(result_list), key=result_list.count)
        cameraCapture.release()
        cv2.destroyAllWindows()
        return result

# if __name__ == '__main__':
#     camera = Camera_reader()
#     result = camera.build_camera()
#     print(result)
