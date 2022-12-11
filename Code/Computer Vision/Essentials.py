import cv2           #OpenCV
import numpy as np   #Numpy για αριθμητικές πράξεις με πίνακες

# filename = 'lena.png'
# # filename = 'sudoku.jpg'
# # filename = 'tiger.png'
# # filename = 'j.png'
#
# img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας
#
# cv2.namedWindow('original')  # Δημιουργία παραθύρου με όνομα "main"
# cv2.imshow('original', img)  # Προβολή εικόνας στο παράθυρο main
# cv2.waitKey(0)           # Διατηρεί ανοιχτό το πρόγραμμα μέχρι να πατηθεί κάτι
#
# cv2.namedWindow('blur')
# img2 = cv2.blur(img, (5, 5))
# cv2.imshow('blur', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('GaussianBlur')
# # img2 = cv2.GaussianBlur(img, (5,5), 0)
# # img2 = cv2.GaussianBlur(img, (5,5), 3)
# img2 = cv2.GaussianBlur(img, (5,5), 5)
# cv2.imshow('GaussianBlur', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('medianBlur')
# img2 = cv2.medianBlur(img,5)
# cv2.imshow('medianBlur', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('Sobel1')
# img2 = cv2.Sobel(img, cv2.CV_8UC1, 0, 1)
# cv2.imshow('Sobel1', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('Sobel2')
# img2 = cv2.Sobel(img, cv2.CV_8UC1, 1, 0)
# cv2.imshow('Sobel2', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('Sobel')
# img2 = cv2.Sobel(img, cv2.CV_8UC1, 1, 1)
# cv2.imshow('Sobel', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('Laplacian')
# img2 = cv2.Laplacian(img, cv2.CV_8UC1)
# cv2.imshow('Laplacian', img2)
# cv2.waitKey(0)
#
# cv2.namedWindow('Canny')
# img2 = cv2.Canny(img, 100, 100)
# cv2.imshow('Canny', img2)
# cv2.waitKey(0)
#
# # filter = 1/9*np.ones((3,3))
# # Or
# filter = 1/9*np.array([[1,1,1], [1,1,1], [1,1,1]])
#
# cv2.namedWindow('filter2D')
# img2 = cv2.filter2D(img, cv2.CV_8UC1, filter)
# cv2.imshow('filter2D', img2)
# cv2.waitKey(0)
#
# # ----------------------------------------------------------------------------------------
#
# filename = 'tiger.png'
# img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# cv2.namedWindow('median')
# img2 = cv2.medianBlur(img,3)
# cv2.imshow('median', img2)
# cv2.waitKey(0)
#
# # Αποθήκευση εικόνας σε αρχείο
# cv2.imwrite('tiger2.png',img2)

# ----------------------------------------------------------------------------------------
filename = 'j.png'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας

cv2.namedWindow('main', )
cv2.imshow('main', img)
cv2.waitKey(0)

scale_percent = 300
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, cv2.INTER_AREA)
print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας

cv2.namedWindow('main', )
cv2.imshow('main', img)
cv2.waitKey(0)

strel = np.ones((7,7), np.uint8)
# strel = cv2.getStructuringElement(cv2.MORPH_CROSS, (11,11))
# strel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))

# EROSION
erode = cv2.morphologyEx(img, cv2.MORPH_ERODE, strel)
cv2.namedWindow('erode', )
cv2.imshow('erode', erode)
cv2.waitKey(0)

# DILATION
dilate = cv2.morphologyEx(img, cv2.MORPH_DILATE, strel)
cv2.namedWindow('dilate', )
cv2.imshow('dilate', dilate)
cv2.waitKey(0)


# EDGE
gradient = dilate - erode
cv2.namedWindow('EDGE', )
cv2.imshow('EDGE', gradient)
cv2.waitKey(0)

strel = np.ones((15,15), np.uint8)

filename = 'opening.png'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας

scale_percent = 300
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, cv2.INTER_AREA)
print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας

cv2.namedWindow('main1', )
cv2.imshow('main1', img)
cv2.waitKey(0)

# OPENING
open = cv2.morphologyEx(img, cv2.MORPH_OPEN, strel)
cv2.namedWindow('OPENING', )
cv2.imshow('OPENING', open)
cv2.waitKey(0)



filename = 'closing.png'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας

scale_percent = 300
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, cv2.INTER_AREA)
print(img.shape)  # Τυπώνει τις διαστάσεις της εικόνας

cv2.namedWindow('main2', )
cv2.imshow('main2', img)
cv2.waitKey(0)

# CLOSING
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, strel)
cv2.namedWindow('CLOSING', )
cv2.imshow('CLOSING', close)
cv2.waitKey(0)

