import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def main():
    st.title("Image to Text App")

    image = st.file_uploader("Upload an image")
    if image is not None:
        with open(image, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        output = response.json()
        st.write(output)

if __name__ == "__main__":
    main()