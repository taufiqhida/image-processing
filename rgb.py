import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original BGR Image")
plt.axis('off')

# RGB Image
plt.subplot(1, 2, 2)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_rgb_images.png')

plt.show()
