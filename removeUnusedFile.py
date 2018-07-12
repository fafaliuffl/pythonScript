#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import fileObject

path = os.getcwd()+'/../kxd'
allFileList = []
allFileList.extend(fileObject.getFile(path,['m','mm','h']))
needRemoveFile = []
needRemoveFile.extend(fileObject.getFile(path+'/ui',['h']))
needRemoveFile.extend(fileObject.getFile(path+'/components',['h']))
needRemoveFile.extend(fileObject.getFile(path+'/ViewLogic',['h']))
needRemoveFile.extend(fileObject.getFile(path+'/ViewModel',['h']))
needRemoveFile.extend(fileObject.getFile(path+'/Logic',['h']))
needRemoveFile.extend(fileObject.getFile(path+'/models',['h']))
for allFilePath in allFileList:
    index = len(needRemoveFile)-1
    while index > 0:
        filePath = needRemoveFile[index]
        allFileName = os.path.splitext(allFilePath)[0]
        fileName = os.path.splitext(filePath)[0]
        if allFileName != fileName :
            try:
                thisFile = open(filePath,encoding='utf8')
            except IOError as e:
                print('open file=====>'+filePath+' error')
            else:
                try:
                    codeString = thisFile.read()
                except IOError as e:
                    print('readFile===>'+filePath+' error')
                else:
                    if fileName+'.h' in codeString:
                        needRemoveFile.pop(index)
                finally:
                    thisFile.close()
print('\n\n===============================\n')
print(needRemoveFile)