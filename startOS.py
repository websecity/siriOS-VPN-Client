import platform
import os
def startup():
    startOS = platform.system()
    if startOS == "Windows":
        os.system("cls")
    elif startOS == "Linux":
        os.system("clear")
    elif startOS == "Darwin":
        os.system("clear")
    else:
        print("Zortladın")