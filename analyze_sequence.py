#!/usr/bin/env python3
from PIL import Image
import sys

def describe_frames(start_num, count):
    """Print basic information about a sequence of frames."""
    for i in range(start_num, start_num + count):
        frame_path = f"frames/frame_{i:04d}.jpg"
        print(f"\nFrame {i}:")
        try:
            with Image.open(frame_path) as img:
                print(f"Size: {img.size}")
                # Get the average brightness
                brightness = sum(img.convert('L').getdata()) / (img.size[0] * img.size[1])
                print(f"Average brightness: {brightness:.1f}/255")
                # Get dominant colors
                colors = img.convert('RGB').getcolors(img.size[0] * img.size[1])
                if colors:
                    colors.sort(reverse=True)
                    print("Top 3 colors (count, RGB):")
                    for count, color in colors[:3]:
                        print(f"  {count} pixels: RGB{color}")
        except FileNotFoundError:
            print(f"Frame {i} not found")

if __name__ == "__main__":
    describe_frames(1, 5)