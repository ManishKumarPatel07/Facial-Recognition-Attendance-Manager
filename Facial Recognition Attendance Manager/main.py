

import cv2
import numpy as np
import face_recognitions

imgManish = face_recognition.load_image_file('MANISH KUMAR PATEL.jpg')
imgManish = cv2.cvtColor(imgManish, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('MANISH.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgManish)[0]
encodeManish = face_recognition.face_encodings(imgManish)[0]
cv2.rectangle(imgManish, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

facelocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[1]
cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

results = face_recognition.compare_faces([encodeManish], encodeTest)
faceDis = face_recognition.face_distance([encodeManish], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('modi', imgManish)
cv2.imshow('MANISH', imgTest)
cv2.waitKeys(0)
