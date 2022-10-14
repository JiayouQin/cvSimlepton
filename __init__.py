'''
A Simple module that integrates some functions to make your life easier with openCV

commands:

    windows:
    imshow          WIP, passing in on image variable name in string type, variable name will be displayed as title. Resizable window as default.

    utility:
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

'''

from cvsimpleton.window import *
from cvsimpleton.util import *

errlog = []