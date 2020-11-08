import os
import glob

for annotation in glob.glob('*.txt'):
    file = open(annotation)
    name_file = annotation.split('.')[0]
    info = file.read()
    lines = info.split('\n')
    for line in lines:
        if len(line) == 0:
            continue
        node = line.split(' ')
        new_file=open('annotation_fix/' + str(name_file) + ".txt",mode="a+",encoding="utf-8")
        new_file.write('1 ' + node[1] + ' ' + node[2] + ' ' + node[3] + ' ' + node[4])
        new_file.close()
    print(name_file)

print('Done')
