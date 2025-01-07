'''
Zuri McKee
11/10/2024
COMP 163
This program uses the function jail to add a set of purple pixels every 10 columns in the dog image to make it look like the dog is 
in jail
'''
from PIL import Image
from image_converter import ListToImage, ImageToList

def jail(pixels):
  '''this function uses for loops to add a set of purple pixels every 10 columns in the dog image'''
  regular_pixels = []
  for row in pixels:#rows
    index = 0
    purp_pixels = []
    regular_pixels.append(purp_pixels)
    for pixel in row: #columns
      if index % 10 == 0:
        R = 128
        G = 0
        B = 128
        pixel = (R, G, B)
      purp_pixels.append(pixel)
      index += 1
  return regular_pixels
      
      



if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = jail(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/jail.png")
