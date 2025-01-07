'''
Zuri McKee
11/10/24
COMP 163
This program takes an image and converts it to grayscale using the PIL, 
the grayscale function, and the dimensions and RGB values of the pixels,
going through the image to turn each pixel grayish.
'''

from PIL import Image
from image_converter import ListToImage, ImageToList


def grayscale(pixels):
  '''converts a colored picture to grayscale/black and white '''
  color_values = []
  for i, row in enumerate(pixels):
    new_row = []
    color_values.append(new_row)
    for j, pixel in enumerate(row):
      R = pixel[0]
      G = pixel[1]
      B = pixel[2]
      average = (R + G + B) // 3
      new_RGB = (average, average, average)
      print(f'pixel at {i}:{j} was {pixel} is now {new_RGB}')
      new_row.append(new_RGB)
  return color_values
    

  

if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)
  height, width = dog_img.size

  # Apply the filter.
  filtered_pixels = grayscale(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/grayscale.png")
