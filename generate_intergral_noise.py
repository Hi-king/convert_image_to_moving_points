# -*- coding: utf-8 -*-
from __future__ import print_function
import cv2
import argparse
import numpy

parser = argparse.ArgumentParser()
parser.add_argument("input_image")
args = parser.parse_args()
input_image = cv2.imread(args.input_image)

fps = 30
size = (input_image.shape[:2][::-1])
print(size)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video_writer = cv2.VideoWriter('output.mp4', fourcc, fps, size)
last_image = numpy.array(numpy.random.rand(*input_image.shape[:2])*256, dtype=numpy.uint16)
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY).astype(numpy.uint16)






for i in xrange(300):
    video_writer.write(cv2.cvtColor(last_image.astype(numpy.uint8), cv2.COLOR_GRAY2BGR))
    last_image = (last_image + gray_image) % 256
    print(last_image.mean())
    # cv2.imwrite("test{:04d}.png".format(i), cv2.cvtColor(last_image, cv2.COLOR_GRAY2BGR))
video_writer.release()
