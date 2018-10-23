import cv2
vidcap = cv2.VideoCapture('1-17.mp4')
success,image = vidcap.read()
count = 0

while success:
    if count % 5 == 0:
        cv2.imwrite("./1-17/frame_%d.jpg" % count, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', count)
    count += 1