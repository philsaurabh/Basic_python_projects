from PIL import Image

bro = Image.open("819.jpg")
print(bro.mode)
r,g,b=bro.split()
r.show()
g.show()
b.show()