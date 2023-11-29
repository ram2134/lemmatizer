from PIL import Image
if __name__ == '__main__':
    img = Image.open("IITK.jpg")
    img = img.resize((50,50), Image.ANTIALIAS)
    img.save('IITK-1.jpg')