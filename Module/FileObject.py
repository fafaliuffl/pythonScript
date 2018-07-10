#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def getFile(dicPath,fileExten=[]):
    if not os.path.isdir(dicPath):
        raise IOError('dicPath is not dir')
        return None
    dirList = [dicPath]
    fileList = []
    for path in fileList:
        dirList.extend([path+'/'+thisFile for thisFile in os.listdir(path) if os.path.isdir(path+'/'+thisFile)])
        if len(fileExten) == 0:
            fileList.extend(os.listdir(path))
        else:
            fileList.extend([path+'/'+thisFile for thisFile in os.listdir(path) if os.path.split(path+'/'+thisFile)[1][1:] in fileExten])
    print(fileList)

