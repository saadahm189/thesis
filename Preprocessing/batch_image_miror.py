from PIL import Image
import os


def flip_images_in_folder(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            # Open the image
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)

            # Flip the image horizontally
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

            # Save the flipped image to the output folder
            output_path = os.path.join(output_folder, filename)
            flipped_img.save(output_path)


# Main function where python will began execution
if __name__ == "__main__":
    # For each folder to be processed:
    for x in range(0, 38):
        # Set input and output folder paths
        # Input folder:
        input_folder = "path" + str(x)
        # Output folder:
        output_folder = "path" + str(x)

        # Mirror images
        flip_images_in_folder(input_folder, output_folder)

        # Print status
        print("Completed folder number ", x)
