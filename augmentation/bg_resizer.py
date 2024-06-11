import os
from PIL import Image

# Define the folder containing the images and the desired size
folder_path = 'augmentation/background'
output_folder = 'augmentation/background_resized'
desired_size = (224, 224)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize a counter for the naming
counter = 1

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Add more formats if needed
        image_path = os.path.join(folder_path, filename)
        
        with Image.open(image_path) as img:
            # Resize the image
            img_resized = img.resize(desired_size, Image.LANCZOS)
            
            # Generate the new filename
            new_filename = f'bg{counter:02d}.jpg'  # Change the extension if needed
            
            # Save the resized image to the output folder with the new name
            output_path = os.path.join(output_folder, new_filename)
            img_resized.save(output_path)
            
            # Increment the counter
            counter += 1

print("All images have been resized, renamed, and saved to the output folder.")
