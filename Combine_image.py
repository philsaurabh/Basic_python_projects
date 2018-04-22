from PIL import Image

bro = Image.open("819.jpg")
sis = Image.open("882.jpg")
area=(100,100,400,400)
sis.paste(bro,area)
sis.show()