import ctypes
import time
import per_face_recognition
flag = True
import psutil

user32 = ctypes.windll.User32

print("All Models call complete")

# def check():
#     if True:
#         time.sleep(20)
#     if not per_face_recognition.master():
#         if user32.GetForegroundWindow() == unlock:    
#             ctypes.windll.user32.LockWorkStation()
#             time.sleep(10)
#             check()
#         elif(user32.GetForegroundWindow() != lock):
#             time.sleep(10)
#     else:
#         check()


# check()

unlock = user32.GetForegroundWindow()


def supercall():
    time.sleep(10)
    if per_face_recognition.master():
        print(True)
        time.sleep(10)
        supercall()
    else:
        print(False)
        ctypes.windll.user32.LockWorkStation()
        while True:
            for proc in psutil.process_iter():
                if(proc.name() == "LogonUI.exe"):
                    print("Workstation Locked")
                    time.sleep(3)
                elif(user32.GetForegroundWindow() == unlock):
                    print("Workstation Unlocked")
                    supercall()

supercall()
