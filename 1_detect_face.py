#!/usr/bin/python
#   This face detector is made using the now classic Histogram of Oriented
#   Gradients (HOG) feature combined with a linear classifier, an image
#   pyramid, and sliding window detection scheme.  This type of object detector
#   is fairly general and capable of detecting many types of semi-rigid objects
#   in addition to human faces.  Therefore, if you are interested in making
#   your own object detectors then read the train_object_detector.py example
#   program.
import sys

import dlib
from skimage import io


detector = dlib.get_frontal_face_detector()

# TODO: add downsample: http://scikit-image.org/docs/dev/api/skimage.transform.html#skimage.transform.downscale_local_mean

for f in sys.argv[1:]:
    print("Processing file: {}".format(f))
    img = io.imread(f)
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  This will make everything bigger and allow us to detect more
    # faces.
    dets, scores, idx = detector.run(img, 1, -1)
    print("Number of faces detected: {}".format(len(dets)))
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))
        print("Detection {}, score: {}, face_type:{}".format(
            d, scores[i], idx[i]))
