import streamlit as st
import torch
import torch.nn as nn

import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt
from PIL import Image
from typing import List, Tuple
import requests
import os
from io import BytesIO
from utils import *

st.set_page_config(page_title="Plant Disease Detection", page_icon="🌱🍂", layout="wide")

add_background(r'bg.jpg')
# Define your device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load your model and class names
#model_save_path = model_path

model, _ = create_vit_model(num_classes=num_classes)

# Load the saved model state dictionary
state_dict = torch.load(model_path,map_location=torch.device('cpu'))

# Create a new dictionary and copy the state dictionary's keys and values to the new dictionary
modified_state_dict = {}
for key, value in state_dict.items():
    modified_key = key.replace("heads.weight", "heads.0.weight").replace("heads.bias", "heads.0.bias")
    modified_state_dict[modified_key] = value

# Load the modified state dictionary into the model
model.load_state_dict(modified_state_dict, strict=False)


# Ensure the model is in evaluation mode
model.eval()

print("Model loaded successfully.")

st.title("Plant Disease Detection 🌱🍂")
#background_image = 'istockphoto-503646746-612x612.jpg'  
#st.image(background_image, use_column_width=True)
st.sidebar.title("Options")

option = st.sidebar.radio("Select Input Method", ["Upload File", "Enter URL"])

if option == "Upload File":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image.', use_column_width=True)
            st.write("")
#             st.write("Classifying...")
#             pred_and_plot_image(model, class_names, img)

elif option == "Enter URL":
        url = st.text_input("Enter Image URL:")
        if url:
            img = download_image_from_url(url)
            if img is not None:
                st.image(img, caption='Image from URL.', use_column_width=True)
                st.write("")
                

if st.button("Predict"):
        st.write("Classifying...")
        pred_and_plot_image(model, class_names, img)