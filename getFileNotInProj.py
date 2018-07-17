#!/usr/bin/env python

import fileObject
import os

fileList = [os.path.basename(filePath) for filePath in fileObject.getFile(os.getcwd()+'/../kxd',['h','m','mm','xib'])]
objectFile = fileObject.getFile(os.getcwd()+'/..',['pbxproj'])
for filePath in objectFile:
    file1 = open(filePath)
    fileCode = file1.read()
    fileList = [fileName for fileName in fileList if fileName not in fileCode]
print(fileList)