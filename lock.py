import ctypes
import time
import per_face_recognition
flag = True
import ctypes

user32 = ctypes.windll.User32

print("All Models call complete")


def check():
    if True:
        time.sleep(20)
    if not per_face_recognition.master():
        if user32.GetForegroundWindow() == 329024:    
            ctypes.windll.user32.LockWorkStation()
            time.sleep(10)
            check()
        elif(user32.GetForegroundWindow() != 329024):
            time.sleep(10)
    else:
        check()


# check()


def supercall():
    time.sleep(60)
    if per_face_recognition.master():
        print(True)
        time.sleep(60)
        supercall()
    else:
        print(False)
        while True:
            ctypes.windll.user32.LockWorkStation()
            time.sleep(2)
            if user32.GetForegroundWindow() == 329024:
                print("Workstation Unlocked")
                supercall()
            elif user32.GetForegroundWindow() == 591712:
                time.sleep(2)
                print("Workstation Locked ")

supercall()