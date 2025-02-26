#!/usr/bin/env python3
from PIL import Image
import numpy as np
import sys

def analyze_texture(path):
    """Analyze image texture and color patterns."""
    with Image.open(path) as img:
        # Convert to numpy array for analysis
        img_array = np.array(img)
        
        # Get color channels
        r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
        
        # Calculate variance (high variance might indicate texture)
        r_var = np.var(r)
        g_var = np.var(g)
        b_var = np.var(b)
        
        print(f"Color variance (higher = more texture):")
        print(f"Red channel variance: {r_var:.2f}")
        print(f"Green channel variance: {g_var:.2f}")
        print(f"Blue channel variance: {b_var:.2f}")
        
        # Get unique colors in central region
        center_y, center_x = img_array.shape[0]//2, img_array.shape[1]//2
        center_region = img_array[center_y-100:center_y+100, center_x-100:center_x+100]
        unique_colors = np.unique(center_region.reshape(-1, 3), axis=0)
        
        print(f"\nUnique colors in center region: {len(unique_colors)}")
        print("\nSample of center region colors (RGB):")
        for color in unique_colors[:5]:
            print(f"RGB{tuple(color)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_texture(sys.argv[1])
    else:
        print("Please provide an image path")