"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:SimpleImage,the original image
    :return:SimpleImage,the blurred image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            pixel = img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                neighbors = [img.get_pixel(x, y + 1), img.get_pixel(x + 1, y), img.get_pixel(x + 1, y + 1)]

            elif x == img.width - 1 and y == 0:
                # Get pixel at the top-right corner of the image.
                neighbors = [img.get_pixel(x - 1, y), img.get_pixel(x - 1, y + 1), img.get_pixel(x, y + 1)]

            elif x == 0 and y == img.height - 1:
                # Get pixel at the bottom-left corner of the image
                neighbors = [img.get_pixel(x, y - 1), img.get_pixel(x + 1, y - 1), img.get_pixel(x + 1, y)]

            elif x == img.width - 1 and y == img.height - 1:
                # Get pixel at the bottom-right corner of the image
                neighbors = [img.get_pixel(x - 1, y - 1), img.get_pixel(x, y - 1), img.get_pixel(x - 1, y)]


            elif 0 < x < img.width - 1 and y == 0:
                # Get top edge's pixels (without two corners)
                neighbors = [img.get_pixel(x - 1, y), img.get_pixel(x - 1, y + 1), img.get_pixel(x, y + 1),
                             img.get_pixel(x + 1, y), img.get_pixel(x + 1, y + 1)]

            elif 0 < x < img.width - 1 and y == img.height - 1:
                # Get bottom edge's pixels (without two corners)
                neighbors = [img.get_pixel(x - 1, y - 1), img.get_pixel(x, y - 1), img.get_pixel(x + 1, y - 1),
                             img.get_pixel(x - 1, y), img.get_pixel(x + 1, y)]


            elif x == 0 and 0 < y < img.height - 1:
                # Get left edge's pixels (without two corners)
                neighbors = [img.get_pixel(x, y - 1), img.get_pixel(x + 1, y - 1), img.get_pixel(x + 1, y),
                             img.get_pixel(x, y + 1), img.get_pixel(x + 1, y + 1)]


            elif x == img.width - 1 and 0 < y < img.height - 1:
                # Get right edge's pixels (without two corners)
                neighbors = [img.get_pixel(x - 1, y - 1), img.get_pixel(x, y - 1), img.get_pixel(x - 1, y),
                             img.get_pixel(x - 1, y + 1), img.get_pixel(x, y + 1)]

            else:
                # Inner pixels.
                neighbors = [img.get_pixel(x - 1, y - 1), img.get_pixel(x, y - 1), img.get_pixel(x + 1, y - 1),
                             img.get_pixel(x - 1, y), img.get_pixel(x + 1, y), img.get_pixel(x - 1, y + 1),
                             img.get_pixel(x, y + 1), img.get_pixel(x + 1, y + 1)]

                # calculate the average rgb values of the neighbors
            new_r = sum([neighbor.red for neighbor in neighbors]) // len(neighbors)
            new_g = sum([neighbor.green for neighbor in neighbors]) // len(neighbors)
            new_b = sum([neighbor.blue for neighbor in neighbors]) // len(neighbors)
            # set the new pixel value in the new image
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = new_r
            new_pixel.green = new_g
            new_pixel.blue = new_b

    return new_img


def main():
    """
    TODO:display an image and show its blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
