import cv2
# для работы с картинкой
img = cv2.imread('test.jpg')
# для изменения размера
img = cv2.resize(img, (700,400))
# для вывода изображения
cv2.imshow('Result', img)
# через какое время окно закроется, 0 - никогда
cv2.waitKey(0)