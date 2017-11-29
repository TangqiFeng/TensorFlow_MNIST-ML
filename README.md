# machine-learning

> author: [Tangqi Feng](https://tangqifeng.github.io/)

This is [4th year emerging technologies project](https://github.com/TangqiFeng/machine-learning/wiki/Project-2017)

> Module: Emerging Technologies / 4th Year  
> Lecturer: Dr [Ian McLoughlin](https://ianmcloughlin.github.io/)

In this project, a web application in Python is created to recognise digits in images.
Users will be able to visit the web application through their browser, draw an image containing a single digit, and the web application will respond with the digit contained in the image.
This repository uses [tensorflow](https://www.tensorflow.org/) and [flask](http://flask.pocoo.org/).


![guess](https://user-images.githubusercontent.com/22374434/33279432-6c0fdcd6-d396-11e7-8d04-4fbdd118ed07.gif)

## How this repository organized

This repository includes:
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
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) (a modern and designer-friendly templating language for Python)
* [Pillow](https://pillow.readthedocs.io/en/4.3.x/) (the Python Imaging Library by Fredrik Lundh and Contributors.)

## How to run?
After you download the repository
* run jupyter notebook :
  Go to the repository folder, open the command-line interpreter or terminal(mac)
  * type:
    ``` $ jupyter notebook ```
    then, click *mnist_data_identify_simple.ipynb* / *mnist_data_identify_01.ipynb* / *mnist_data_identify_02.ipynb* on browser which opened automatically
* run the Flask app
  Go to the repository folder, open the command-line interpreter or terminal(mac)
  * type:
    ``` $ FLASK_APP=webapp.py flask run ```
    then, open browser to url: 127.0.0.1:5000
 
**Before you run the project, mack sure all needed components are installed:**
* [Python3](https://anaconda.org/anaconda/python)
* Jupyter, Numpy, Tensorflow,Pillow and Jinja2 use pip install:

```bash
$ pip install Jupyter / Tensorflow / Pillow / numpy / Jinja2 
```
## REFERENCES
* [YouTube tutorial](https://www.youtube.com/watch?v=eAtGqz8ytOI&list=PLjSwXXbVlK6IHzhLOMpwHHLjYmINRstrk) (Chinese)
* [MNIST For ML Beginners](https://www.tensorflow.org/get_started/mnist/beginners)
