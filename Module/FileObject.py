#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def getFile(dicPath,fileExten=[]):
    if not os.path.isdir(dicPath):
        error = dicPath+'dicPath is not dir'
        raise IOError(error)
        return None
    dirList = [dicPath]
    fileList = []
    for path in dirList:
        allFile = [path+'/'+thisFile for thisFile in os.listdir(path) if not thisFile.startswith('.')]
        dirList.extend([thisFile for thisFile in allFile if os.path.isdir(thisFile)])
        if len(fileExten) == 0:
            print(fileExten)
            fileList.extend(allFile)
        else:
            fileList.extend([thisFile for thisFile in allFile if os.path.splitext(thisFile)[1][1:] in fileExten])
    print('\n===========================================\n\n'+fileList)
