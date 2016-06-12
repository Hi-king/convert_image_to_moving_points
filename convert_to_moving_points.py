# -*- coding: utf-8 -*-
from __future__ import print_function
import cv2
import argparse
import numpy

parser = argparse.ArgumentParser()
parser.add_argument("input_image")
args = parser.parse_args()

input_image = cv2.imread(args.input_image)




def get_image(color_image):
    gray = (255 - cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY))
    print(gray.max())
    canvas = numpy.zeros(gray.shape, gray.dtype)
    for y in xrange(gray.shape[0]):
        for x in xrange(gray.shape[1]):
            scale = 3 * float(gray[y, x]) / 255 + 0.001
            ploty = int(numpy.random.normal(y, scale=scale))
            plotx = int(numpy.random.normal(x, scale=scale))
            if(0 <= ploty < gray.shape[0] and 0 <= plotx < gray.shape[1]):
                canvas[ploty, plotx] = 255


    # cv2.imshow("test", canvas)
    # cv2.waitKey(-1)
    # exit(0)
    return cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)


def get_image_from_last(color_image, last_image):
    gray = (255 - cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY))
    print(gray.max())
    canvas = numpy.zeros(gray.shape, gray.dtype)
    for y in xrange(gray.shape[0]):
        for x in xrange(gray.shape[1]):
            diff = numpy.random.normal(0, scale=gray[y, x] + 0.001)
            last_image[y, x] = int(last_image[y, x] + diff) % 255

    # cv2.imshow("test", canvas)
    # cv2.waitKey(-1)
    # exit(0)
    return last_image

fps = 10
size = (input_image.shape[:2][::-1])
print(size)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video_writer = cv2.VideoWriter('output.mp4', fourcc, fps, size)
last_image = numpy.array(numpy.random.rand(*input_image.shape[:2])*255, dtype=numpy.uint8)
for i in xrange(30):
    last_image = get_image_from_last(input_image, last_image)
    # video_writer.write(last_image)
    video_writer.write(cv2.cvtColor(last_image, cv2.COLOR_GRAY2BGR))
video_writer.release()
