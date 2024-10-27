import cv2 as cv

img = cv.imread("image2.jpg", cv.IMREAD_ANYCOLOR)

zoom_value = int(input("enter zoom value: "))

def zoom(img, zoom_factor=1.5):
    return cv.resize(img, None, fx=zoom_factor, fy=zoom_factor)

height, width = img.shape[:2]

zoomed = zoom(img, zoom_value)

cv.imshow("image", zoomed)
cv.waitKey(0)
