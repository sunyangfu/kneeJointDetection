import shutil
import glob
import os

path1 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/processedData/error/'
path2 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/new/'
path3 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/images/'
count1 = 0
count2 = 0
for i in glob.glob(path2+'*.xml'):
    idx = i.rfind('/')
    name = i[idx+1:].replace('.xml', '.jpg')
    print(name)
    xmlPath = path3 +name
    if os.path.exists(xmlPath):
        count1+=1
        shutil.move(xmlPath, path1)
    else:
        count2+=1
    #    print(xmlPath)
print(count1)
print(count2)
