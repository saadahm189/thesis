from PIL import Image, ExifTags
import os


def remove_exif_orientation(img):
    # Remove EXIF orientation metadata
    if hasattr(img, "_getexif"):
        exif = img._getexif()
        if exif is not None:
            for tag, value in exif.items():
                if tag in ExifTags.TAGS.keys() and ExifTags.TAGS[tag] == "Orientation":
                    img = apply_orientation(img, value)
    return img


def apply_orientation(img, orientation):
    if orientation == 1:
        return img
    elif orientation == 2:
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        return img.transpose(Image.ROTATE_180)
    elif orientation == 4:
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 5:
        return img.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 6:
        return img.transpose(Image.ROTATE_270)
    elif orientation == 7:
        return img.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 8:
        return img.transpose(Image.ROTATE_90)
    else:
        return img


def resize_image(input_path, output_path, max_size_kb=500):
    # Open the image
    with Image.open(input_path) as img:
        # Remove EXIF orientation metadata
        img = remove_exif_orientation(img)

        # Calculate the aspect ratio
        aspect_ratio = img.width / img.height

        # Calculate new width and height to maintain aspect ratio
        new_width = int((max_size_kb * 1024) ** 0.5 * aspect_ratio)
        new_height = int(new_width / aspect_ratio)

        # Resize the image
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Save the resized image with desired compression quality
        img.save(output_path, optimize=True, quality=95)


def resize_images_in_folder(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if (
            filename.endswith(".jpg")
            or filename.endswith(".jpeg")
            or filename.endswith(".png")
        ):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            # Resize the image
            resize_image(input_path, output_path)


#  Main function where python will began execution
if __name__ == "__main__":
    # For each folder to be processed:
    for x in range(0, 38):
        # Set input and output folder paths
        # Input folder:
        input_folder = "../../Datasets/Dataset/" + str(x)
        # Output folder:
        output_folder = "Processed/Final/" + str(x)

        # Resize images
        resize_images_in_folder(input_folder, output_folder)

        # Print status
        print("Completed folder number ", x)
