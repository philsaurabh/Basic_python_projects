from PIL import Image
from PIL import ImageFilter
bro = Image.open("819.jpg")
sis = Image.open("882.jpg")
b_w=bro.convert("L")
b_w.show()
blur=sis.filter(ImageFilter.BLUR)
details=sis.filter(ImageFilter.DETAIL)
edges=sis.filter(ImageFilter.FIND_EDGES)
blur.show()
details.show()
edges.show()