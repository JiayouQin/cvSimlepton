A Simple module that integrates some functions to make your life easier with openCV

**commands:**

```   
    window
    imshow          WIP, passing in on image variable name in string type, variable name will be displayed as title. Resizable window as default.
    utility
    converge        use eitehr mean or gaussian kernel to make a high pass filter, low frequency signal will be merged into mean average value of the whole histogram. 
    		    (https://github.com/JiayouQin/Python-projects/tree/master/17%20Image%20Balancing)
    list_images     return all image files in the directory including sub directories in a list
    imread          identical to openCV imread but supports UTF-8 formatted string path
    imwrite         identical to openCV imwrite but supports UTF-8 formatted string path
    open_morph      perform open operation with given kernel
    open_circle     perform open operation with circular kernel
    open_rect       perform open operation with rectangular kernel
    close_morph     perform close operation with given kernel
    close_circle    perform close operation with circular kernel
    close_rect      perform close operation with rectangular kernel
    bgr_to_hsv      convert a bgr image to hsv image, if parameter 2 is true then returned image will be split into 3 channels
    add_noise       add noise of given type to image (0:gaussian, 1:s&p), accepts both string and integer number
```


**example usage:**

show window within a class function

```python
import cv2 as cv
import cvsimpleton as cvs


class FunClass():
	def __init__(self):
		self.images = cvs.list_images('./')
		self.img = cvs.imread(self.images[0])

	def have_fun(self):
		print(self.img)
		cvs.imshow('self.img')
		k = cv.waitKey(0)

fun = FunClass()
fun.have_fun()


img  = cvs.imread(fun.images[1])
cvs.imshow('img')
cv.waitKey(0)
```

Use converge function:
'''
path = 'myOwnPath'
k_size = 15
images = cvs.list_images(path)
print(images )

for i in range(len(images)):
    image = cv.imread(images[i])
    result = cvs.converge(image,k_size)
    for name in ['image', 'result', ]:
        cvs.imshow(name)
    k = cv.waitKey(0)
    if k == 27:
        break
'''
