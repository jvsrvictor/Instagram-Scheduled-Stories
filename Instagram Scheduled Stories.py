import datetime
import os
import glob
from instagrapi import Client

USERNAME="username"
PASSWORD="password"

#Get the DOF(Day of Week)
DOF=datetime.datetime.today().weekday()

#Test if it is post day
if(DOF==1 or DOF==3 or DOF==6):
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    if(DOF==1):
        Day="Tuesday"
    elif(DOF==3):
        Day="Thursday"
    elif(DOF==6):
        Day="Sunday"

    #First part of the Story
    fileName1="\File 1.mp4"

    media_path1 = Day + fileName1
    cl.video_upload_to_story(
        media_path1
    )

    #Second part of the Story
    fileName2="\File 2.mp4"

    media_path2 = Day + fileName2
    cl.video_upload_to_story(
        media_path2
    )

    #Delete all the content of folders
    if(DOF==6):
        files = glob.glob('Tuesday/*')
        for f in files:
            os.remove(f)

        files = glob.glob('Thursday/*')
        for f in files:
            os.remove(f)

        files = glob.glob('Sunday/*')
        for f in files:
            os.remove(f)
