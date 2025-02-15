import torch.nn as nn
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt
import streamlit as st
import torch

from PIL import Image
from typing import List, Tuple
import requests
import os
from io import BytesIO
import base64

from constants import *

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")   

def create_vit_model(num_classes: int = 4, seed: int = 42):
    # Create ViT_B_16 pretrained weights, transforms and model
    weights = torchvision.models.ViT_B_16_Weights.DEFAULT
    transforms = weights.transforms()
    model = torchvision.models.vit_b_16(weights=weights)

    # Freeze all layers in model
    for param in model.parameters():
        param.requires_grad = False

    # Change classifier head to suit our needs (this will be trainable)
    torch.manual_seed(seed)
    model.heads = nn.Sequential(nn.Linear(in_features=768, out_features=num_classes))  # update to reflect target number of classes

    return model, transforms

def pred_and_plot_image(
    model: torch.nn.Module,
    class_names: List[str],
    img: Image.Image,  # Change image_path to img of type Image.Image
    image_size: Tuple[int, int] = (224, 224),
    transform: torchvision.transforms = None,
    device: torch.device = device,
):
    # Remove the part that opens the image from a file

    # Create transformation for image (if one doesn't exist)
    if transform is not None:
        image_transform = transform
    else:
        image_transform = transforms.Compose(
            [
                transforms.Resize(image_size),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

    ### Predict on image ###

    # Make sure the model is on the target device
    model.to(device)

    with torch.no_grad():
        # Transform and add an extra dimension to image (model requires samples in [batch_size, color_channels, height, width])
        transformed_image = image_transform(img).unsqueeze(dim=0)

        # Make a prediction on image with an extra dimension and send it to the target device
        target_image_pred = model(transformed_image.to(device))

    # Convert logits -> prediction probabilities (using torch.softmax() for multi-class classification)
    target_image_pred_probs = torch.softmax(target_image_pred, dim=1)

    # Convert prediction probabilities -> prediction labels
    target_image_pred_label = torch.argmax(target_image_pred_probs, dim=1)

    # Check if predicted probability is greater than 0.5
    print(f"Pred: {class_names[target_image_pred_label]} | Prob: {target_image_pred_probs.max():.3f}")
    if target_image_pred_probs.max() > 0.5:
        # Plot image with predicted label and probability
        plt.figure()
        plt.imshow(img)
        plt.title(
            f"Pred: {class_names[target_image_pred_label]} | Prob: {target_image_pred_probs.max():.3f} | Remedy : {disease_remedies[class_names[target_image_pred_label]]}"
        )
        plt.axis(False)
        st.pyplot(plt)
    else:
        # Plot image with predicted label as 'None' since probability is less than 0.5
        plt.figure()
        plt.imshow(img)
        plt.title("Pred: None")
        plt.axis(False)
        st.pyplot(plt)

def download_image_from_url(url: str) -> Image.Image:
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        return img
    else:
        st.error("Failed to load image from URL.")
        return None
    
def add_background(image):
    with open(image, "rb") as image:
        enc_string = base64.b64encode(image.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{enc_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )