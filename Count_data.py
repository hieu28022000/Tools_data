import os
import glob
arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for dir_path in glob.glob('data/*.txt'):
    #print(dir_path)        
    f = open(dir_path,'r')
    l=(sum(1 for _ in f))
    #print(l)
    f = open(dir_path,'r')
    for _ in range(l):
        a=f.readline()
        a = a.split()
        a =int(a[0])
        arr[a]=arr[a]+1
print(arr)
#[1320, 62, 13268, 14, 112, 353, 3914, 142, 47, 416, 482, 3043, 493, 19]
