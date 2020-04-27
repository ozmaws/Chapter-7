from images import Image
def posterize(image, colorPixel):
  whitePixel = (255, 255, 255)
  for y in range(image.getHeight()):
    for x in range(image.getWidth()):
      (r, g, b) = image.getPixel(x, y)
      average = (r + g + b) // 3
      if average < 128:
        image.setPixel(x, y, colorPixel)
      else:
        image.setPixel(x, y, whitePixel)
def main(filename = "example.gif"):
  image = Image(filename)
  print("Close to continue.")
  image.draw()
  color = (82, 50, 168)
  posterize(image, color)
  print("Close window to quit.")
  image.draw()
if __name__ == "__main__":
  main()
