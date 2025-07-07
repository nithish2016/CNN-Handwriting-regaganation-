from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image,ImageOps

app = Flask(__name__)


model = load_model('model.hdf5')


def prepare_image(image):
    image = ImageOps.grayscale(image) #convert to grayscale (black and white)
    image = ImageOps.invert(image) #invert the colors
    image = image.resize((28,28)) #resize the image to 28x28
    image = np.array(image)/255.0 #normalize the image (0-1)
    image = image.reshape(1,28,28,1) #reshape the image to 28x28x1 (1 channel)
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image'] #get the image from the form
        if file:
            image = Image.open(file.stream) #open the image
            image = prepare_image(image) #prepare the image for the model
            prediction = model.predict(image) #predict the number
            predicted_class = np.argmax(prediction) #get the predicted class
            return render_template('result.html', predicted_class = predicted_class) #render the result page
    return render_template('index.html') #render the index page

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) #run the app in debug mode