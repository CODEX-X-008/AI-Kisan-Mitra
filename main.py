import streamlit as st

st.title("AI Kisan Mitra")

uploaded_file = st.file_uploader("Upload a leaf image")
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Crop Image")
    st.write("Running diagnosis...")
    # Call your Gemini AI function here
