import os
import glob
import shutil

path1 = '/infodev1/phi-data/shi/kneeJointDetection/annotationData/dataBasedOnPatientID/F/'
path2 = '/infodev1/phi-data/shi/kneeJointDetection/annotationData/dataBasedOnPatientID/M/'
path3 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/annotations/'
path4 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/images/'
path5 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/'

'''
for folder in folderList:
    jpgFolderPath = path1 + folder + '/'
    xmlFolderPath = path2 + folder + '/'

    for i in glob.glob(jpgFolderPath+'*.jpg'):
        idx = i.rfind('/')
        fileName =  i[idx+1:]      
        patientIdx = fileName.find('patientID')
        sexIdx = fileName.find('sex')
        sexId = fileName[sexIdx:sexIdx+6]
        tmpName = fileName.replace(sexId, '')
        newName = sexId + tmpName
        os.rename(i, jpgFolderPath+newName)

    for i in glob.glob(xmlFolderPath+'*.xml'):
        idx = i.rfind('/')
        fileName =  i[idx+1:]      
        patientIdx = fileName.find('patientID')
        sexIdx = fileName.find('sex')
        sexId = fileName[sexIdx:sexIdx+6]
        tmpName = fileName.replace(sexId, '')
        newName = sexId + tmpName
        os.rename(i, xmlFolderPath+newName)

for i in glob.glob(path1+'*.jpg'):
    idx = i.rfind('/')
    fileName =  i[idx+1:]      
    sexIdx = fileName.find('sex')
    sexId = fileName[sexIdx:sexIdx+6]
    tmpName = fileName.replace(sexId, '')
    newName = sexId + tmpName
    print(newName)
    os.rename(i, path1+newName)

for i in glob.glob(path3+'*.xml'):
    idx = i.rfind('/')
    fileName =  i[idx+1:]      
    sexIdx = fileName.find('sex')
    sexId = fileName[sexIdx:sexIdx+6]
    tmpName = fileName.replace(sexId, '')
    newName = sexId + tmpName
    print(path3+newName)
    os.rename(i, path3+newName)
'''
