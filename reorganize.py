import os
import glob
import shutil


path1 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/F/images/'
path2 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/F/annotations/'
path3 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/M/images/'
path4 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/cleanedData/M/annotations/'

def move(path1, path2, ends):
    tmp = os.listdir(path1)
    for folder in tmp:
        for i in glob.glob(path1+folder+'/'+ends):
            idx = i.rfind('/')
            fileName = i[idx+1:]
            
            if fileName.startswith('sex_M'):
                print(fileName)
                new = path2+folder+'/'
                if not os.path.exists(new):
                    os.makedirs(new)
                    shutil.move(i,new)
                else:
                    shutil.move(i,new)
            else:
                continue

move(path1, path3,'*.jpg')
move(path2, path4,'*.xml')
