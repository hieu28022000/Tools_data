import glob
import os

for name in glob.glob('images/*.txt'):
    fix_name = name.split('_')
    new_name = str(fix_name[0] + '_' + fix_name[1] + '.txt')
    os.rename(str(name), new_name)