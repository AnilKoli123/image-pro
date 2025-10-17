import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io

st.set_page_config(page_title="Image Filtering App", layout="centered")

st.title("🖼 Image Filtering App")
st.write("Upload an image and apply different filters using Streamlit + Python")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Original Image", use_container_width=True)
    st.write("---")

    st.sidebar.header("🎨 Image Filters")
    filter_type = st.sidebar.selectbox(
        "Choose a filter",
        (
            "Original",
            "Grayscale",
            "Invert",
            "Blur",
            "Sharpen",
            "Contrast",
            "Brightness",
            "Emboss",
            "Contour",
            "Detail",
        )
    )

    intensity = st.sidebar.slider("Intensity", 0.0, 3.0, 1.0)

    filtered_img = image

    if filter_type == "Grayscale":
        filtered_img = ImageOps.grayscale(image)
    elif filter_type == "Invert":
        filtered_img = ImageOps.invert(image)
    elif filter_type == "Blur":
        filtered_img = image.filter(ImageFilter.GaussianBlur(radius=intensity*2))
    elif filter_type == "Sharpen":
        enhancer = ImageEnhance.Sharpness(image)
        filtered_img = enhancer.enhance(intensity)
    elif filter_type == "Contrast":
        enhancer = ImageEnhance.Contrast(image)
        filtered_img = enhancer.enhance(intensity)
    elif filter_type == "Brightness":
        enhancer = ImageEnhance.Brightness(image)
        filtered_img = enhancer.enhance(intensity)
    elif filter_type == "Emboss":
        filtered_img = image.filter(ImageFilter.EMBOSS)
    elif filter_type == "Contour":
        filtered_img = image.filter(ImageFilter.CONTOUR)
    elif filter_type == "Detail":
        filtered_img = image.filter(ImageFilter.DETAIL)

    st.image(filtered_img, caption=f"🪄 Filter Applied: {filter_type}", use_container_width=True)

    buf = io.BytesIO()
    filtered_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Download Filtered Image",
        data=byte_im,
        file_name=f"filtered_{filter_type.lower()}.png",
        mime="image/png"
    )

else:
    st.info("👆 Please upload an image to get started.")