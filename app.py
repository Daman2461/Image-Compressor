import streamlit as st
import pickle
from PIL import Image
import sys


from my_model import compress

# Streamlit web app
st.title("Image Compression App")

# File uploader for image input
uploaded_file = st.file_uploader("Upload a PNG Image", type=["png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    n=st.slider('Enter number of colors to compress into(number of centroids)',2,25)
    it=st.slider('Enter number of iterations',1,15)
    
    
    # Compress the uploaded image using the compress function
    if st.button("Compress Image"):
        compressed_image = compress(image,n,it)
        if(compressed_image==-1):
            st.error("Invalid Image")
        
        # Display the compressed image
        else:
            
            st.image(compressed_image, caption="Compressed Image", use_column_width=True)
        
            st.success("Image compressed successfully.")
