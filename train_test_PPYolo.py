import glob
import os
import numpy as np

num_val = len(glob.glob('images/*')) // 5
print('Train case : Valid case = 8:2')

all_images = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image = glob.glob(os.path.join("images", ext))
  all_images += image

rand_idx = np.random.randint(0, len(all_images), num_val)

for i in range(len(all_images)):
    
    if i not in rand_idx:
        img = all_images[i]
        file_name = img.split('\\')[1].split('.')[0]
        image_name = './images/' + str(file_name) + '.jpg'
        annotation_name = './annotations/' + str(file_name) + '.xml'
        
        if os.path.exists(annotation_name) == True:
            new_file=open('train.txt', mode="a+", encoding="utf-8")
            new_file.write(image_name + ' ' + annotation_name + "\n")
            new_file.close()
    
    if i in rand_idx:
        img = all_images[i]
        file_name = img.split('\\')[1].split('.')[0]
        image_name = './images/' + str(file_name) + '.jpg'
        annotation_name = './annotations/' + str(file_name) + '.xml'
        
        if os.path.exists(annotation_name) == True:
            new_file=open('valid.txt', mode="a+", encoding="utf-8")
            new_file.write(image_name + ' ' + annotation_name + "\n")
            new_file.close()
    

