import os
import fileinput
from shutil import copyfile

filename = 'ac-data/run.bat'

if(not(os.path.exists('gw2.exe')) and not(os.path.exists('gw2-64.exe'))):
    print('Error: Could not find the Guild Wars 2 executable in this folder!')
    exit(15)

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('potato', os.getcwd()), end='')

copyfile('ac-data/runTmp.bat','run.bat')
    