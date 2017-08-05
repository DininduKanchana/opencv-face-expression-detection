import cv2
import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fileName")
args = parser.parse_args()
image = args.fileName

facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def preProcess(image):
	image = cv2.imread(image)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#gray = cv2.resize(gray, (300, 300))
	cv2.imshow("image", gray)
	cv2.waitKey(0) 
	face = facecascade.detectMultiScale(gray, 1.1, 5)
	
	for (x, y, w, h) in face:
		cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2) 
	gray = gray[y:y+h, x:x+w]
	gray = cv2.resize(gray, (300, 300))
	cv2.imshow("image", gray)
	cv2.waitKey(0) 

	fisher = cv2.face.createFisherFaceRecognizer()
	fisher.load("trained_classifier.xml")

	pred, conf = fisher.predict(gray)

	return pred, conf


def output(image):

	emotions = ["anger", "happy", "surprise"]
	i, p=preProcess(image)
	emotion = emotions[i]

	img = cv2.imread(image)
	cv2.putText(img, emotion, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1,  (0,0,255),5)
	cv2.imshow("image", img)
	cv2.waitKey(0) 

	print (emotions[i])


output(image)


