import numpy as np
from PIL import Image

img = Image.open("images/pic.jpg")  
img_arr = np.array(img)

print("Image shape:", img_arr.shape)

gray = np.mean(img_arr, axis=2).astype(np.uint8)
flipped = np.flip(img_arr,axis=1)

Image.fromarray(gray).save("gray_image.jpg")
Image.fromarray(flipped).save("flipped_image.jpg")

print("Gray-scale and flipped images saved.")