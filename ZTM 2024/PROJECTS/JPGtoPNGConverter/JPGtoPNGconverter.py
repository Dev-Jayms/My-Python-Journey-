import sys
import os
from PIL import Image

# grab first and second arguments
image_folder = sys.path[0]
output_folder = sys.path[1]
# print(image_folder)
# print(output_folder)
# # check if new/exist, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png",format="png")
    print(f"{filename} saved")
