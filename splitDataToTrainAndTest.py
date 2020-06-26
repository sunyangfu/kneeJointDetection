import os
import shutil
import glob
import numpy as np
import random


def getId(path):
    idList = []
    count = 0
    for i in glob.glob(path + '*/*.jpg'):
        # idx = i.find('_manu_')
        # end = i.find('_size_')
        # manu = i[idx + 6:end]
        # nameidx = i.rfind('/')
        # name = i[nameidx + 1:]
        pIdx = i.find('_patientID_')
        patientId = i[pIdx + 11: pIdx + 19]
        if patientId not in idList:
            count += 1
            idList.append(patientId)
        '''
        if i.find('sex_M') != -1:
            mCount += 1
            if patientId not in mIdList:
                mIdList.append(patientId)
        if i.find('sex_F') != -1:
            fCount += 1
            if patientId not in fIdList:
                fIdList.append(patientId)
        '''
    return idList, count


def shuffleId(idList, inputDataPath):
    random.shuffle(idList)
    quarterStep = int(len(idList) / 5)
    foldId = []
    # save the number of different manufacturer of each fold. manu = [[1,2,3], [2,3,1],..., [5,4,6]]
    # depuy, howmedica, zimmer
    manuNumList = []
    for i in range(1, 6, 1):
        depuy = 0
        howmedica = 0
        zimmer = 0
        tmpList = idList[(i - 1) * quarterStep: i * quarterStep]
        for id in tmpList:
            for jpgPath in glob.glob(inputDataPath + '*/*.jpg'):
                idx = jpgPath.find('_manu_')
                end = jpgPath.find('_size_')
                manu = jpgPath[idx + 6:end]
                nameidx = jpgPath.rfind('/')
                name = jpgPath[nameidx + 1:]
                pIdx = jpgPath.find('_patientID_')
                patientId = jpgPath[pIdx + 11: pIdx + 19]
                if patientId == id and manu == 'DEPUY':
                    depuy += 1
                if patientId == id and manu == 'HOWMEDICA':
                    howmedica += 1
                if patientId == id and manu == 'ZIMMER':
                    zimmer += 1
        manuNumList.append([depuy, howmedica, zimmer])
    # idList store the patient id which was randomly shuffuled
    return manuNumList, idList


def findGoodFold(idList, lowerList, higherList, inputDataPath):
    flag = True
    manuNumList, idList = shuffleId(idList, inputDataPath)
    while flag:
        # check the number of each manufacturer, to see whether it's in a valid range, if not, reshuffle the idlist
        # unitl finds the good combination.
        for fold in manuNumList:
            depuy, howmedica, zimmer = fold[0], fold[1], fold[2]
            if (lowerList[0] < depuy < higherList[0]) and (lowerList[1] < howmedica < higherList[1]) and (
                    lowerList[2] < zimmer < higherList[2]):
                flag = False
            else:
                manuNumList, idList = shuffleId(idList, inputDataPath)
                flag = True
                break
        continue
    print(manuNumList)
    return idList


def generateFold(idList, inputDataPath, outputDataPath):
    quarterStep = int(len(idList) / 5)
    for i in range(1, 6, 1):
        tmpList = idList[(i - 1) * quarterStep: i * quarterStep]
        if not os.path.exists(outputDataPath + 'fold' + str(i) + '/'):
            os.makedirs(outputDataPath + 'fold' + str(i) + '/' + 'DEPUY' + '/')
            os.makedirs(outputDataPath + 'fold' + str(i) + '/' + 'HOWMEDICA' + '/')
            os.makedirs(outputDataPath + 'fold' + str(i) + '/' + 'ZIMMER' + '/')
        for id in tmpList:
            for jpgPath in glob.glob(inputDataPath + '*/*.jpg'):
                idx = jpgPath.find('_manu_')
                end = jpgPath.find('_size_')
                manu = jpgPath[idx + 6:end]
                nameidx = jpgPath.rfind('/')
                name = jpgPath[nameidx + 1:]
                pIdx = jpgPath.find('_patientID_')
                patientId = jpgPath[pIdx + 11: pIdx + 19]
                if patientId == id:
                    if manu == 'DEPUY':
                        shutil.copy(jpgPath, outputDataPath + 'fold' + str(i) + '/' + 'DEPUY' + '/')
                    if manu == 'HOWMEDICA':
                        shutil.copy(jpgPath, outputDataPath + 'fold' + str(i) + '/' + 'HOWMEDICA' + '/')
                    if manu == 'ZIMMER':
                        shutil.copy(jpgPath, outputDataPath + 'fold' + str(i) + '/' + 'ZIMMER' + '/')
                else:
                    continue


def exec(inputDataPath, outputDataPath, lowerList, higherList):
    tmpIdList, count = getId(inputDataPath)
    print('ID extracted')
    manuNumList, idList = shuffleId(tmpIdList, inputDataPath)
    print('First shuffle finished')
    idList = findGoodFold(idList, lowerList, higherList, inputDataPath)
    print('Found good fold')
    generateFold(idList, inputDataPath, outputDataPath)
    print('Generate good fold')
    np.save(outputDataPath + 'idList.npy', idList)


# ap3:  1904, 1295, 1180, lower: 280, 190, 170  higher: 480, 330, 300
# lat3: 1913, 1301, 1186, lower:
# mix3: 3817, 2597, 2366, lower: 560, 380, 340  higher: 960, 660, 60

# ap = '/infodev1/phi-data/shi/tkaTypeDetection/3Manu/ap3/'
# lat = '/infodev1/phi-data/shi/tkaTypeDetection/3Manu/lat3/'
# mix = '/infodev1/phi-data/shi/tkaTypeDetection/3Manu/mix3/'
# apPath = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/ap3/'
# latPath = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/lat3/'
# mixPath = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/mix3/'

# lowerList = [340, 230, 210]
# higherList = [440, 300, 270]
# exec(inputDataPath=ap, outputDataPath=apPath, lowerList=lowerList, higherList=higherList)
# exec(inputDataPath=lat, outputDataPath=latPath, lowerList=lowerList, higherList=higherList)
#
# lowerList = [680, 460, 420]
# higherList = [880, 600, 540]
# exec(inputDataPath=mix, outputDataPath=mixPath, lowerList=lowerList, higherList=higherList)


def final(ori, dst):
    for i in range(1, 6, 1):
        foldList = [1, 2, 3, 4, 5]
        foldList.remove(i)
        # create folder to save data
        trainImgPath = dst + str(i) + '/train/'
        valImgPath = dst + str(i) + '/val/'
        if not os.path.exists(trainImgPath):
            os.makedirs(trainImgPath + 'DEPUY/')
            os.makedirs(trainImgPath + 'HOWMEDICA/')
            os.makedirs(trainImgPath + 'ZIMMER/')
        if not os.path.exists(valImgPath):
            os.makedirs(valImgPath + 'DEPUY/')
            os.makedirs(valImgPath + 'HOWMEDICA/')
            os.makedirs(valImgPath + 'ZIMMER/')

        # copy data to train folder
        for foldId in foldList:
            for jpgs in glob.glob(ori + 'fold' + str(foldId) + '/DEPUY/*.jpg'):
                shutil.copy(jpgs, trainImgPath + 'DEPUY/')
            for jpgs in glob.glob(ori + 'fold' + str(foldId) + '/HOWMEDICA/*.jpg'):
                shutil.copy(jpgs, trainImgPath + 'HOWMEDICA/')
            for jpgs in glob.glob(ori + 'fold' + str(foldId) + '/ZIMMER/*.jpg'):
                shutil.copy(jpgs, trainImgPath + 'ZIMMER/')
        # copy data to val folder
        for jpgs in glob.glob(ori + 'fold' + str(i) + '/DEPUY/*.jpg'):
            shutil.copy(jpgs, valImgPath + 'DEPUY/')
        for jpgs in glob.glob(ori + 'fold' + str(i) + '/HOWMEDICA/*.jpg'):
            shutil.copy(jpgs, valImgPath + 'HOWMEDICA/')
        for jpgs in glob.glob(ori + 'fold' + str(i) + '/ZIMMER/*.jpg'):
            shutil.copy(jpgs, valImgPath + 'ZIMMER/')


apOri = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/5fold/ap3/'
latOri = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/5fold/lat3/'
mixOri = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/5fold/mix3/'

apDst = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/ap3/'
latDst = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/lat3/'
mixDst = '/infodev1/phi-data/shi/tkaTypeDetection/experiment/data/mix3/'

final(apOri, apDst)
final(latOri, latDst)
final(mixOri, mixDst)
