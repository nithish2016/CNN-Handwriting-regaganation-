# Handwritten Digit Recognition Web Application

## Description
This project is a Flask-based web application that allows users to upload images of handwritten digits and predicts the digit using a pre-trained TensorFlow/Keras model. The application preprocesses the uploaded image, feeds it to the model, and displays the predicted digit on a result page.

## Screenshots

![image](https://github.com/user-attachments/assets/58e78ed8-98b1-4d26-9f71-1f3ddc40d279)

![image](https://github.com/user-attachments/assets/37f67aae-f9eb-4738-9ff4-3586995f408f)



## Features
- Upload an image of a handwritten digit via a simple web interface.
- Image preprocessing including grayscale conversion, inversion, resizing, and normalization.
- Digit prediction using a pre-trained deep learning model.
- Clean and responsive UI using Bootstrap.

## Installation

1. Clone the repository or download the project files.

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install flask tensorflow pillow numpy
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

3. Upload an image of a handwritten digit and click "Predict".

4. View the predicted digit on the result page.

## File Structure

- `app.py`: Main Flask application script that handles image upload, preprocessing, prediction, and routing.
- `model.hdf5`: Pre-trained TensorFlow/Keras model used for digit recognition.
- `templates/`: Contains HTML templates for the web interface.
  - `index.html`: Upload form page.
  - `result.html`: Prediction result display page.

