from PIL import Image

# Open the background image
background = Image.open('test/bg/bg (9).jpg')  # Replace with your background image file


# Open the foreground image with transparent background (PNG)
foreground = Image.open('test/hand/hand (1).png')  # Replace with your foreground image file


background = background.convert('RGBA')    # Ensure background is in RGBA mode


foreground = foreground.convert('RGBA')    # Ensure foreground is in RGBA mode

# Optional: Resize foreground image if necessary
foreground = foreground.resize((224, 224))  # Example resizing, adjust as needed
background = background.resize((224, 224))  # Example resizing, adjust as needed

# Position where foreground image will be placed on background
position = (0, 0)  # Adjust the position as needed

# Create a new image by combining the two
combined = Image.alpha_composite(background, Image.new('RGBA', background.size))
combined.paste(foreground, position, foreground)

# Save the combined image
combined.save('combined_image.png')
