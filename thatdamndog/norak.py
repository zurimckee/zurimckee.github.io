'''
Zuri McKee
11/10/24
COMP 163
This program takes an image and converts it to the norak filter using the items RGB values and the averages of said RGB values.
'''


from PIL import Image
from image_converter import ListToImage, ImageToList


def norak(pixels):
  '''This function takes an image and it's RGB values. It then converts the pixels with RGB average values greater than 153 to greyscale.
  the other pixels with values under 153 are left alone. '''
  norak_list = []
  for i, row in enumerate(pixels):#row
    grey_pixels = []
    norak_list.append(grey_pixels)
    for j, pixel in enumerate(row): #columns
      R = pixel[0]
      G = pixel[1]
      B = pixel[2]
      average = (R + G + B) // 3
      if average > 153: 
        new_pixel = (average, average, average)
        grey_pixels.append(new_pixel)
      else:
        grey_pixels.append(pixel)
  return norak_list
  


if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = norak(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/norak.png")
