import os
import shutil

# Function to create subfolders and move images


def organize_images(source_folder, target_folder, batch_size):
    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Iterate through the source folder and move images
    image_files = sorted(os.listdir(source_folder))
    for i in range(0, len(image_files), batch_size):
        batch = image_files[i:i + batch_size]
        subfolder_name = str(i // batch_size)
        subfolder_path = os.path.join(target_folder, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)
        for image_file in batch:
            src_path = os.path.join(source_folder, image_file)
            dst_path = os.path.join(subfolder_path, image_file)
            shutil.move(src_path, dst_path)


# Define parent folder
parent_folder = "data"

# Define target folder
target_parent_folder = "new"

# Define batch size
batch_size = 5

# Iterate through each source folder within the parent folder
for folder_name in os.listdir(parent_folder):
    source_folder = os.path.join(parent_folder, folder_name)
    target_folder = os.path.join(target_parent_folder, folder_name)
    organize_images(source_folder, target_folder, batch_size)
