# HOG Faces

> These instructions are for Mac OS X

Code for [Machine Learning is Fun! Part 4: Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78#.csqwby8z9).

## Step 0: Optional steps to easy the rest

1. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
2. Install [XQuartz](https://www.xquartz.org/)
3. Install [dlib](https://npatta01.github.io/2015/08/10/dlib/)

## Step 1: Finding all the faces

Install dependencies (Mac OS X):

```
brew install boost --with-python
brew install boost-python
virtualenv -p python3 p3env
. p3env/bin/activate
pip install scikit-image
pip install dlib
```
