import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread('coba.jpeg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
print('Number of cars in the image is ' + str(label.count('car')))
plt.imshow(output_image)
plt.show()