import numpy as np
from PIL import Image

# Path of Images
IMAGE1 = "sample images/image1.png"
IMAGE2 = "sample images/image2.png"

# Opening Image using PIL
img1 = Image.open(IMAGE1)
img2 = Image.open(IMAGE2)

# Converting Images into Numpy Array / Matrix
rgbImage1 = np.asarray(img1, dtype="int32" )
rgbImage2 = np.asarray(img2, dtype="int32" )

# Converting RGB image to Gray Scale by computing average of RGB values
grayImage1 = np.mean(rgbImage1,axis = 2)
grayImage2 = np.mean(rgbImage2,axis = 2)

# Subtracting both Images
result = grayImage1 - grayImage2

# Forming image from array
finalImage = Image.fromarray(result)

# Storing final result
finalImage.convert("L").save("result.png")

# Displaying final result
finalImage.show()