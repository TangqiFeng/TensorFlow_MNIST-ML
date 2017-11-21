# upload images. adapted from:
# http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
import os
from flask import Flask, request, redirect, url_for, render_template, json, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file', filename=filename))
#     return render_template("index.html")



import base64
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # convert base64 data to image file
        # adapt from: http://blog.csdn.net/lxdcyh/article/details/4021476
        # and https://stackoverflow.com/questions/31410525/base64-uri-to-png-python
        image = request.values.get('imageBase64')
        print(image)
        imgdata = base64.b64decode(image.split(",")[1])
        # here we define the img type: png
        # and the name of img is image.png 
        # this means everytime the newest img will replace the old one
        # 'wb' here means write binary
        with open('uploads/image.png', 'wb') as fh:
            fh.write(imgdata)
        # get new 28*28 White/Black image
        reDoImage()
        return ''
        

    return render_template("index.html")

# here use Pillow image library
from PIL import Image
def reDoImage():
    # first, read 'image.png' from dolder uploads
    image = Image.open('uploads/image.png')
    # Convert png to jpeg type using Pillow 
    # (from RGBA to RGB)
    # adapt from https://stackoverflow.com/questions/43258461/convert-png-to-jpeg-using-pillow-in-python
    bg = Image.new("RGB", image.size, (255,255,255))
    bg.paste(image,image)
    bg.save('uploads/image.jpg')
    resizeImage()
    
def resizeImage():
    # Change the colorful image to black/white image
    # adapt from: https://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white
    bg = Image.open('uploads/image.jpg')
    gray = bg.convert('L')
    bw = gray.point(lambda x: 0 if x>128 else 255, '1')
    # Then, change the image size to 28*28
    new_image = bw.resize((28, 28))
    # save image.jpg
    new_image.save('uploads/image_28.jpg')


@app.route('/uploaded_file')
def uploaded_file():
    return 'Thanks for uploding'