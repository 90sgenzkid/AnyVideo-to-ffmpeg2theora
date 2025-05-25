import os, shutil
from glob import glob
# Any Video to ffmpeg2theora for Stalker Series, Making Cutscenes
# By TheSparrowhawk
# 2025

theFolder = "videos"
current_ext = {".avi"}

getFiles = [os.path.abspath(f) for f in glob(os.path.join(theFolder, "*"))]

for file_path in getFiles:
        
        filename = os.path.splitext(file_path)[0]
        
        ext = os.path.splitext(file_path)[1].lower()
        
        print(filename)
        print(ext)
    
        output_path = os.path.join(theFolder, filename)
        print(f"Converting the file from {file_path} to {output_path}")

        os.system(f"ffmpeg2theora-0.16.exe {os.path.abspath(file_path)}")
            
if ext.endswith(".avi"): 
    os.remove(file_path)
print("JOB IS DONE")