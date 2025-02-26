#!/usr/bin/env python3
from PIL import Image
import sys

def describe_image(path):
    """Print basic information about an image file."""
    with Image.open(path) as img:
        print(f"Image Size: {img.size}")
        print(f"Mode: {img.mode}")
        print(f"Format: {img.format}")
        # Get the dominant colors from the image
        colors = img.getcolors(img.size[0] * img.size[1])
        if colors:
            colors.sort(reverse=True)
            print(f"Most common colors (RGB): {colors[:3]}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        describe_image(sys.argv[1])
    else:
        print("Please provide an image path")