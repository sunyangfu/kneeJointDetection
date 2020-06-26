import os
import glob
import shutil
import numpy as np
from yoloFormat import yoloFormat
fJpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/F/'

mJpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/M/'

def generateTxt(path):
    folderList = os.listdir(path+'annotations/')
    
    for folder in folderList:
        if not os.path.exists(path+'txt/'+folder+'/'):
           os.makedirs(path+'txt/'+folder+'/')
           yoloFormat(path+'annotations/'+folder+'/', path+'txt/'+folder+'/')

def getPatientId(path, sex):
    idList=[]
    folderList = os.listdir(path+'images/')
    for folder in folderList:
        for jpgPath in glob.glob(path+'images/'+folder+'/*.jpg'):
            patientIdx = jpgPath.find('patientID_')
            patientId = jpgPath[patientIdx+10:patientIdx+18]
            if patientId not in idList:
                idList.append(patientId)
    print(len(idList))
    print(idList)
    np.save(sex+'IdList.npy', idList)
getPatientId(fJpgPath, 'f')
getPatientId(mJpgPath, 'm')
