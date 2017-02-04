# HOG Faces

> These instructions are for Mac OS X

Code for [Machine Learning is Fun! Part 4: Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78#.csqwby8z9).

## Install dependencies and set up

First, you must install [XQuartz](https://www.xquartz.org/).

Then, you can install other dependencies:

```
# Boost
brew install boost --with-python3 --with-python
brew install boost-python

# virtualenvwrapper (see https://virtualenvwrapper.readthedocs.io/en/latest/)
pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh  # add to .bash_profile
# I use Python 3
mkvirtualenv --python=`which python3` p3env-ai
workon p3env-ai

# dlib dependencies
pip install numpy
pip install scipy
pip install scikit-image

# dlib (see https://npatta01.github.io/2015/08/10/dlib/)
git clone git@github.com:davisking/dlib.git
cd dlib
python setup.py install --yes DLIB_JPEG_SUPPORT  # takes a long time
```

## Step 1: Finding all the faces

Activate environment (if not already active):

```
workon p3env-ai
```

Run face detection:

```
# For demo with GUI
python 1_detect_face_visual.py faces/face1.jpg

# For demo without GUI
python 1_detect_face.py faces/face1.jpg
```
