from PIL import Image as image
from pprint import pprint
img  = image.open("/Users/emodatt08/Desktop/flip2.png")
img2 = image.open("/Users/emodatt08/Desktop/error.png")

#get image size and format
def size_and_format():
    print img.size
    print img.format

#open image in default image program
def open_image():
    img.show()

###CROP IMAGE
def crop_image():
# give area of image
    area = (20, 100, 200, 200)
# first two parameters are the x/y coordinates of the right corner and other two are the left corner respectively
    crop_image = img.crop(area)
#show cropped image
    crop_image.show()


###COMBINE TWO IMAGES
def comb_two_images():
# give area of image
    area = (400,700)
# combine image by passing two parameters, first parameter takes in the image and the second the area
    img.paste(img2, area)
    img.show()

###SHOW IMAGE PIXELS
def pixel_image():
    #convert image to RGB format
    imge = img.convert('RGB')
    #split image
    r,g,b = imge.split()
    return b,g,r
    # r.show()
    # g.show()
    # b.show()

###Merge effects
def merge_image():
    #convert first image to RGB format
    img_1 = img.convert('RGB')
    #split first image
    r,g,b = img_1.split()

    #convert second image to RGB format
    img_2 = img2.convert('RGB')
    #split second image
    r1,g1,b1 = img_2.split()
    #combine pixels from both the first and second
    new = image.merge('RGB', (r1,g1,b))
    new.show()


merge_image()
