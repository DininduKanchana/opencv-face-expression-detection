import cv2
import glob

classifier1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
classifier2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
classifier3 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
classifier4 = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] 

def detector(emotion):
    files = glob.glob("sorted_set/"+emotion+"/*")
    num = 0
    for f in files:
        gray = cv2.imread(f, 0)
     #   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face1 = classifier1.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
        face2 = classifier2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
        face3 = classifier3.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
        face4 = classifier4.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)

        if len(face1) == 1:
            face = face1
        elif len(face2) == 1:
            face = face2
        elif len(face3) == 1:
            face = face3
        elif len(face4) ==1:
            face = face4
        else:
            face = ""
            
        for (x, y, w, h) in face:
            gray = gray[y:y+h, x:x+w]
            result = cv2.resize(gray, (300, 300))
            cv2.imwrite("dataset/"+emotion+"/"+str(num)+".jpg", result)

        num = num +1

for emotion in emotions:
    detector(emotion)



