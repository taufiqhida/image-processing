import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"aku1.png", 1)  # Load as BGR

# Split the color channels
blue_channel = image[:, :, 0]
green_channel = image[:, :, 1]
red_channel = image[:, :, 2]

# Plotting
plt.figure(figsize=(15, 5))

# Original BGR Image
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
plt.title("Original BGR Image")
plt.axis('off')

# Blue Channel Image
plt.subplot(1, 4, 2)
plt.imshow(blue_channel, cmap='Blues')  # Display in blue colormap
plt.title("Blue Channel")
plt.axis('off')

# Green Channel Image
plt.subplot(1, 4, 3)
plt.imshow(green_channel, cmap='Greens')  # Display in green colormap
plt.title("Green Channel")
plt.axis('off')

# Red Channel Image
plt.subplot(1, 4, 4)
plt.imshow(red_channel, cmap='Reds')  # Display in red colormap
plt.title("Red Channel")
plt.axis('off')

plt.tight_layout()

# Save the displayed plot automatically
plt.savefig('original_and_color_channels.png')

plt.show()
