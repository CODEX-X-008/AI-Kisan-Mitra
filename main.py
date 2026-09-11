import streamlit as st
import google.generativeai as genai

st.title("AI Kisan Mitra")

uploaded_file = st.file_uploader("Upload a leaf image")

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Crop Image")

    if st.button("Run Diagnosis"):
        with st.spinner("Running Gemini diagnosis..."):
            try:
                response = genai.generate_text(
                    model="gemini-pro-vision",   # or gemini-pro depending on your setup
                    prompt="Diagnose crop disease from uploaded image",
                    timeout=30                   # prevents infinite hang
                )
                st.success("Diagnosis complete!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Diagnosis failed: {e}")
