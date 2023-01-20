import cv2
# для работы с видеокамерой
cap =cv2.VideoCapture(0)
while True:
    success, frame = cap.read() # ловим кадры видео
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):  # через 1 милисек обновляется кадр
        break                             # и по клавише q выходим