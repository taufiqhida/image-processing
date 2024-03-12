import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)  # Load as BGR

# Define the translation matrix
tx, ty = 150, 200  # Translation in x and y directions
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply translation to the image
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original BGR Image")
plt.axis('off')

# Translated BGR Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
plt.title("Translated BGR Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_translated_images.png')

plt.show()
