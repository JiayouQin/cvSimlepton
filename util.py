import numpy as np
import cv2 as cv
import os

def converge(image, k_size, gaussian_kernel=True):
    '''
    high pass filter via kernel convolution, low frequency signals will be merged into the average mean.
    if gaussian kernel is true then a gaussian kernel will be used, otherwise a mean kernel.
    '''
    image = image.astype(np.float32)/255
    average_color = cv.mean(image)
    if gaussian_kernel:
        blurred = cv.GaussianBlur(image,(k_size,k_size),0)
    else:
        blurred = cv.blur(image, (k_size, k_size))
    sub = blurred - average_color[:3]
    result = image - sub
    norm = cv.normalize(result, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    return norm


def imread(path, flag=1):
    '''
    read image from path into OpenCV format（numpy array）, supports UTF-8 format.
    :param path: file path
    :param flag: 0: gray scaled, 1:normal
    :return: numpy array image or None
    '''
    stream = open(path, "rb")
    byte_array = bytearray(stream.read())
    np_array = np.asarray(byte_array, dtype=np.uint8)
    bgr_image = cv.imdecode(np_array, cv.IMREAD_UNCHANGED)
    if flag == 0:
        bgr_image = cv.cvtColor(bgr_image, cv.COLOR_BGR2GRAY)
    return bgr_image


def imwrite(path, img, format='.bmp'):
    '''
    write OpenCV format image onto disk(), supports UTF-8 format.
    :param path:
    :param img:
    :return: retVal from OpenCV
    '''
    suffix = path.split('.')[-1]
    ret, im_buf_arr = cv.imencode(".jpg", img)
    im_buf_arr.tofile(path)
    return ret


def list_images(path):
    images = []
    for path, sub_dirs, files in os.walk(path):
        for name in files:
            suffix = name.split('.')[-1]
            if suffix in ['jpg','bmp','png']:
                images.append(f'{path}/{name}')
    return images


def open_morph(image, kernel, iterations=1):
    # perform open (erosion then dilation) operation
    eroded = cv.erode(image, kernel, iterations)
    dilated = cv.dilate(eroded, kernel, iterations)
    return dilated


def open_circle(image, size_x=3, size_y=0, iterations=1):
    # perform open operation using a circular kernel
    size_y = size_x if not size_y else size_y
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (size_x, size_y))
    return open_morph(image, kernel, iterations)


def open_rect(image, size_x=3, size_y=0, iterations=1):
    size_y = size_x if not size_y else size_y
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (size_x, size_y))
    return open_morph(image, kernel, iterations)


def close_morph(image, kernel, iterations=1):
    dilated = cv.dilate(image, kernel, iterations)
    eroded = cv.erode(dilated, kernel, iterations)
    return eroded


def close_circle(image, size_x=3, size_y=0, iterations=1):
    size_y = size_x if not size_y else size_y
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (size_x, size_y))
    return close_morph(image, kernel, iterations=1)


def close_rect(image, size_x=3, size_y=0, iterations=1):
    size_y = size_x if not size_y else size_y
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (size_x, size_y))
    return close_morph(image, kernel, iterations=1)


def bgr_to_hsv(image, split=False):
    # convert BGR image to HSV, split into 3 channels if variable is true
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    if not split:
        return hsv
    return cv.split(hsv)


def add_noise(image, noise_type=0):
    ref = {'gauss': 0, 's&p': 1}
    if type(noise_type) == str:
        if noise_type not in ref:
            return image
        noise_type = ref[noise_type]

    if noise_type == 0:
        row, col, c = image.shape
        mean = 0
        var = 0.1
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col, c))
        gauss = gauss.reshape(row, col, c)
        noisy = image + gauss
        return noisy

    if noise_type == 1:
        row, col, c = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coordinates = [np.random.randint(0, i - 1, int(num_salt))
                       for i in image.shape]
        out[coordinates] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coordinates = [np.random.randint(0, i - 1, int(num_pepper))
                       for i in image.shape]
        out[coordinates] = 0
        return out
