import numpy as np
import glob
import os
import shutil
import random

fIdList = np.load('./fIdList.npy').tolist()
mIdList = np.load('./mIdList.npy').tolist()

#random.shuffle(fIdList)

fJpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/F/images/'
mJpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/M/images/'
def generate5Fold(path,sex,idList):
    fmNum = len(idList)
    fmQuarterStep = int(fmNum/5)
    folderList = os.listdir(path)
    newPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/experiment/'+sex+'/'
    for i in range(1, 6):
        tmpPath = newPath+'fold'+str(i)+'/'
        if i!=5:
            start,end = (i-1)*fmQuarterStep, i*fmQuarterStep
            tmpList = idList[start:end]
        else:
            start,end = (i-1)*fmQuarterStep, fmNum
            tmpList = idList[start:end]
      
        for patientId in tmpList:
            for folder in folderList:
                for jpgPath in glob.glob(path+folder+'/'+'*.jpg'):
                    if patientId in jpgPath:
                        if os.path.exists(tmpPath+folder):
                            shutil.copy(jpgPath, tmpPath+folder)
                        else:
                            os.makedirs(tmpPath+folder)
                            shutil.copy(jpgPath, tmpPath+folder)  
                          
generate5Fold(fJpgPath,'F',fIdList)                            
generate5Fold(mJpgPath,'M',mIdList)        




