import sys
import traceback
import tkinter as tk
import tkinter.font as font
from tkinter import *
from PIL import Image, ImageTk

# Ascii character standard ramp from black -> white, source: http://paulbourke.net/dataformats/asciiart/
# "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. "
# kinda trash tbh
#ASCII_CHARS_STANDARD = ['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t','/','\\','|','(',')','1','{','}','[',']','?','-','_','+','~','<','>','i','!','l','I',';',':',',','"','^','`','\'','.',' ']
# looks better imo
ASCII_CHARS_NORMALIZED = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']
DEFAULT_WIDTH = 150

def scale_image(image, new_width):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image):
    pixels_in_image = list(image.getdata())

    depth = len(ASCII_CHARS_NORMALIZED) - 1
    
    pixels_to_chars = [ASCII_CHARS_NORMALIZED[best_match_dither(pixel_value, depth)] for pixel_value in pixels_in_image]

    return "".join(pixels_to_chars)

def best_match_dither(pixel_brightness, depth):
    # debug
    print(f'Brightness {pixel_brightness}, Depth {depth}, Index {int(depth*(pixel_brightness/255))}')
    return int(depth*(pixel_brightness/255))

def convert_image(image, new_width=DEFAULT_WIDTH):
    image = scale_image(image, new_width)
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

        # Set new width
        try:
            new_width = int(sys.argv[2])
        except:
            # No width given, set to default
            new_width = DEFAULT_WIDTH

        ascii_image = convert_image(image, new_width)
        print(ascii_image)

        font_size=12

        root = tk.Tk()
        root.option_add('*Font', f'{font_size}')

        asciiFont = font.Font(root=root, family="Square", size=9)

        (original_width, original_height) = image.size
        aspect_ratio = original_height/float(original_width)
        new_height = int(aspect_ratio * new_width)

        root.geometry(f"300x300")

        text = tk.Text(root, height=(new_height * font_size), width=(new_width * font_size), font=asciiFont)
        text.pack()
        text.insert(tk.END, ascii_image)

        #debug grayscale
        debugTop = Toplevel()
        debugTop.title('Grayscale')
        debugTop.wm_geometry('300x300')
        debugTop.resizable(width = True, height = True)

        debugImage = ImageTk.PhotoImage(convert_to_grayscale(image))
        panel = Label(debugTop, image = debugImage)
        panel.image = debugImage
        panel.grid(row=2)

        root.mainloop()
