import cv2
    # для работы с определением лиц
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
img = cv2.imread('face.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Для определение координат лиц
faces = face_cascades.detectMultiScale(img_gray)
    # выводим координаты 2 точек прямоугольника лица
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow('Result', img)
cv2.waitKey(0)

    # для работы с видеокамерой
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #faces = face_cascades.detectMultiScale(img_gray)

    #for (x, y, w, h) in faces:
    #    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break # через 1 милисек обновляется кадр
             # и по клавише q выходим
