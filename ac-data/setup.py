import os
import fileinput
# from shutil import copyfile

filename = './ac-data/runTmp.bat'

print(os.getcwd())

if(not(os.path.exists('gw2.exe')) and not(os.path.exists('gw2-64.exe'))):
    print('Error: Could not find the Guild Wars 2 executable in this folder!')
    exit(15)

lines = []
with open(filename) as inFile:
    for line in inFile:
        print("LINE:",line)
        if line.strip() == "echo You forgot to run install.bat or setup.py first!" or line.strip() == "goto:eof":
            continue
        lines.append(line.replace('replaceMe', os.getcwd()))

with open('run.bat','w') as outFile:
    for line in lines:
        outFile.write(line)