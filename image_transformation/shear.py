image = Image.open("C:/Users/ASUS/OneDrive/Desktop/input image/bean.jpg")
x = 0.2
y = 0.4
sheared = image.transform(
    image.size,
    Image.AFFINE,
    (1,x,0,y,1,0),
    resample = Image.BICUBIC
)
sheared.save("sheared.jpg")
sheared.show()
