import img2pdf as ip
from PIL import Image
import os

img_path = "C:\\Users\\Admin\\Pictures\\w7.jpg"
pdf_path = "C:\\Users\\Admin\\Pictures\\w7.pdf"  

img = Image.open(img_path)

with open(pdf_path, "wb") as file:
    pdf_bytes = ip.convert(img_path)
    file.write(pdf_bytes)

img.close()

print("Successfully made pdf file")
