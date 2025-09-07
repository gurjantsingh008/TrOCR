# TrOCR
📝 TrOCR Image Text Matcher with Notepad Verification
# 📝 TrOCR Image Text Matcher with Notepad Verification

This project is a **Streamlit application** that uses Microsoft’s **TrOCR (Transformer OCR)** model to extract and compare text from two uploaded images.  
If the similarity score between the extracted texts is **greater than or equal to 50%**, the app automatically sends a verification message to a **Notepad window** open on your desktop.  

---

## ✨ Features
- 📷 Upload two images (`.jpg`, `.jpeg`, `.png`)  
- 🔍 Extract text using **Hugging Face TrOCR model**  
- 📊 Compare extracted text similarity with **difflib**  
- ✅ Display results in Streamlit (comparison, similarity percentage, progress bar)  
- 🖊️ If similarity ≥ 50%, automatically type **“Result Verified ✅”** into Notepad using **pyautogui**  

---

## 🛠️ Tech Stack
- [Python 3.9+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – Web app UI  
- [Hugging Face Transformers](https://huggingface.co/) – OCR model (TrOCR)  
- [PyTorch](https://pytorch.org/) – Model backend  
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) – Automates typing into Notepad  
- [difflib](https://docs.python.org/3/library/difflib.html) – String similarity comparison  

---

## 🚀 How It Works
1. Run the Streamlit app:  
   ```bash
   streamlit run app.py
Open Notepad on your desktop and keep it focused.

Upload two images in the app and click Compare Texts.

If similarity ≥ 50%, the app will automatically type into Notepad:

Result Verified ✅
Installation

Clone the repo and install dependencies:

git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt

📌 Requirements

Make sure you have these installed (included in requirements.txt):

streamlit
torch
transformers
pillow
pyautogui

⚠️ Notes

Keep Notepad open and focused, otherwise the message may be typed into another window.

Windows may ask for accessibility permissions to allow pyautogui to control the keyboard.

Works best on Windows with Notepad; can be adapted for other editors or applications.
