#!/usr/bin/env python3

from PIL import Image
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# Define relative paths from the script directory
image_location = os.path.join(script_dir, "images")
save_location = os.path.join(script_dir, "opt","icons")

os.makedirs(save_location, exist_ok=True)

for filename in os.listdir(image_location):
    if filename[0] != '.':
        filepath= os.path.join(image_location,filename)
        image= Image.open(filepath)
        newimage= image.rotate(270).resize((128,128)).convert('RGB')
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}.jpeg"
        new_path = os.path.join(save_location, new_filename)
        newimage.save(new_path)