# -*- coding: utf-8 -*-
from __future__ import print_function

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
