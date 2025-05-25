import os
from glob import glob
# Any Video to ffmpeg2theora for Stalker Series, Making Cutscenes
# By TheSparrowhawk
# 2025

theFolder = "videos" #the folder for videos
current_ext = {".avi"} #to get only .avi video to convert

#looks for the videos folder, if not, creates it
getPath = r"videos"
if not os.path.exists(getPath):
    os.makedirs(getPath)

#The folder where you put videos on
getFiles = [os.path.abspath(f) for f in glob(os.path.join(theFolder, "*"))]

for file_path in getFiles:
        
        filename = os.path.splitext(file_path)[0] #Gets Name
        ext = os.path.splitext(file_path)[1].lower() #Gets File Extension
    
        #Makes converted file new name
        output_path = os.path.join(theFolder, filename)
        print(f"Converting the file from {file_path} to {output_path}")

        #Start converting
        os.system(f"ffmpeg2theora-0.16.exe {os.path.abspath(file_path)}")

#Removes .avi files after converting them to .ogg            
if glob("*.avi"): 
    os.remove(file_path)

print("JOB IS DONE")