# import time as t
# import os

# def start(): 
#     t.sleep(10)     
#     return os.system(".\power.ps1")

# print(start())

import ctypes
import time
user32 = ctypes.windll.User32
time.sleep(10)

print(user32.GetForegroundWindow())




# import psutil
# import time as t
# while True:
#     for proc in psutil.process_iter():
#         if(proc.name() == "LogonUI.exe"):
#             print ("Locked")