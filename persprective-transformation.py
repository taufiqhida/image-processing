import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)  # Load as BGR

# Define the transformation matrix
# For example, here's a matrix for scaling and rotation
# You can adjust this matrix for your specific transformation needs
# This matrix performs scaling by 1.5 in x and y directions, and rotation of 45 degrees clockwise
# You can modify this matrix according to your desired affine transformation
affine_matrix = np.float32([[1.5, 0.5, 0], [0.5, 1.5, 0]])

# Apply the affine transformation to the image
transformed_image = cv2.warpAffine(image, affine_matrix, (int(image.shape[1] * 1.5), int(image.shape[0] * 1.5)))

# Plotting
plt.figure(figsize=(10, 5))

# Original BGR Image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original BGR Image")
plt.axis('off')

# Transformed BGR Image
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB))
plt.title("Transformed BGR Image")
plt.axis('off')

# Save the displayed plot automatically
plt.savefig('original_and_transformed_images.png')

plt.show()
