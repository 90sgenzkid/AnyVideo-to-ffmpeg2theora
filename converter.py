import os, time,subprocess
from glob import glob
# Any Video to ffmpeg2theora for Stalker Series, Making Cutscenes
# By 90sgenzkid
# 2025

theFolder = "videos" #the folder for videos
current_ext = {".avi"} #to get only .avi video to convert

#looks for the videos folder, if not, creates it
getPath = r"videos"
if not os.path.exists(getPath):
    print("Videos Folder Doesn't Exist, Creating...")
    os.makedirs(getPath)
    time.sleep(1)
    print("Stopping this program, please add .avi videos into Videos folder.")
    print("Exiting.")
    exit(0)

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
        if ext == ".avi": 
            os.remove(file_path)
            
        #Renames .ogg files to .ogm to do it easily, without user input
        subprocess.run(['MakeOGM.bat'])

print("JOB IS DONE")
