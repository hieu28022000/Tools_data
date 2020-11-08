import os
import glob

for image in glob.glob('*.jpg'):
    name = image.split('.')[0]
    name = str(name) + '.txt'
    if os.path.exists(name) != True:
        os.remove(image)
