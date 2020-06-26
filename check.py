import glob
import os

path1 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/annotations/'
path2 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/images/'
path3 = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/yoloFormat/'
jpgFiles = os.listdir(path2)
xmlFiles = os.listdir(path1)
print(len(jpgFiles))
count=0
for i in range(len(jpgFiles)):
    jpg = jpgFiles[i]
    xml = path1 + jpg.replace('.jpg', '.xml')
    if not os.path.exists(xml):
        os.remove(path2+jpg)
'''
count=0
for i in glob.glob(path1+'*.xml'):
    count+=1
print(count)

count=0
for i in glob.glob(path3+'*.txt'):
    count+=1
print(count)
count=0
for i in range(len(xmlFiles)):
    xml = xmlFiles[i]
    txt = path3 + xml.replace('.xml', '.txt')
    if not os.path.exists(txt):
        print(xml)
'''
