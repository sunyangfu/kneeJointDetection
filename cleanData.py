import shutil
import os
import glob

path1 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/tmp/'
path2 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/images/'
path3 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/annotations/'
path4 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/images/'
path5 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/annotations/'
tmpList = os.listdir(path1)

for folder in tmpList:
    imageFolderPath = path2 + folder
    xmlFolderPath = path3 + folder
    if not os.path.exists(imageFolderPath):
        os.makedirs(imageFolderPath)
    if not os.path.exists(xmlFolderPath):
        os.makedirs(xmlFolderPath)

    for i in glob.glob(path1+folder+'/*.jpg'):
        idx = i.rfind('/')
        jpgName = i[idx+1:]
        xmlName = jpgName.replace('.jpg', '.xml')
        oldJpgPath = path4+jpgName
        oldXmlPath = path5+xmlName
        shutil.move(oldJpgPath, imageFolderPath)
        shutil.move(oldXmlPath, xmlFolderPath)

