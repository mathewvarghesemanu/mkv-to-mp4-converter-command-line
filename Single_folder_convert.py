##Use os.remove(item) only if you are sure that eerything else is working


import os
from os import listdir
from os.path import isfile, join
import send2trash

video_path=input("Enter the path : ")
mypath=video_path.replace('"', "")
# mypath=os.getcwd()

count=0
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
videofiles=[]

print([item for item in onlyfiles])

for item in onlyfiles:
    if item[-4:] == ".mkv":
        videofiles.append(mypath+"/"+item)
        
print([item for item in videofiles])

for item in videofiles:
    os.system("ffmpeg -i {} -c:v libx264 -c:a aac {}".format('"'+item+'"','"'+item.replace("mkv","mp4")+'"'))
# # print("ffmpeg -i {} -c:v libx264 -c:a aac {}".format('"'+item+'"','"'+item.replace("mkv","mp4")+'"'))
    for path in video_paths:
        checkfiles = [path+'/'+f for f in listdir(path) if isfile(join(path, f))]
    if item.replace("mkv","mp4") in checkfiles:
        os.remove(item)    
    # send2trash.send2trash(item)

