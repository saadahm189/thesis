import torch
import torchvision.transforms as T
from PIL import Image, ImageFilter
import os
import random
import numpy as np
from tqdm import tqdm  # Import tqdm for progress bar

# Load the pre-trained DeepLabV3 model
model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet101', pretrained=True)
model.eval()

# Preprocess input images
def preprocess(image):
    # Convert RGBA image to RGB
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    preprocess_transform = T.Compose([
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess_transform(image)

# Get the mask for hand and body parts
def get_segmentation_mask(image):
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)['out'][0]
    output_predictions = output.argmax(0).byte().cpu().numpy()
    
    # Create mask for the hand and body parts (assuming class indices for person are used)
    mask = (output_predictions == 15).astype(np.uint8) * 255  # Class 15 in COCO dataset is 'person'
    
    # Apply a slight blur to the mask to soften the edges
    mask = Image.fromarray(mask).filter(ImageFilter.GaussianBlur(radius=2))
    
    return mask

def overlay_hand_on_background(hand_img, background_img, mask):
    # Ensure images are in RGBA format
    hand_img = hand_img.convert("RGBA")
    background_img = background_img.convert("RGBA")
    
    # Resize background to match hand image size if needed
    background_img = background_img.resize(hand_img.size)
    
    # Apply the mask to the hand image to keep hand and body parts
    hand_img_np = np.array(hand_img)
    background_img_np = np.array(background_img)
    mask_np = np.array(mask)
    
    # Ensure mask has the same shape as input images
    mask_np = np.expand_dims(mask_np, axis=-1)  # Add singleton dimension for channels
    
    # Perform alpha composition with proper blending
    alpha = mask_np / 255.0
    combined_img_np = (alpha * hand_img_np + (1 - alpha) * background_img_np).astype(np.uint8)
    combined_img = Image.fromarray(combined_img_np, 'RGBA')
    
    return combined_img

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(folder, filename)).convert("RGBA")
            images.append(img)
    return images

def save_image(image, filename):
    # Convert RGBA to RGB before saving as JPEG
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image.save(filename)

def augment_dataset(dataset_folder, background_folder, output_folder, num_augmentations=3):
    # Load background images
    backgrounds = load_images_from_folder(background_folder)
    
    # Process each class folder in the dataset
    for class_folder in tqdm(os.listdir(dataset_folder), desc="Augmenting dataset"):
        class_path = os.path.join(dataset_folder, class_folder)
        output_class_path = os.path.join(output_folder, class_folder)
        os.makedirs(output_class_path, exist_ok=True)

        # Load and process each image in the class folder
        for image_file in tqdm(os.listdir(class_path), desc=f"Augmenting {class_folder}", leave=False):
            if image_file.endswith(".jpg") or image_file.endswith(".png"):
                image_path = os.path.join(class_path, image_file)
                hand_img = Image.open(image_path).convert("RGBA")
                
                # Save the original image in the output folder
                save_image(hand_img, os.path.join(output_class_path, image_file))
                
                # Get the segmentation mask
                mask = get_segmentation_mask(hand_img)
                
                for i in range(num_augmentations):
                    background_img = random.choice(backgrounds)
                    augmented_img = overlay_hand_on_background(hand_img, background_img, mask)
                    
                    # Save the augmented image
                    output_filename = f"{os.path.splitext(image_file)[0]}_aug_{i}.png"
                    output_path = os.path.join(output_class_path, output_filename)
                    augmented_img.save(output_path)

# Paths
dataset_folder = 'path/to/dataset'
background_folder = 'path/to/backgrounds'
output_folder = 'path/to/output'

# Perform augmentation
augment_dataset(dataset_folder, background_folder, output_folder, num_augmentations=3)