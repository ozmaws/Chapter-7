from images import Image
def grayscale(image):
  for y in range(image.getHeight()):
    for x in range(image.getWidth()):
      (r, g, b) = image.getPixel(x, y)
      average = (r + g + b) // 3
      image.setPixel(x, y, (average, average, average))
def main(filename = "example.gif"):
  image = Image(filename)
  print("Close to continue.")
  image.draw()
  grayscale(image)
  print("Close window to quit.")
  image.draw()
if __name__ == "__main__":
  main()
