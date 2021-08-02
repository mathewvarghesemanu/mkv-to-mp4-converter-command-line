##Use os.remove(item) only if you are sure that eerything else is working

''' Importing necessary header files'''
import os
from os import listdir
from os.path import isfile, join
# import send2trash                         #is not working in windows, ignore                  

video_paths=[]
video_path=""
print("After adding all the folders one by one, press y to continue for the question below.")
while 1:
    print(video_path)
    video_path=input("Enter the path : ")
    if video_path in ['y','Y']:
        break
    mypath=video_path.replace('"', "")
    video_paths.append(mypath)
# mypath=os.getcwd()

for path in video_paths:
    onlyfiles = [path+'/'+f for f in listdir(path) if isfile(join(path, f))]
   
videofiles=[]

print([item for item in onlyfiles])

for item in onlyfiles:
    if item[-4:] == ".mkv":
        videofiles.append(item)
        
print([item for item in videofiles])

for item in videofiles:
    os.system("ffmpeg -i {} -c:v libx264 -c:a aac {}".format('"'+item+'"','"'+item.replace("mkv","mp4")+'"'))       #calling ffmpeg using the os command



    # send2trash.send2trash(item)           #ignore, not working

    checkfiles=[] 
    for path in video_paths:
        checkfiles = [path+'/'+f for f in listdir(path) if isfile(join(path, f))]
    if item.replace("mkv","mp4") in checkfiles:
        os.remove(item)                     #comment out if you don't wasnt to lose files. It deletes converted files after conversion. use with caution

input("End")