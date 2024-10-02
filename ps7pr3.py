#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def bw(pixels, threshold):
    ''' takes in a 2D-list, pixels, of the pixels of an image, and threshold, a number,
    and returns a 2-D list, of the black and white version of that image, a pixel becomes white
    if its brightness is above the threshold, and black if it isn't'''
    pixheight = len(pixels)
    pixwidth = len(pixels[0])
    new_pixels = create_green_image(pixheight, pixwidth)
    black = [0,0,0]
    white = [255,255,255]
    
    for r in range(pixheight):
        for c in range(pixwidth):
            pixbrightness = brightness(pixels[r][c])
            if pixbrightness > threshold:
                new_pixels[r][c] = white
            else:
                new_pixels[r][c] = black
    return new_pixels


def upside_down(pixels):
    ''' takes in a 2D-list, pixels, of the pixels of an image, and returns a list, of the pixels
    of the image upside down'''
    pixheight = len(pixels)
    pixwidth = len(pixels[0])
    new_pixels = create_green_image(pixheight, pixwidth)
    
    for r in range(pixheight):
        for c in range(pixwidth):
            maxheight = pixheight - 1
            new_pixels[r][c] = pixels[maxheight-r][c]
    return new_pixels

def reflect(pixels):
    ''' takes in a 2D-list, pixels, of the pixels of an image, and returns a list, of the pixels
    of half the image reflected to the other half'''
    pixheight = len(pixels)
    pixwidth = len(pixels[0])
    halfwidth = pixwidth//2
    new_pixels = create_green_image(pixheight, pixwidth)
    
    for r in range(pixheight):
        for c in range(pixwidth):
            maxwidth = pixwidth- 1
            if c >= halfwidth:
                new_pixels[r][c] = pixels[r][maxwidth - c]
            else:
                new_pixels[r][c] = pixels[r][c]
    return new_pixels

def shrink(pixels):
    '''takes in a 2D-list, pixels, of the pixels of an image, and returns a list, of the pixels
    of the picture shrunk by removing every other pixel'''
    pixheight = len(pixels)
    pixwidth = len(pixels[0])
    halfwidth = pixwidth//2
    halfheight = pixheight//2
    new_pixels = create_green_image(halfheight, halfwidth)
    
    for r in range(halfheight):
        for c in range(halfwidth):
            new_pixels[r][c]=pixels[2*r][2*c]
    return new_pixels
    
            
    