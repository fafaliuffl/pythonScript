#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from PIL import Image
import fileObject

def getIconeFilePath(filePath):
    return fileObject.getFile(filePath,['appiconset'])[0]

#需要更新的路径放这里
newImagePath = ''

replaceImagePath = getIconeFilePath(os.getcwd()+'/..')
replaceImageList = fileObject.getFile(replaceImagePath,['png'])
newImageList = fileObject.getFile(newImagePath,['png'])
for imagePath in replaceImageList:
    image = Image.open(imagePath)
    imageSize = image.size
    for newImagePath in newImageList:
        newImage = Image.open(newImagePath)
        newImageSize = newImage.size
        if newImageSize == imageSize:
            shutil.copyfile(newImagePath,imagePath)
            break

            