import os
codePath = "/Users/liuyudi/pkgame-ios_3.5_develop_feature/pkgame"
fileList = [codePath]
unCallRemoveNotifyFile = []
for file in fileList:
    files = os.listdir(file)
    for thisFile in files:
        if 'thirdparty' == thisFile:
            continue
        if thisFile.endswith('.m') or thisFile.endswith('.mm'):
            try :
                codeFile = open(file+'/'+thisFile,)
            except IOError,e:
                print('tryError')
            else:
                codeString = codeFile.read()
                if (not 'removeObserver:' in codeString and not 'REMOVE_NOTIFY' in codeString) and ('addObserver:' in codeString or 'ADD_NOTIFY' in codeString or 'ADD_NOTIFY_DefaultSelectorName' in codeString):
                    unCallRemoveNotifyFile.append(thisFile)
                codeFile.close()
        elif os.path.isdir(file+'/'+thisFile):
            fileList.append(file+'/'+thisFile)
print(unCallRemoveNotifyFile)
print(len(unCallRemoveNotifyFile))