from PIL import Image
import pytesseract

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open image
img = Image.open("sample.png")

# Extract text
text = pytesseract.image_to_string(img)

print("Extracted Text:")
print(text)