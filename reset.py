import os
from shutil import rmtree
arr = os.listdir()
print(arr)
cwd = os.getcwd()
open("hotelnumbersmall.txt", "w").write('0')
open("hotelnumbermedium.txt", "w").write('0')
open("hotelnumberbig.txt", "w").write('0')
for file in arr:
    print(file)
    if "small" in file or "medium" in file or "big" in file:
        if 'hotel' not in file:
            rmtree(cwd + "\\" + file)