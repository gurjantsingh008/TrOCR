import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import difflib
import pyautogui
import time

# --- Load Model ---
@st.cache_resource
def load_model():
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-printed")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-printed")
    return processor, model

processor, model = load_model()

# --- Functions ---
def extract_text(image):
    image = image.convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    with torch.no_grad():
        generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return text.strip()

def compare_texts(text1, text2):
    similarity = difflib.SequenceMatcher(None, text1, text2).ratio() * 100
    if similarity == 100:
        return f"✅ Exact match: '{text1}'", similarity
    else:
        return f"❌ Not an exact match.\n\n**Text1:** {text1}\n**Text2:** {text2}", similarity

def write_to_notepad(message):
    # Wait 1 second to give you time to focus Notepad
    time.sleep(1)
    pyautogui.write(message, interval=0.05)  # types the message
    pyautogui.press("enter")

# --- Streamlit UI ---
st.set_page_config(page_title="TrOCR Image Text Matcher", layout="centered")
st.title("📝 TrOCR Image Text Matcher")
st.write("Upload two images, compare text, and send result to Notepad if similarity ≥ 50%.")

col1, col2 = st.columns(2)
with col1:
    img1_file = st.file_uploader("Upload first image", type=["jpg", "jpeg", "png"])
with col2:
    img2_file = st.file_uploader("Upload second image", type=["jpg", "jpeg", "png"])

if img1_file and img2_file:
    img1 = Image.open(img1_file)
    img2 = Image.open(img2_file)

    st.image([img1, img2], caption=["Image 1", "Image 2"], width=250)

    if st.button("🔍 Compare Texts"):
        with st.spinner("Extracting text..."):
            text1 = extract_text(img1)
            text2 = extract_text(img2)
            result, similarity = compare_texts(text1, text2)

        st.subheader("Comparison Result")
        st.markdown(result)
        st.write(f"**Similarity Score:** {similarity:.2f}%")

        if similarity >= 50:
            st.success("Similarity ≥ 50%! Sending result to Notepad...")
            # Bring Notepad to front manually before running, then press
            write_to_notepad("Result Verified ✅")
