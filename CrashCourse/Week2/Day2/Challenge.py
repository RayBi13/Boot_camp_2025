

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d olgabelitskaya/flower-color-images

!unzip flower-color-images.zip

!pip install tensorflow
! pip install keras
! pip install pillow

# Load an image using PIL
from PIL import Image
image_path = '0010.png'
original_image = Image.open(image_path)

# Display the original image using matplotlib
import matplotlib.pyplot as plt
plt.imshow(original_image)

# Rotate an image by 90 degrees

from scipy.ndimage import rotate

from scipy import misc

# def rotate_image_90_degrees(image):
#     return rotate(image, 90, reshape=False, mode='nearest')

def rotate_image_90_degrees(original_image):
    return rotate(original_image, 90, reshape=False, mode='nearest')

# Charger une image d'exemple
# Vous pouvez remplacer cette ligne par votre propre image
rotated_image = rotate_image_90_degrees(original_image)

# showes original image and rotated image
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(original_image)
ax[0].set_title('Original Image')
ax[0].axis('off')  # Masquer les axes
ax[1].imshow(rotated_image)
ax[1].set_title('Rotated Image')
ax[1].axis('off')  # Masquer les axes
plt.show()

# Flip horizontally
from PIL import Image, ImageOps

horizontal_flip = ImageOps.mirror(original_image)

fig, axes = plt.subplots(1, 1, figsize=(6, 4)) # Only one subplot

axes.imshow(horizontal_flip)  # Display only the flipped image
axes.set_title("Horizontally Flipped")
axes.axis("off")  # Hide axes

plt.show()

vertical_flip = ImageOps.flip(original_image)

fig, axes = plt.subplots(1, 1, figsize=(6, 4))  # One subplot only

axes.imshow(vertical_flip)  # Display only the vertically flipped image
axes.set_title("Vertically Flipped")
axes.axis("off")  # Hide axes

plt.show()

width, height = original_image.size  # Get original dimensions
zoomed_image = original_image.resize((int(width * 1.2), int(height * 1.2)))  # Scale by 1.2x

fig, ax = plt.subplots(1, 1, figsize=(6, 4))  # One subplot only

ax.imshow(zoomed_image)  # Show the zoomed image
ax.set_title("Zoomed-in (1.2x)")
ax.axis("off")  # Hide axes

plt.show()

