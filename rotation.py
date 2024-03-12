import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)  # Load as BGR

# Rotate the image (90 degrees clockwise)
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original BGR Image")
plt.axis('off')

# Rotated BGR Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.title("Rotated BGR Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_rotated_images.png')

plt.show()
