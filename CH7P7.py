from images import Image
def invert(image):
  for y in range(image.getHeight()):
    for x in range(image.getWidth()):
      (r, g, b) = image.getPixel(x, y)
      invertRed = 255 - r
      invertGreen = 255 - g
      invertBlue = 255 - b
      image.setPixel(x, y, (invertRed, invertBlue, invertGreen))
def main(filename = "example.gif"):
  image = Image(filename)
  print("Close to continue.")
  image.draw()
  invert(image)
  print("Close window to quit.")
  image.draw()
if __name__ == "__main__":
  main()
