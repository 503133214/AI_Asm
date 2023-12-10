import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


def take_photo(directory):
    frame_count = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Save the frame as an image file
        file_name = f"{directory}/frame_{frame_count:03}.jpg"
        cv2.imwrite(file_name, frame)
        frame_count += 1
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame, 'num:%d' % frame_count, (30, 30), font, 1, (255, 0, 255), 4)
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        if frame_count >= 100:  # Stop after 100 frames
            break
        if cv2.waitKey(1) == ord('q'):  # Quit if 'q' is pressed
            break

    cap.release()
    cv2.destroyAllWindows()


#Ensure the directory exists
# directory = "../img/dataset"
# if not os.path.exists(directory):
#     os.makedirs(directory)
#
# take_photo(directory)
