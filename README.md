# HOG Faces

> These instructions are for Mac OS X

Code for [Machine Learning is Fun! Part 4: Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78#.csqwby8z9).

## Step 0: Optional steps to easy the rest

1. Install boost:
    * `brew install boost --with-python3 --with-python`
    * `brew install boost-python`
1. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
1. Install [XQuartz](https://www.xquartz.org/)
1. Create virtual environment:
```mkvirtualenv --python=`which python3` p3env-ai```
1. Activate your Python environment: `workon p3env-ai` (p3env-ai is my environment name)
1. Install a bunch of Python dependencies:
    * pip install scipy
    * pip install scikit-image
    * There might be more...
1. Install [dlib](https://npatta01.github.io/2015/08/10/dlib/)
1. Run the examples to see if dlib worked.

## Step 1: Finding all the faces

Activate environment:

```
workon p3env-ai
```

Run face detection:

```
python face_detector.py faces/face1.jpg
```
