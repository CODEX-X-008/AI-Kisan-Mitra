import streamlit as st
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key="YOUR_API_KEY")

# Use the vision model since you’re uploading images
model = genai.GenerativeModel("gemini-pro-vision")

st.title("AI Kisan Mitra")

uploaded_file = st.file_uploader("Upload a leaf image")

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Crop Image")

    if st.button("Run Diagnosis"):
        with st.spinner("Running Gemini diagnosis..."):
            try:
                # Pass both the text prompt and the uploaded image
                response = model.generate_content(
                    ["Diagnose crop disease from this image", uploaded_file]
                )
                st.success("Diagnosis complete!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Diagnosis failed: {e}")
