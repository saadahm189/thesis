import os
from PIL import Image

# Paths to the directories
foreground_dir = 'test/hand'  # Directory containing foreground images
background_dir = 'test/bg'    # Directory containing background images
output_dir = 'test/output'    # Directory to save combined images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get lists of all foreground and background images
foreground_images = [f for f in os.listdir(foreground_dir) if f.endswith('.png')]
background_images = [f for f in os.listdir(background_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

print(f"Found {len(foreground_images)} foreground images and {len(background_images)} background images.")

# Process each foreground image
for fg_image_name in foreground_images:
    try:
        foreground_path = os.path.join(foreground_dir, fg_image_name)
        foreground = Image.open(foreground_path).convert('RGBA')
        foreground = foreground.resize((224, 224))  # Adjust size as needed
        
        print(f"Processing foreground image: {fg_image_name}")
        
        # Process each background image
        for bg_image_name in background_images:
            try:
                background_path = os.path.join(background_dir, bg_image_name)
                background = Image.open(background_path).convert('RGBA')
                background = background.resize((224, 224))  # Adjust size as needed
                
                print(f"Combining with background image: {bg_image_name}")
                
                # Create a new image by combining the two
                combined = Image.alpha_composite(background, Image.new('RGBA', background.size))
                combined.paste(foreground, (0, 0), foreground)

                # Save the combined image
                combined_image_name = f"{os.path.splitext(fg_image_name)[0]}_{os.path.splitext(bg_image_name)[0]}.png"
                combined.save(os.path.join(output_dir, combined_image_name))
                
                print(f"Saved combined image: {combined_image_name}")
                
            except Exception as e:
                print(f"Error processing background image {bg_image_name}: {e}")
    
    except Exception as e:
        print(f"Error processing foreground image {fg_image_name}: {e}")

print("Batch processing complete. Combined images saved in the output directory.")
