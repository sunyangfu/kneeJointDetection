import os
import glob
import cv2
import argparse
from xml.dom import minidom


def yoloFormat(xmlPath, yoloFormatPath):
    # get all jpg and parse xml
    for i in glob.glob(xmlPath + '*.xml'):
        print(i)
        # xmlFile = i.replace('.jpg', '.xml')
        xmlFile = i
        idx = i.rfind('/')
        txtFile = yoloFormatPath + i[idx + 1:].replace('.xml', '.txt')

        mydoc = minidom.parse(xmlFile)
        imgSize = mydoc.getElementsByTagName('size')
        width = int(imgSize[0].getElementsByTagName('width')[0].firstChild.data)
        height = int(imgSize[0].getElementsByTagName('height')[0].firstChild.data)
        classes = mydoc.getElementsByTagName('object')
        for item in classes:
            className = item.getElementsByTagName('name')[0].firstChild.data
            if className == 'kneeApView':
                className = '0'
            if className == 'tkaApView':
                className = '1'
            if className == 'kneeLatView':
                className = '2'
            if className == 'tkaLatView':
                className = '3'
            coordinates = item.getElementsByTagName('bndbox')
            for loc in coordinates:
                xmin = int(loc.getElementsByTagName('xmin')[0].firstChild.data)
                xmax = int(loc.getElementsByTagName('xmax')[0].firstChild.data)
                ymin = int(loc.getElementsByTagName('ymin')[0].firstChild.data)
                ymax = int(loc.getElementsByTagName('ymax')[0].firstChild.data)
                # x = int(round((xmax+xmin)/2,0) )
                # y = int(round((ymax+ymin)/2,0))
                x = (xmax + xmin) / 2
                y = (ymax + ymin) / 2
                format(0.1950, '.2f')
                relativeX = str(format(x / width, '0.6f'))
                relativeY = str(format(y / height, '0.6f'))
                relativeWidth = str(format((xmax - xmin) / width, '0.6f'))
                relativeHeight = str(format((ymax - ymin) / height, '0.6f'))
                print(className, relativeX, relativeY, relativeWidth, relativeHeight)
                if os.path.exists(txtFile):
                    print('exist')
                    file = open(txtFile, 'a')
                    file.write('\n')
                    file.write(' ')
                    file.write(className)
                    file.write(' ')
                    file.write(relativeX)
                    file.write(' ')
                    file.write(relativeY)
                    file.write(' ')
                    file.write(relativeWidth)
                    file.write(' ')
                    file.write(relativeHeight)
                    file.close()
                if not os.path.exists(txtFile):
                    print('not exist')
                    file = open(txtFile, 'w+')
                    file.write(className)
                    file.write(' ')
                    file.write(relativeX)
                    file.write(' ')
                    file.write(relativeY)
                    file.write(' ')
                    file.write(relativeWidth)
                    file.write(' ')
                    file.write(relativeHeight)
                    file.close()


def main():
    parser = argparse.ArgumentParser(description='yoloFormat')
    parser.add_argument('--xmlPath',
                        type=str,
                        default='/infodev1/phi-data/shi/kneeJointDetection/experimentData/OAIData/annotations/')
    parser.add_argument('--yoloFormatPath',
                        type=str,
                        default='/infodev1/phi-data/shi/kneeJointDetection/experimentData/OAIData/labels/')
    args = parser.parse_args()
    yoloFormat(args.xmlPath, args.yoloFormatPath)


if __name__ == '__main__':
    main()
