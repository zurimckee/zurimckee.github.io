'''
Zuri McKee
11/10-11/24
COMP 163 
This project uses the yours function to take the RGB values of the original dog picures, and the average 
function from another part of the project, but instead of averaging the values, I subtracted R G and B 
then I multiplied them, so sort of an opposite average. I also used the same if average statement from 
Norak and used it to decide which pixels were changed into the new psuedo-average pixels.
'''

def yours(pixels):
  '''This function returns screamo-dog/badly-developed-film dog, it's the dog but he's hyper saturated and the bright colors in 
  the original pictures are amplified. '''
  regular_pixels = []
  for row in pixels:#rows
    purp_pixels = []
    regular_pixels.append(purp_pixels)
    index = 0
    for pixel in row: #columns
      R = pixel[0]
      G = pixel[1]
      B = pixel[2]
      average = (R - G - B) * 3
      #print(f'{R}, {G}, {B}')
      if average < 153: 
        new_pixel = (average, average, average)
        purp_pixels.append(new_pixel)
  return regular_pixels

  
  
if __name__ == '__main__':
  # Open the image.
  dog_img = Image.open("images/dog.png")
  pixels = ImageToList(dog_img)

  # Apply the filter.
  filtered_pixels = yours(pixels)
  

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("images/yours.png")
