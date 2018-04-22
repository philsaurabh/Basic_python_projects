from PIL import Image

bro = Image.open("819.jpg")
print(bro.mode)
r,g,b=bro.split()
new_img1=Image.merge("RGB",(r,g,b))
new_img1.show()
new_img2=Image.merge("RGB",(b,g,r))
new_img2.show()