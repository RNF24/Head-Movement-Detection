import cv2
from PIL import Image, ImageOps
import numpy as np
import glob
import os

# Input and output directories
input_directory1 = r'YOUR_DESIRED_LOCATION'
input_directory2 = r'YOUR_DESIRED_LOCATION'
output_directory = r'YOUR_DESIRED_LOCATION'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def apply_histo(input_dir, output_directory):
    for filename in glob.glob(os.path.join(input_dir, '*.png')):
        im = Image.open(filename)

        histo_image = ImageOps.equalize(im, mask = None)

        output_filename = os.path.join(output_directory, os.path.basename(filename))
        cv2.imwrite(output_filename, np.array(histo_image))
        print(f'Saved: {output_filename}')

# Apply clahe to images in input_directory1 and input_directory2
apply_histo(input_directory1, output_directory)
apply_histo(input_directory2, output_directory)