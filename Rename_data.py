import os
import glob
numb=0
name=input("Nhap ten: ")
for file in glob.glob('*.jpg'):
    print(file)
    name_b = name + str(numb)+".jpg"
    os.rename(file,name_b)
    numb+=1
print('Done')