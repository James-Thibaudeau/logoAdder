import os
import time
from PIL import Image

"""James' Logo adding tool for StartUp Algonquin -
It adds the StartUp Algonquin logo to batches of photos
Version 1.0 Python 2.7"""

#Load the image
SQUARE_FIT_SIZE = 300.0
print "This is James' logo adding tool version 1.0 FOR PYTHON 2.7"
print "\n**************************\n"

LOGO_FILENAME = raw_input("Enter a file name: ")

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

if not os.path.exists('withLogo'):
    os.makedirs('withLogo')

# change this ratio variable according to the width of the image
ratio = 4
aspRatio = 0.3804262036
#Timer start
start = time.clock()
count = 0

#Loop over all photos in a directory
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) \
		or filename == LOGO_FILENAME:
		continue

	im = Image.open(filename) 
	imWidth, imHeight = im.size
	logoWidth = int(imWidth / ratio)
	logoHeight = int(logoWidth * aspRatio)
	logoIm = logoIm.resize((logoWidth, logoHeight), Image.ANTIALIAS)

	print 'Adding %s to %s...' %(LOGO_FILENAME, filename)
	im.paste(logoIm, (0, 0), logoIm)

	#save the images in a new folder
	im.save(os.path.join('withLogo', filename))
	
	count += 1
	
#Timer end
end = time.clock() - start
print "\n**************************\n"
print "%d files done in %d seconds." %(count, end)