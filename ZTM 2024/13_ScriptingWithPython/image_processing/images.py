from PIL import Image, ImageFilter
img = Image.open("./pokedex/210 - bulbasaur.jpg")
# print(img)
print(img.format) #This gives us the image format
print(dir(img)) #This gives us all the method to use on the image
