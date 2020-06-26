import glob
import shutil

path1 = '/infodev1/phi-data/shi/kneeJointDetection/annotationData/dataBasedOnPatientID/1/'
path2 = '/infodev1/phi-data/shi/kneeJointDetection/annotationData/dataBasedOnPatientID/tmp/'

for i in glob.glob(path1+'*/*.jpg'):
    shutil.move(i, path2)
