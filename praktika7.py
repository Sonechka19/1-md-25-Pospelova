def task1():
    from PIL import Image
    img = Image.open("severodvinsk.jpg")
    img.show()
    print(img.size)
    print(img.format)
    print(img.mode)
# task1()

def task2():
    from PIL import Image
    img = Image.open("severodvinsk.jpg")
    img1 = img.reduce(3)
    img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img1.save("onesev.jpg")
    img2.save("twosev.jpg")
    img3.save("threesev.jpg")
# task2()

def task3():
    from PIL import Image, ImageFilter
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpeg", "5.jpg"]
    for img in images:
        image = Image.open(img)
        imgcont = image.filter(ImageFilter.CONTOUR)
        imgcont.save('filters/' + str(img))
# task3()

def task4():
    from PIL import Image
    m = Image.open("img.png")
    ma = m.reduce(12)
    ma.save('imgg.jpg')
    # def water(severodvinsk, outimg, img, position):
    #     baza = Image.open(severodvinsk)
    #     marka = Image.open(img)
    #     baza.paste(marka, position)
    #     baza.show()
    #     baza.save(outimg)
    # if __name__ == '__main__':
    #     water("severodvinsk.jpg", "imgg.jpg", "water.jpg", (0, 0))
task4()