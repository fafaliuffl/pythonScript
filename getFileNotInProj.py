#!/usr/bin/env python

import Module
import os

fileList = [os.path.basename(filePath) for filePath in Module.FileObject.getFile('/Users/liuyudi/PKGame/Normal/kxd-ios/kxd',['m','mm','xib'])]
objectFile = Module.FileObject.getFile('/Users/liuyudi/PKGame/Normal/kxd-ios',['pbxproj'])
for filePath in objectFile:
    file1 = open(filePath)
    fileCode = file1.read()
    fileList = [fileName for fileName in fileList if fileName not in fileCode]
print(fileList)