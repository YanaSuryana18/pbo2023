import pytesseract as tess
tess.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
from PIL import Image

img = Image.open (r"C:\\Users\LENOVO\\OneDrive\\Documents\\Tugas PBO\\yana.png")
text = tess.image_to_string (img)

print (text)