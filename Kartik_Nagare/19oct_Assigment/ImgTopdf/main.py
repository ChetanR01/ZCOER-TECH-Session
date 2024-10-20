# Develop a Python program for image-to-PDF converter
# it choose random img from img folder to make PDF

import random
import img2pdf
from PIL import Image
import os

img_num = random.randint(1,6)

img_path =f"Kartik_Nagare/19oct_Assigment/ImgTopdf/img/{img_num}.png"

pdf_path = f"Kartik_Nagare/19oct_Assigment/ImgTopdf/pdf/{img_num}.pdf"

img = Image.open(img_path)

pdf_converting = img2pdf.convert(img.filename)

file = open(pdf_path, "wb")

file.write(pdf_converting)

img.close()

file.close()

print("Successfully pdf created")