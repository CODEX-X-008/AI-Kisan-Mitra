import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="AI Kisan Mitra",
    page_icon="🌾",
    layout="wide"
)

# Header Section
st.title("🌾 AI Kisan Mitra")
st.caption("Smart India Hackathon Prototype | Crop Health & Fair Price Assistant")

st.markdown("---")

# Main Navigation Tabs
tab1, tab2 = st.tabs(["🌿 Crop Disease Classifier", "📈 Market Price Predictor"])

# =========================================================
# TAB 1: CROP DISEASE CLASSIFIER
# =========================================================
with tab1:
    st.header("Upload Crop Image for Disease Diagnosis")
    st.write("Upload a clear picture of the leaf or crop to identify potential diseases and get care recommendations.")

    uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        col1, col2 = st.columns([1, 1])

        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Crop Image", use_container_width=True)

        with col2:
            st.subheader("Diagnosis Results")
            # Simulated model prediction for demonstration
            st.success("Analysis Complete!")
            st.markdown("**Detected Issue:** Early Blight (Fungal Infection)")
            st.markdown("**Confidence Score:** 92.4%")

            st.warning("⚠️ **Recommended Treatments:**")
            st.markdown("""
            * Apply copper-based fungicides or Mancozeb every 7-10 days.
            * Avoid overhead irrigation to keep foliage dry.
            * Rotate crops with non-solanaceous plants next season.
            """)
    else:
        st.info("Please upload an image file to trigger the AI diagnosis.")

# =========================================================
# TAB 2: MARKET PRICE PREDICTOR (FRAMEWORK)
# =========================================================
with tab2:
    st.header("📈 Market Price Predictor (Framework)")
    st.info("⚡ Live Agmarknet API Integration Pending")

    st.markdown("""
    ### Pipeline Architecture & Real-Time Feed Plan

    * **Data Sources:** Government of India **Agmarknet API** (`data.gov.in`) and **e-NAM** daily arrivals.
    * **Analytical Pipeline:** Time-series forecasting via Random Forest and XGBoost models.
    * **Feature Ingestion:** Mandi location, historical seasonal trends, and crop volume.
    """)

    col1, col2 = st.columns([1, 2])
    with col1:
        selected_crop = st.selectbox("Select Crop (Preview)", ["Wheat", "Paddy", "Potato", "Tomato", "Cotton"])
        forecast_days = st.slider("Forecast Horizon (Days)", min_value=1, max_value=30, value=7)
    
    with col2:
        st.warning(f"Live market price feeds and a {forecast_days}-day price trend forecast for **{selected_crop}** will sync upon Agmarknet API key authorization.")

st.markdown("---")
st.caption("AI Kisan Mitra • SIH Prototype Version 1.0")
