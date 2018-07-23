import fileObject
import os
import shutil

codePath = os.getcwd()+'/..'
fileList = fileObject.getFile(codePath,['png','jpg','jpeg'])
for imagePath in fileList:
    imageName = os.path.basename(imagePath)
    shutil.copytree(imagePath,codePath+'/imageFile')