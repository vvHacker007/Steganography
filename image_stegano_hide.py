from stegano import lsb

secret=lsb.hide("./HelloThere.jpg","Hello")
secret.save("./Encoded_Image.jpg")
