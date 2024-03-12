import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"aku1.png", 1)
# Loading the image

resized_30x30 = cv2.resize(image, (30, 30))
resized_90x90 = cv2.resize(image, (90, 90))
resized_120x120 = cv2.resize(image, (120, 120), interpolation=cv2.INTER_LINEAR)

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resized_30x30 = cv2.cvtColor(resized_30x30, cv2.COLOR_BGR2RGB)
resized_90x90 = cv2.cvtColor(resized_90x90, cv2.COLOR_BGR2RGB)
resized_120x120 = cv2.cvtColor(resized_120x120, cv2.COLOR_BGR2RGB)

Titles = ["Original", "Resized 30x30", "Resized 90x90", "Resized 120x120"]
images = [image, resized_30x30, resized_90x90, resized_120x120]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

# Save the displayed plot automatically
plt.savefig('original_and_risize-30-90-120.png')

plt.show()
