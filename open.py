from PIL import Image

path = "cat.jpg"

#program retrieves image
img = Image.open(path)

#program displays image through any default image program such as "Windows Photos"
img.show()