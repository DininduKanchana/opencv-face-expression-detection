import cv2
import glob
import random
import numpy as np

emotions = ["anger", "happy", "surprise"]
fisher = cv2.face.createFisherFaceRecognizer()

data = {}

def makeDataSets (emotion):
    files = glob.glob("dataset/" + emotion +"/*")
    random.shuffle(files)
    trainData = files[:int(len(files)*0.9)]
    prediction = files[-int(len(files) * 0.1):]

    return trainData, prediction

def makeSets():
    trainData = []
    trainLabels = []
    predictionData = []
    predictionLables =[]

    for emotion in emotions:
        train, prediction = makeDataSets(emotion)

        for img in train :
            image = cv2.imread(img)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            trainData.append(gray)
            trainLabels.append(emotions.index(emotion))


        for img in prediction:
             image = cv2.imread(img)
             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
             predictionData.append(gray)
             predictionLables.append(emotions.index(emotion))


    return trainData, trainLabels, predictionData, predictionLables


def trainFisher():
	print("Training model...")
	trainData, trainLabels, predictionData, predictionLables = makeSets()
        fisher.train(trainData, np.asarray(trainLabels))


def start():
	trainFisher()
	print("Saving model")
	fisher.save("trained_classifier.xml")
	print("Model saved succesfully")


start()

"""
def accurancy():

    count = 0
    correctCount = 0
    incorrectCount = 

   

    for image in predictionData:
        pred, conf = fisher.predict(image)

        if pred == predictionLables[count]:
            correctCount = correctCount+1
            count = count + 1
        else:
            incorrectCount = incorrectCount + 1
            count = count + 1

    return (100*correctCount)/ (correctCount+incorrectCount)

	metascore = []
	for i in range(0,10):
    
   		correct = trainFisher()
    	print "got", correct, "percent correct!"
   		metascore.append(correct)

	print "\n\nend score:", np.mean(metascore), "percent correct!"

"""
