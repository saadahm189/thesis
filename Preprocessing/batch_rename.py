import os


def rename_files(folder_path, symbol):
    # Get list of files in the folder
    files = os.listdir(folder_path)

    # Sort the files alphabetically
    files.sort()

    # Counter for serial numbering
    counter = 1

    # Iterate through files and rename them
    for file_name in files:
        # Split the file name and extension
        base_name, extension = os.path.splitext(file_name)

        # Create new file name with serial number
        new_name = f"class{symbol}{counter}{extension}"

        # Construct full paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        # Increment the counter
        counter += 1


#  Main function where python will began execution
if __name__ == "__main__":
    # For each folder to be processed:
    for x in range(0, 38):
        # Set input and output folder paths
        folder_path = "Processed/newData/" + str(x)
        symbol = x

        # Rename images
        rename_files(folder_path, symbol)

        # Print status
        print("Completed folder number ", x)
