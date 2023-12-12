# AI_Asm
## Introduction
这是一个利用opencv和CNN实现的人脸识别签到系统，

## Requirements
详情见requirement.txt文件
## Usage
运行src中的index_test.py文件即可

## Structure
文件结构如下：
```
├── img         # 项目图片
│   ├── picTest
│   ├── source
├── model       # 模型文件
├── src         # 项目源码
│   ├── dataSet.py      # Dataset calss for exracting data from the model
│   ├── face_collect.py # Capture faces using the computer camera
│   ├── haarcascade_frontalface_default.xml # OpenCV face detection model
│   ├── index_test.py   # Main entry of the project
│   ├── pick_face.py    # Clip faces from images and apply necessary conversions
│   ├── read_camera.py  # Running the recognition in real time and label the face if matched
│   ├── read_data.py    # Read the source dataset directory
│   ├── read_image.py   # Read all the images under a directory into an array using OpenCV
│   ├── Test_model.py   # Running the recognition on a single photo and label the face if matched
│   ├── train_model.py  # Train the model


├── README.md
├── requirement.txt
```
### dataSet.py
数据集处理，用于读取、处理、和格式化训练数据集。这个类在初始化时会从指定路径读取数据
<br>
并执行一系列的数据预处理操作，包括数据分割、重塑、标准化和标签的one-hot编码。
<br>
**数据读取与分割 (extract_data 方法):**
<br>
从指定路径读取数据,
使用 **train_test_split** 从 scikit-learn 库随机分割数据为训练集和测试集。
<br>
**数据格式化和标准化:**
<br>
将图片数据重塑为指定格式（基于 theano 或 tensorflow 的 backend 需要不同的数据格式）。
<br>
将数据标准化为 [0, 1] 的范围。
<br>
**标签的 One-hot 编码:**
将标签转换为 one-hot 编码格式，适用于多类别的分类问题。
<br>
**数据检查 (check 方法):**
提供一种方法来检查处理后数据的维度、形状和大小。
### face_collect.py
采集人脸，将采集到的人脸图片保存到dataset文件夹中
<br>
**初始化摄像头:**
使用 cv2.VideoCapture(0) 初始化摄像头。0 表示默认的摄像头。
<br>
**检查摄像头是否打开:**
通过 cap.isOpened() 检查摄像头是否成功打开。
<br>
**捕捉和保存帧 (take_photo 函数):**
<br>
1.循环捕捉摄像头的每一帧。
<br>
2.将每一帧保存为JPEG格式的图片到指定目录。
<br>
3.在每一帧上添加文本（如帧计数）。
<br>
4.在窗口中显示当前帧。
5.在捕获100帧后停止，或者当用户按下'q'键时停止。
<br>
**释放资源:**
关闭摄像头和销毁所有OpenCV创建的窗口。
### haarcascade_frontalface_default.xml
opencv人脸检测模型
### index_test.py
主程序
### pick_face.py
人脸检测，将摄像头中的人脸检测出来
### read_camera.py
读取摄像头
### read_data.py
读取数据
### read_image.py
读取图片
### Test_model.py
测试模型
### train_model.py
训练模型

## _About Author

>Men Zhaolin
>Qi Yujun 
>Li Xingchen
>Zhang Zhou
>Yang Yifan
>
>All from Xiamen University Malaysia 
>

