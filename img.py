import cv2 as cv
import numpy as np
import sys
import random

print(cv.__version__)

# load an img
# ----------------------------------------------------------
'''
Mat cv::imread	(	const String & 	filename,
    int 	flags = IMREAD_COLOR 
    )		
Python:
    cv.imread(	filename[, flags]	) ->	retval
'''
img = cv.imread('img/tiger.jpeg', 1)
if img is None:
    sys.exit("Could not read the image.")

# img representation
# ----------------------------------------------------------
print(img)
print("numpy => ", type(img))
print("rows (height) - columns (width) - channels (colors/pixels)", img.shape)

# resize img before opening
# ----------------------------------------------------------
'''
void cv::resize	(	InputArray 	src,
    OutputArray 	dst,
    Size 	dsize,
    double 	fx = 0,
    double 	fy = 0,
    int 	interpolation = INTER_LINEAR 
    )		
Python:
    cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	) ->	dst
'''
img = cv.resize(img, (0, 0), fx=1, fy=1)

# rotate and img
# ----------------------------------------------------------
'''
void cv::rotate	(	InputArray 	src,
    OutputArray 	dst,
    int 	rotateCode 
    )		
Python:
    cv.rotate(	src, rotateCode[, dst]	) ->	dst
'''
img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

# open a window with an img
# ----------------------------------------------------------
'''
void cv::imshow	(	const String & 	winname,
    InputArray 	mat 
    )		
Python:
    cv.imshow(	winname, mat	) ->	None
'''
cv.imshow("Display window", img)

# create a window
# ----------------------------------------------------------
'''
void cv::namedWindow	(	const String & 	winname,
    int 	flags = WINDOW_AUTOSIZE 
    )		
Python:
    cv.namedWindow(	winname[, flags]	) ->	None
'''
img1 = cv.imread('img/field.jpg', 2)
cv.namedWindow("windows", cv.WINDOW_AUTOSIZE)
cv.imshow("windows", img1)

# manipulate img
# ----------------------------------------------------------
'''
blue, green, red
[0, 0, 0]
'''
print("array of row 0 => ", img[0])
'''
 [175 204 219]
 [178 204 221]
 ...
 [117 160 133]
 [116 158 133]
 [119 161 136]]
'''
print("array of row 0, pixels between 0:2 => ", img[0][0:2])
'''
[[175 204 219]
[175 204 219]]
'''
print("array of row 0, pixel 2 => ", img[0][2])
'''
[178 204 221]
'''

# modify pixels (i, j) => each pixel gives an array of BGR (B, G, R)
# -------------------------------------------------------------------
'''
shape(): dimensions of the given img
The height of the image: 0.
The width of the image: 1.
The number of channel: 2.
'''
for i in range(50):
    for j in range(img.shape[1]):
        #(rows, columns, channels)
        img[i][j] = [random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)]
cv.imshow('Random Image', img)

# copy part of the image, gaps/size must be the same
# ----------------------------------------------------------
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag
cv.imshow('Copy', img)

# wait 0 seconds to close the window
# ----------------------------------------------------------
'''
int cv::waitKey	(	int 	delay = 0	)	
Python:
    cv.waitKey(	[, delay]	) ->	retval
'''
k = cv.waitKey(0)
# if it keys "p" it copies the img
if k == ord("p"):
    # save a numpy array as an image
    array = np.arange(0, 737280, 1, np.uint8)
    array = np.reshape(array, (1024, 720))
    cv.imwrite('img/file.jpeg', array)
    # copy img
    cv.imwrite("img/img_copied.png", img)
cv.destroyAllWindows()
