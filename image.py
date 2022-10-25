from PIL import Image

image_file = Image.open('image.png')
image_file = image_file.convert('1')
image_file.save("result.png")