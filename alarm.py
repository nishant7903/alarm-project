import time

import subprocess


def set(atime, path):
    print(f"Alarm is set for {atime}")


    while True:     #for check the time

        crttime = time.strftime("%H:%M")   # for check current system time


        if crttime == atime: # for check current time match or not
            print("Time to Wake Up!")

            subprocess.Popen(["start", "/min", "wmplayer", path], shell=True) #run the ringtone in the backgroung
            break


        time.sleep(10)       # Sleep for 10 seconds before checking the time again



atime = input("Enter the alarm time (HH:MM): ") # input time


path = "D:\\music\\nokia.mp3"  # ringtone path


set(atime, path)
