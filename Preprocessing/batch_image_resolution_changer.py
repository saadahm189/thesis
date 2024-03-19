from PIL import Image, ExifTags
import os


def resize_images(input_folder, output_folder, target_resolution):
    # Ensure output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Iterate over each file
    for file_name in files:
        # Construct full path for input and output images
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Open the image
        img = Image.open(input_path)

        # Check for image orientation and rotate if necessary
        if hasattr(img, "_getexif"):  # Check if the image has EXIF data
            exif = img._getexif()
            if exif is not None:
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == "Orientation":
                        break
                if orientation in exif:
                    if exif[orientation] == 3:
                        img = img.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        img = img.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        img = img.rotate(90, expand=True)

        # Resize the image while preserving aspect ratio
        img.thumbnail(target_resolution, Image.LANCZOS)

        # Create a new blank image with the target resolution
        new_img = Image.new("RGB", target_resolution, (255, 255, 255))

        # Paste the resized image onto the center of the blank image
        img_width, img_height = img.size
        new_img.paste(
            img,
            (
                (target_resolution[0] - img_width) // 2,
                (target_resolution[1] - img_height) // 2,
            ),
        )

        # Save the image with the same format
        new_img.save(output_path)


#  Main function where python will began execution
if __name__ == "__main__":
    # For each folder to be processed:
    for x in range(0, 38):
        # Set input and output folder paths
        # Input folder:
        input_folder = "F:/datasets/dataset" + str(x)
        # Output folder:
        output_folder = "F:/thesis/data" + str(x)

        # Set target resolution
        target_resolution = (224, 224)

        # Resize images
        resize_images(input_folder, output_folder, target_resolution)

        # Print status
        print("Completed folder number ", x)
