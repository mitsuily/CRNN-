import sys
sys.path.append("/root/pvc/build/install/python")

import argparse
import numpy as np
import os
import time
import sys

from collections import defaultdict
import cv2

if __name__ == '__main__':
    exts = ["jpg", "png"]

    mean = np.zeros(3)
    N = 0
    classSizes = defaultdict(int)

    beginTime = time.time()
    for subdir, dirs, files in os.walk(sys.argv[1]):
        for fName in files:
            (imageClass, imageName) = (os.path.basename(subdir), fName)
            if any(imageName.lower().endswith("." + ext) for ext in exts):
                img = cv2.imread(os.path.join(subdir, fName)) # io.imread(os.path.join(subdir, fName))
                img = cv2.resize(img, (280, 32))
                if True:
                    mean[0] += np.sum(img[:, :, 0])
                    mean[1] += np.sum(img[:, :, 1])
                    mean[2] += np.sum(img[:, :, 2])
                    N += 1
                    if N % 1000 == 0:
                        elapsed = time.time() - beginTime
                        print("Processed {} images in {:.2f} seconds. "
                              "{:.2f} images/second.".format(N, elapsed,
                                                             N / elapsed))
    mean[0] /= N * 280 * 32
    print(mean)
