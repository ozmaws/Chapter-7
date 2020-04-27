from images import Image
def lighten(image, value):
  for y in range(image.getHeight()):
    for x in range(image.getWidth()):
      (r, g, b) = image.getPixel(x, y)
      r = r + value
      if r > 255:
        r = 255
      g = g + value
      if g > 255:
        g = 255
      b = b + value
      if b > 255:
        b = 255
      image.setPixel(x, y, (r, g, b))
def darken(image, value):
  for y in range(image.getHeight()):
    for x in range(image.getWidth()):
      (r, g, b) = image.getPixel(x, y)
      r = r - value
      if r < 0:
        r = 0
      g = g - value
      if g < 0:
        g = 0
      b = b - value
      if b < 0:
        b = 0
      image.setPixel(x, y, (r, g, b))
def colorFilter(image, cFilter):
  for y in range(image.getHeight()):
    for x in range(image.getWidth()):
      (r, g, b) = image.getPixel(x, y)
      (adjustedRed, adjustedGreen, adjustedBlue) = cFilter
      r = r + adjustedRed
      if r > 255:
        r = 255
      elif r < 0:
        r = 0
      g = g + adjustedGreen
      if g > 255:
        g = 255
      elif g < 0:
        g = 0
      b = b + adjustedBlue
      if b > 255:
        b = 255
      elif b < 0:
        b = 0
      image.setPixel(x, y, (r, g, b))
def main(filename = "example.gif"):
  image = Image(filename)
  print("Close to continue.")
  image.draw()
  colorFilter(image, (0, -100, 0))
  print("Close window to quit.")
  image.draw()
if __name__ == "__main__":
  main()
