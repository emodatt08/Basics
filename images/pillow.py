from PIL import Image as image

img  = image.open("/Users/emodatt08/Desktop/flip2.png")
img2 = image.open("/Users/emodatt08/Desktop/error.png")

#get image size and format
print img.size
print img.format

#open image in default image program
img.show()

###CROP IMAGE
# give area of image
area = (20, 100, 200, 200)
# first two parameters are the x/y coordinates of the right corner and other two are the left corner respectively
crop_image = img.crop(area)
#show cropped image
crop_image.show()


###COMBINE TWO IMAGES
# give area of image
area = (400,700)
# combine image by passing two parameters, first parameter takes in the image and the second the area
img.paste(img2, area)
img.show()