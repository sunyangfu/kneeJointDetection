import os
import glob
import cv2
from xml.dom import minidom

for i in glob.glob('/infodev1/phi-data/shi/kneeJointDetection/experimentData/annotations/' + '*.xml'):
    idx = i.rfind('/')
    jpgName = i[idx + 1:].replace('.xml', '.jpg')
    jpgPath = '/infodev1/phi-data/shi/kneeJointDetection/experimentData/imagesWithBoundingBox/' + jpgName
    mydoc = minidom.parse(i)
    objects = mydoc.getElementsByTagName('object')
    for object in objects:
        label = str(object.getElementsByTagName('name')[0].firstChild.data)
        coordinates = object.getElementsByTagName('bndbox')
        if len(coordinates) > 1:
            print('jj')
        for loc in coordinates:
            xmin = int(loc.getElementsByTagName('xmin')[0].firstChild.data)
            xmax = int(loc.getElementsByTagName('xmax')[0].firstChild.data)
            ymin = int(loc.getElementsByTagName('ymin')[0].firstChild.data)
            ymax = int(loc.getElementsByTagName('ymax')[0].firstChild.data)

        if label == 'kneeApView':
            img = cv2.imread(jpgPath, cv2.IMREAD_COLOR)
            cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (0, 255, 0), 5)
            cv2.imwrite(jpgPath, img)
        if label == 'tkaApView':
            img = cv2.imread(jpgPath, cv2.IMREAD_COLOR)
            cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (0, 0, 255), 5)
            cv2.imwrite(jpgPath, img)
        if label == 'kneeLatView':
            img = cv2.imread(jpgPath, cv2.IMREAD_COLOR)
            cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (0, 255, 255), 5)
            cv2.imwrite(jpgPath, img)
        if label == 'tkaLatView':
            img = cv2.imread(jpgPath, cv2.IMREAD_COLOR)
            cv2.rectangle(img, (xmin, ymax), (xmax, ymin), (255, 0, 0), 5)
            cv2.imwrite(jpgPath, img)
