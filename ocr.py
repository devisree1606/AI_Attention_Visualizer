import pytesseract
import shutil

tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text.strip()
