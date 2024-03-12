import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)  # Load as BGR

# Define padding size
top, bottom, left, right = 200, 200, 200, 200  # Increase the padding size

# Add padding to the image
padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(0, 0, 0))

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original BGR Image")
plt.axis('off')

# Padded BGR Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(padded_image, cv2.COLOR_BGR2RGB))
plt.title("Padded BGR Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_padded_images.png')

plt.show()
