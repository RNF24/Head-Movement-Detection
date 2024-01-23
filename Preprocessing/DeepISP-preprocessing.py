import cv2
from PIL import Image
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

def apply_deep_isp(input_dir, output_directory):
    for filename in glob.glob(os.path.join(input_dir, '*.png')):
        image = Image.open(filename)

        # Convert PIL Image to NumPy array
        image_np = np.array(image)

        brightness = 20
        contrast = 1.5
        enhanced_image = cv2.convertScaleAbs(image_np, alpha=contrast, beta=brightness)
        enhanced_frame = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
        output_filename = os.path.join(output_directory, os.path.basename(filename))
        cv2.imwrite(output_filename, np.array(enhanced_frame))
        print(f'Saved: {output_filename}')

# Apply clahe to images in input_directory1 and input_directory2
apply_deep_isp(input_directory1, output_directory)
apply_deep_isp(input_directory2, output_directory)