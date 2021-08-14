import datetime
import os
import glob
from instagrapi import Client



USERNAME="jvsrvictor127"
PASSWORD="jvsr@127"

#Get the DOF(Day of Week)
#DOF=datetime.datetime.today().weekday()
DOF=3

#Test if it is post day
if(DOF==1 or DOF==3 or DOF==6):
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    if(DOF==1):
        Day="TER"
    elif(DOF==3):
        Day="QUIN"
    elif(DOF==6):
        Day="DOM"

    #First part of the Story
    fileName1="\STORIES - P1.mp4"

    media_path1 = Day + fileName1
    cl.video_upload_to_story(
        media_path1,
        "Credits @adw0rd",
    )

    #Second part of the Story
    fileName2="\STORIES - P2.mp4"

    media_path2 = Day + fileName2
    cl.video_upload_to_story(
        media_path2,
        "Credits @adw0rd",
    )

    #Delete all the content of folders
    if(DOF==6):
        files = glob.glob('TER/*')
        for f in files:
            os.remove(f)

        files = glob.glob('QUIN/*')
        for f in files:
            os.remove(f)

        files = glob.glob('DOM/*')
        for f in files:
            os.remove(f)