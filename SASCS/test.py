import numpy as np
import matplotlib.pyplot as plt

def display_pixel_art(pixels):
    pixels = np.array(pixels)
    plt.figure(figsize=(len(pixels[0]), len(pixels)))
    plt.imshow(pixels, interpolation='nearest')
    plt.axis('off')
    plt.show()

# Define pixel art using a 2D list of colors
pixel_art = [
    ['white', 'white', 'black', 'black', 'white', 'white'],
    ['white', 'black', 'red', 'red', 'black', 'white'],
    ['black', 'red', 'red', 'red', 'red', 'black'],
    ['black', 'red', 'red', 'red', 'red', 'black'],
    ['white', 'black', 'red', 'red', 'black', 'white'],
    ['white', 'white', 'black', 'black', 'white', 'white']
]

display_pixel_art(pixel_art)