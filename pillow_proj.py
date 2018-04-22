from PIL import Image

img = Image.open("819.jpg")
print(img.size)
print(img.format)

area=(100,100,200,200)
cropped_img=img.crop(area)
img.show()
cropped_img.show()