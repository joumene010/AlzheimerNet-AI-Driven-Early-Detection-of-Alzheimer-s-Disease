import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load your model
MODEL_PATH = "model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Class names mapping (replace with your actual classes)
class_names = {0: "AD", 1: "CI", 2: "CN"}

# Preprocessing function
def preprocess_image(image):
    image = image.resize((128, 128))  # Resize to the input size of the model
    image_array = np.array(image)  # Convert to numpy array
    if image_array.ndim == 2:  # If grayscale, add channel dimension
        image_array = np.expand_dims(image_array, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    image_array = image_array / 255.0  # Normalize to [0, 1]
    return image_array

# Streamlit interface
st.title("ALZHEIMER CLASSIFICATION APP")
st.write("Upload an image, and the model will predict its class.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    st.write("Processing the image...")
    preprocessed_image = preprocess_image(image)

    # Predict the class
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions)
    class_name = class_names.get(predicted_class, "Unknown")
    
   

    # Display the result
    st.write(f"Predicted Class: **{class_name}**")
