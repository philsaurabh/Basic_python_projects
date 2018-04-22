from PIL import Image

bro = Image.open("819.jpg")
sis = Image.open("882.jpg")

r1,g1,b1=bro.split()

r2,g2,b2=sis.split()
new_img1=Image.merge("RGB",(r1,g2,b1))
new_img1.show()
new_img2=Image.merge("RGB",(b2,g1,r2))
new_img2.show()