# machine-learning

> author: [Tangqi Feng](https://tangqifeng.github.io/)

This is [4th year emerging technologies project](https://github.com/TangqiFeng/machine-learning/wiki/Project-2017)

> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr [Ian McLoughlin](https://ianmcloughlin.github.io/)

In this project you will create a web application in Python to recognise digits in images.
Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image.
You should use [tensorflow](https://www.tensorflow.org/) and [flask](http://flask.pocoo.org/) to do this.
Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.

![guess](https://user-images.githubusercontent.com/22374434/33279432-6c0fdcd6-d396-11e7-8d04-4fbdd118ed07.gif)

## How this repository organized

This repository inclouds:
* Three attempts for tensorflow with mnist data, using jupyter notebook:
  * file [mnist_data_identify_simple.ipynb](https://github.com/TangqiFeng/machine-learning/blob/master/mnist_data_identify_simple.ipynb) simple TensorFlow with mnist data.
  * file [mnist_data_identify_01.ipynb](https://github.com/TangqiFeng/machine-learning/blob/master/mnist_data_identify_01.ipynb) add middle layer tenser and dropout method to improve accuracy
  * file [mnist_data_identify_02.ipynb](https://github.com/TangqiFeng/machine-learning/blob/master/mnist_data_identify_02.ipynb) 	try different optimizer to train the model
* [mnist_tf.py](https://github.com/TangqiFeng/machine-learning/blob/master/mnist_tf.py) contains a solution which achieves a good accuracy,this version came out after three attempts above.
* [webapp.py](https://github.com/TangqiFeng/machine-learning/blob/master/webapp.py) the main server scripts, imports minist_tf.py, handles routes from ajax call of web page.
* some html files in folder 'templates':
  * [layout.html](https://github.com/TangqiFeng/machine-learning/blob/master/templates/layout.html) uses **Jinjia2** template, defines basic structure of web app, which can change component of web page easily.
  * [index.htmml](https://github.com/TangqiFeng/machine-learning/blob/master/templates/index.html) organizing related parts of (use Jinja2 template) main web page.
  * [draw.html](https://github.com/TangqiFeng/machine-learning/blob/master/templates/draw.html) is draw picture part, related javascript handles draw a img in a canvas, and sent the img to the server.
  * [uploadImage.html](https://github.com/TangqiFeng/machine-learning/blob/master/templates/uploadImage.html) allows user upload img to server. At this moment, this part does not included in the main project. But it is easy to add this function, because img convertion method is provided, and related receive image function is existed in webapp.py (comment part down the bottom).
* example image files in folder 'uploads':
  * image.png -> image got directly from canvas in web page.
  * image.jpg -> a 'jpg' type image (RGB) convert from 'image.png'(RGBA).
  * image_28.jpg -> a 'gray' and sized '28*28' image convert from 'image.jpg'.
in order to predict the number user drawing/uploading, the image need convert to same size and coding image as Mnist dataset.

## Components
* [Python3](https://www.python.org/download/releases/3.0/) (a programming language that lets you work quickly
and integrate systems more effectively)
* [Jupyter](http://jupyter.org/) (an interactive computing environment that enables users to author notebook documents)
* [Numpy](http://www.numpy.org/) (the fundamental package for scientific computing with Python.)
* [Tensorflow](https://www.tensorflow.org/) (An open-source software library for Machine Intelligence)
* [Keras](https://keras.io/) (a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.)

## How to run?
After you download the repository

Go to the repository folder, open the command-line interpreter or terminal(mac)
* type:
  ``` $ jupyter notebook ```
  then, click *Iris_data_set_TensorFlow.ipynb* on browser which opened automatically
* type: 
  ``` $ python3 iris_nn.py ```
  then, you can get the results
 
**Before you run the project, mack sure all needed components are installed:**
* [Python3](https://anaconda.org/anaconda/python)
* Jupyter, Numpy, Tensorflow and Keras use pip install:

```bash
$ pip install Jupyter / Tensorflow / numpy / Keras 
```
## REFERENCES
