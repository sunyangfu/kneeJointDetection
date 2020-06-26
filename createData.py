import os
import shutil
import glob

fJpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/5fold/F/'
mJpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/5fold/M/'
ftxtPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/F/txt/'
mtxtPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/M/txt/'


def generateData(path, txtPath, sex):
    folderList = os.listdir('/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/F/txt/')
    print(folderList)
    for i in range(1, 6, 1):
        foldList = [1, 2, 3, 4, 5]
        foldList.remove(i)
        # create folder to save data
        dataPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/data/'
        trainImgPath = dataPath + str(i) + '/images/train/'
        valImgPath = dataPath + str(i) + '/images/val/'
        if not os.path.exists(trainImgPath):
            os.makedirs(trainImgPath)
        if not os.path.exists(valImgPath):
            os.makedirs(valImgPath)
        trainLabelPath = dataPath + str(i) + '/labels/train/'
        valLabelPath = dataPath + str(i) + '/labels/val/'
        if not os.path.exists(trainLabelPath):
            os.makedirs(trainLabelPath)
        if not os.path.exists(valLabelPath):
            os.makedirs(valLabelPath)

        # create train
        kneeLat, tkaLat, mixedAp, doubleKneeAp, doubleTkaAp, singleKneeAp, singleTkaAp = 0, 0, 0, 0, 0, 0, 0
        for foldId in foldList:
            for folder in folderList:
                tmpPath = path + 'fold' + str(foldId) + '/' + folder + '/'
                for jpgPath in glob.glob(tmpPath + '*.jpg'):
                    if folder == 'kneeLatView':
                        kneeLat += 1
                    if folder == 'tkaLatView':
                        tkaLat += 1
                    if folder == 'mixedApView':
                        mixedAp += 1
                    if folder == 'doubleKneeApView':
                        doubleKneeAp += 1
                    if folder == 'doubleTkaApView':
                        doubleTkaAp += 1
                    if folder == 'singleKneeApView':
                        singleKneeAp += 1
                    if folder == 'singleTkaApView':
                        singleTkaAp += 1
                    idx = jpgPath.rfind('/')
                    txtName = jpgPath[idx + 1:].replace('.jpg', '.txt')
                    shutil.copy(jpgPath, trainImgPath)
                    shutil.copy(txtPath + folder + '/' + txtName, trainLabelPath)

        file = open(dataPath + str(i) + '/trainStats'+sex+'.txt', 'w')
        file.write('sex ')
        file.write(sex)
        file.write('\n')
        file.write('kneeLat ')
        file.write(str(kneeLat))
        file.write('\n')
        file.write('tkaLat ')
        file.write(str(tkaLat))
        file.write('\n')
        file.write('mixedAp ')
        file.write(str(mixedAp))
        file.write('\n')
        file.write('doubleKneeAp ')
        file.write(str(doubleKneeAp))
        file.write('\n')
        file.write('doubleTkaAp ')
        file.write(str(doubleTkaAp))
        file.write('\n')
        file.write('singleKneeAp ')
        file.write(str(singleKneeAp))
        file.write('\n')
        file.write('singleTkaAp ')
        file.write(str(singleTkaAp))

        file.close()
        # print(kneeLat,tkaLat,mixedAp,doubleKneeAp,doubleTkaAp,singleKneeAp, singleTkaAp)

        # create val
        kneeLat, tkaLat, mixedAp, doubleKneeAp, doubleTkaAp, singleKneeAp, singleTkaAp = 0, 0, 0, 0, 0, 0, 0
        for folder in folderList:
            tmpPath = path + 'fold' + str(i) + '/' + folder + '/'
            for jpgPath in glob.glob(tmpPath + '*.jpg'):
                if folder == 'kneeLatView':
                    kneeLat += 1
                if folder == 'tkaLatView':
                    tkaLat += 1
                if folder == 'mixedApView':
                    mixedAp += 1
                if folder == 'doubleKneeApView':
                    doubleKneeAp += 1
                if folder == 'doubleTkaApView':
                    doubleTkaAp += 1
                if folder == 'singleKneeApView':
                    singleKneeAp += 1
                if folder == 'singleTkaApView':
                    singleTkaAp += 1
                    idx = jpgPath.rfind('/')
                    jpgName = jpgPath[idx + 1:]
                idx = jpgPath.rfind('/')
                txtName = jpgPath[idx + 1:].replace('.jpg', '.txt')
                shutil.copy(jpgPath, valImgPath)
                shutil.copy(txtPath + folder + '/' + txtName, valLabelPath)

        file = open(dataPath + str(i) + '/valStats'+sex+'.txt', 'w')
        file.write('sex ')
        file.write(sex)
        file.write('\n')
        file.write('kneeLat ')
        file.write(str(kneeLat))
        file.write('\n')
        file.write('tkaLat ')
        file.write(str(tkaLat))
        file.write('\n')
        file.write('mixedAp ')
        file.write(str(mixedAp))
        file.write('\n')
        file.write('doubleKneeAp ')
        file.write(str(doubleKneeAp))
        file.write('\n')
        file.write('doubleTkaAp ')
        file.write(str(doubleTkaAp))
        file.write('\n')
        file.write('singleKneeAp ')
        file.write(str(singleKneeAp))
        file.write('\n')
        file.write('singleTkaAp ')
        file.write(str(singleTkaAp))
        file.close()
        # print(kneeLat,tkaLat,mixedAp,doubleKneeAp,doubleTkaAp,singleKneeAp, singleTkaAp)


generateData(fJpgPath, ftxtPath, 'Female')
generateData(mJpgPath, mtxtPath, 'Male')
