import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)  # Load as BGR

# Flip the image horizontally
flipped_image = cv2.flip(image, 1)

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original BGR Image")
plt.axis('off')

# Flipped BGR Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB))
plt.title("Flipped BGR Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_flipped_images.png')

plt.show()
