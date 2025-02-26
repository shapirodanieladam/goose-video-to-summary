#!/usr/bin/env python3
from PIL import Image
import sys
import os

def save_thumbnail(path, size=(800, 600)):
    """Create a thumbnail of the image."""
    output_path = path.replace('.jpg', '_thumb.jpg')
    with Image.open(path) as img:
        img.thumbnail(size)
        img.save(output_path)