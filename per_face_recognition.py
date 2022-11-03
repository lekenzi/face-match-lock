import capture
import face_recognition
import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


known_image = face_recognition.load_image_file(resource_path("me.jpg"))
# // your main pic



def master():
    name = capture.cap()
    unknown_image = face_recognition.load_image_file(str(name)+".png")
    os.system("del "+str(name)+".png")
    if len(face_recognition.face_encodings(unknown_image)) == 0:
        return 0

    super_encodxing = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(
        [super_encodxing],
         unknown_encoding)
    return results[-1]
