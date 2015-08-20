from math import *
import sys
import re
import numpy as np
import cv2
import sys
from collections import *

def distance(a, b):
    return sqrt(sum((a - b) ** 2 for a, b in zip(a, b)))

def classify(a, dataset):
    distances = []
    for item in dataset:
        distances.append(((distance(a, item[0])), item[1]))
    return sorted(distances)[0][1]

images = []

characters = ["F", "M"]

# Get raw text as string.
with open("color_data.txt") as f:
    data = f.read()

values = re.findall(r'.*?:', data)
labels = re.findall(r': .*?\n', data)

color_data = []

for i in range(len(labels)):
    values[i] = values[i].replace(":", "")
    labels[i] = labels[i].replace(": ", "").replace("\n", "")
    color_data.append((([int(x) for x in values[i].split(',')]), labels[i]))

for character in characters:
    for i in range(1):
        print character+"{0}.png".format(i)
        img = cv2.imread("characters/"+character+"{0}.png".format(i))

        width = img.shape[0]
        height = img.shape[1]

        pixels = []

        # For every pixel in the image:
        for x in range(height):
            for y in range(width):
                red = img[y, x, 2]
                green = img[y, x, 1]
                blue = img[y, x, 0]
                if(classify([red, green, blue], color_data) == "brown"):
                    pixels.append(1)
                else:
                    pixels.append(0)

        images.append((pixels, character))

def arrayOutput(img):
    img = cv2.imread(img)

    width = img.shape[0]
    height = img.shape[1]

    pixels = []

    # For every pixel in the image:
    for x in range(height):
        for y in range(width):
            red = img[y, x, 2]
            green = img[y, x, 1]
            blue = img[y, x, 0]
            if(classify([red, green, blue], color_data) == "brown"):
                pixels.append(1)
            else:
                pixels.append(0)
    return pixels

print classify(arrayOutput("classify/classF.png"), images)
