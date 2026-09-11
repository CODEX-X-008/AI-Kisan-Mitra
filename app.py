import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Gemini with your API key
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro-vision")

st.title("AI Kisan Mitra")

uploaded_file = st.file_uploader("Upload a leaf image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Convert Streamlit UploadedFile → PIL.Image
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Crop Image")

    if st.button("Run Diagnosis"):
        with st.spinner("Running Gemini diagnosis..."):
            try:
                # Pass the PIL image, not UploadedFile
                response = model.generate_content(
                    ["Diagnose crop disease from this image", image]
                )
                st.success("Diagnosis complete!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Diagnosis failed: {e}")
