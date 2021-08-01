import os
from os import listdir
video_path=input("Enter the path : ")
mypath=video_path
# mypath=os.getcwd()

from os.path import isfile, join
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
    os.remove(item)    
    
#     count+=1
# #     os.system("..\main.py --i %s -o %s"%(item,item+"count"))
#     # os.system("python main.py -i \"Inputs/%s\" -o \"outputs\%s\" -s true"%(item,item+str(count)))
#     os.system("python main.py -i \"Inputs/%s\" -s false"%(item))
#     print("processing %s"%item)
    