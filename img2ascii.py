import sys
import traceback
from PIL import Image

ASCII_CHARS = ['.', ',', ':', ';', '-', '+', '|', 'V', 'N', 'M']
DEFAULT_WIDTH = 150

def scale_image(image, new_width=DEFAULT_WIDTH):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    pixels_in_image = list(image.getdata())

    #print("".join(str(pixels_in_image)))

    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)-1] for pixel_value in pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image(image, new_width=DEFAULT_WIDTH):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    num_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in range(0, num_chars, new_width)]

    return "\n".join(image_ascii)

if __name__=='__main__':
        try:
            image_filepath = sys.argv[1]
            image = None
        
            image = Image.open(image_filepath)
        except:
            traceback.print_exc()
            exit("Unable to open image file")

        ascii_image = convert_image(image)
        print(ascii_image)

