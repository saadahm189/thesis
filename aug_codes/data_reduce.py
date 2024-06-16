import os
from PIL import Image

# Define the target size in bytes
TARGET_SIZE = 15 * 1024  # 15 KB

def compress_image(image_path, output_path, quality=85):
    """Compress an image to be under the target size."""
    with Image.open(image_path) as img:
        # Convert images with an alpha channel to RGB
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(output_path, 'JPEG', quality=quality)
        while os.path.getsize(output_path) > TARGET_SIZE and quality > 10:
            quality -= 5
            img.save(output_path, 'JPEG', quality=quality)

def process_folder(input_folder, output_folder):
    """Process each image in the given folder and save to output folder."""
    for root, _, files in os.walk(input_folder):
        # Calculate the relative path to maintain folder structure
        relative_path = os.path.relpath(root, input_folder)
        subfolder_name = os.path.basename(root)
        output_dir = os.path.join(output_folder, relative_path)
        os.makedirs(output_dir, exist_ok=True)

        # Track image count in the subfolder
        image_count = 1

        for file in files:
            file_path = os.path.join(root, file)
            output_filename = f"class-{subfolder_name}-{image_count}.jpg"
            output_path = os.path.join(output_dir, output_filename)
            if os.path.getsize(file_path) > TARGET_SIZE:
                print(f"Compressing: {file_path}")
                compress_image(file_path, output_path)
            else:
                # If the image is already under 15KB, just copy it to the output folder as JPEG
                with Image.open(file_path) as img:
                    # Convert images with an alpha channel to RGB
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(output_path, 'JPEG')
            image_count += 1

# Replace these with the paths to your source and destination folders
input_folder_path = 'data'
output_folder_path = 'reduced_data'
process_folder(input_folder_path, output_folder_path)
