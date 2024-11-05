from PIL import Image, ImageFilter


# Code run for images on James Folder
image = Image.open("./James/BBJ.jpg")
# print(image.format)#This gives us the picture format of the image, jpg, png.
# print(image.size) #This gives us the size of the image
# print(image.mode)#This gives us the coloring mode of the image
image.show()


# this code gives us filtered image
filtered_image = image.filter(ImageFilter.BLUR)#This code blur the image
filtered_image.save(fp="./James/BBJBlur.png",format="png") #This save a copy of the image to a filePath and format
filtered_image.show() #This code show us the image

# This code convert the color of the image
convert_image = image.convert("L")#This code convert the image to Black n white
convert_image.save(fp="./James/BBJConvert.png",format="png") #This save a copy of the image to a filePath and format
convert_image.show()#This code show us the image

# This code ROTATE THE IMAGE TO 90 degrees
rotate_image = Image.open("./James/JayBee.jpg")
rotate_img= rotate_image.rotate(90)
rotate_img.save("./James/Rotate.png","png")
rotate_img.show()

# RESIZING a picture
resize_image = Image.open("./James/Pinky.jpg")
resize_img = resize_image.resize((300,300))
resize_img.save("./James/ResizePinky.png","png")
resize_img.show()

# Thumbnail a picture and resize it 
thumbnail_image = Image.open("./James/JayBee2.jpg")
thumbnail_image.thumbnail((300,300))
thumbnail_image.save("./James/thumbnailImg.png","png")
thumbnail_image.show()
