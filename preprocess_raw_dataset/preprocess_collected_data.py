import os
from PIL import Image, ExifTags
from tqdm import tqdm

# Function to resize images in a folder, rename them, and save them to another folder
def resize_and_rename_images(source_folder, destination_folder, target_size=(224, 224)):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through subfolders in the source folder
    for subfolder_name in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder_name)
        
        # Create a subdirectory in the destination folder
        output_subfolder = os.path.join(destination_folder, subfolder_name)
        os.makedirs(output_subfolder, exist_ok=True)

        # Initialize counter for renaming images
        image_count = 1

        # Initialize tqdm progress bar
        progress_bar = tqdm(os.listdir(subfolder_path), desc=f'Resizing images in class {subfolder_name}')

        # Iterate through images in the subfolder
        for filename in progress_bar:
            file_path = os.path.join(subfolder_path, filename)
            
            # Open the image and check orientation
            with Image.open(file_path) as img:
                # Check if the image has orientation metadata
                if hasattr(img, '_getexif'):
                    exif = img._getexif()
                    if exif is not None:
                        # Get the orientation tag
                        orientation = exif.get(0x0112)
                        
                        # Rotate the image if necessary
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)

                # Resize the image
                img_resized = img.resize(target_size, Image.LANCZOS)

                # Rename the image
                new_filename = f"class-{subfolder_name}-{image_count}.jpg"
                image_count = image_count +1

                # Save the resized and renamed image to the destination folder
                output_file_path = os.path.join(output_subfolder, new_filename)
                img_resized.save(output_file_path)

                # Update tqdm progress bar
                progress_bar.set_postfix({'File': new_filename})

# Path to the source folder containing subfolders with images
source_folder_path = "F:/datasets/dataset"

# Path to the destination folder where resized and renamed images will be saved
destination_folder_path = "F:/thesis/data"

# Resize and rename images and save them to the destination folder
resize_and_rename_images(source_folder_path, destination_folder_path)