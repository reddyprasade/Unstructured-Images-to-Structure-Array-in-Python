# load and display an image with Matplotlib
from matplotlib import image
import numpy as np
from matplotlib import pyplot



# load image as pixel array
image = image.imread('Reddy.png')

# summarize shape of the pixel array
print(image.dtype)
print(image.shape)

# Convert to array
print(image)

# How to Save the array into File
data = np.ravel(image)
np.savetxt('Matplotlib_Data.txt',data)

# display the array of pixels as an image
pyplot.imshow(image)
pyplot.show()
