import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)

# Define the coordinates for cropping (y1:y2, x1:x2)
x1, y1, x2, y2 = 450, 450, 1050, 1050  # Adjust these values for smaller cropping

# Crop the image
cropped_image = image[y1:y2, x1:x2]

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original BGR Image")
plt.axis('off')

# Cropped BGR Image
plt.subplot(1, 2, 2)
plt.imshow(cropped_image_rgb)
plt.title("Cropped BGR Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_cropped_images.png')

plt.show()
