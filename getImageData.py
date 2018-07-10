# -*- coding: utf-8 -*-
# 本脚本需在python3环境下运行
import os
import sys
import re
import argparse
import imp

def getImageName(imagePath):
    stringList = re.compile('\S+/').findall(imagePath)
    if len(stringList) > 0:
        imageName = imagePath.replace(stringList[0],'')
    stringList = re.compile('\.\S+').findall(imageName)
    if len(stringList) > 0:
        imageName = imageName.replace(stringList[0],'')
    return imageName
def deleteAnnoationCode(codeString):
    annoationList1 = re.compile('/\*[^(/\*|\*/)]+\*/').findall(codeString)
    for string in annoationList1:
        codeString = codeString.replace(string,'')
    annoationList2 = re.compile('//.*\n').findall(codeString)
    for string in annoationList2:
        codeString = codeString.replace(string,'')
        print(string)
    return codeString

imp.reload(sys)
path = os.getcwd() + "/.." #文件夹目录
# path = '/Users/liuyudi/pkgame-ios_develop_feature'
os.chdir(path)
imageList = []
fileList = [path]
for file in fileList:
    files = os.listdir(file)
    imageList.extend([file+'/'+thisFile for thisFile in files if ('.imageset' in thisFile) and (not thisFile.startswith('{',0))])
    dirFileList = [file+'/'+thisFile for thisFile in files if  os.path.isdir(file+'/'+thisFile)]
    fileList.extend(dirFileList)
codePath = path
fileList = [codePath]
jointString = []
for file in fileList:
    files = os.listdir(file)
    for thisFile in files:
        if 'thirdparty' == thisFile:
            continue
        if thisFile.endswith('.m') or thisFile.endswith('.mm') or thisFile.endswith('.xib') or thisFile.endswith('.storyboard') or thisFile.endswith('.xml') or thisFile.endswith('.plist'):
            try :
                codeFile = open(file+'/'+thisFile,encoding='utf8')
            except IOError as e:
                print('tryError')
            else:
                try:
                    codeString = codeFile.read()
                except IOError as e:
                    print('tryopenFileError')
                else:
                    codeString = deleteAnnoationCode(codeString)
                    connectImage = re.compile('"[^"\n%:=]+%').findall(codeString)
                    jointString.extend(connectImage)
                    imageList = [thisImage for thisImage in imageList if getImageName(thisImage) not in codeString]
                    codeFile.close()
    dirFileList = [file+'/'+thisFile for thisFile in files if os.path.isdir(file+'/'+thisFile) and not thisFile == 'Pods' and '.' not in thisFile]
    fileList.extend(dirFileList)
index = len(imageList) - 1
while (index >= 0):
    thisImage = imageList[index]
    thisImage = getImageName(thisImage)
    for joint in jointString:
        string = joint[1:-1]
        if thisImage.startswith(string):
            imageList.pop(index)
            break
    index -= 1


for string in imageList:
    svnstring = 'rm -rf '
    svnstring = svnstring + '"' + string + '"'
    print(svnstring)
    os.system(svnstring)
