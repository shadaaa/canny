pip install Pillow
from PIL import Image
image = Image.open("C:/Users/ASUS/OneDrive/Desktop/input image/bean.jpg")
rotated_image = image.rotate(90)
rotated_image.save("rotateed_image.jpg")
rotated_image
