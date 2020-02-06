import os
import time
from PIL import Image
#from resizeimage import resizeimage

# version number
VERSION = 1.1

"""James' Logo adding tool for StartUp Algonquin -
It adds the StartUp Algonquin logo to batches of photos
Version 1.1"""

# Load the image
print("This is James' logo adding tool version %d" %(VERSION))
print("\n**************************\n")

# gets the logo file number with extension from the user
LOGO_FILENAME = input("Enter a file name: ")

# loads the image, size, and the ratio
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
logoRatio = logoHeight / logoWidth

# checks if directory withLogo exists, if not create one
if not os.path.exists('withLogo'):
    os.makedirs('withLogo')

# gets the ratio of the logo to the images from user input
LOGO_RATIO = int(input("Enter the logo ratio to the image width: "))

# timer start
start = time.clock()
count = 0

# loop over all photos in a directory
for filename in os.listdir('.'):
    if not (filename.endswith('.jpg') or filename.endswith('.JPG') \
	    or filename.endswith('.jpeg') or filename.endswith('.JPEG')) \
	or filename == LOGO_FILENAME:
	    continue

    im = Image.open(filename) 
    imWidth, imHeight = im.size
    logoWidth = int(imWidth / LOGO_RATIO)
    logoHeight = int(logoWidth * logoRatio)
    logoIm = logoIm.resize((logoWidth, logoHeight), Image.ANTIALIAS)

    print('Adding %s to %s...' %(LOGO_FILENAME, filename))
    im.paste(logoIm, (0, 0), logoIm)

    # save the images in a new folder
    im.save(os.path.join('withLogo', filename))
    
    count += 1
	
# timer end
end = time.clock() - start
print("\n**************************\n")
print("%d files done in %d seconds." %(count, end))
