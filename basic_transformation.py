from PIL import Image

bro = Image.open("819.jpg")
baby = Image.open("882.jpg")
square_bro=bro.resize((250,250))
flip_baby=baby.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby=baby.transpose(Image.ROTATE_90)
square_bro.show()
flip_baby.show()
spin_baby.show()