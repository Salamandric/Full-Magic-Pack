import sys
import os
from PIL import Image

dir_path = sys.argv[1]

for filename in os.listdir(dir_path):
	file_path = os.path.join(dir_path, filename)
	try:
		img = Image.open(file_path)
	except IOError:
		continue
	width = img.width
	if width == 523:
		img_rotated = img.rotate(90, expand=True)
		img_rotated.save(file_path)
		print (filename + " rotated.")
