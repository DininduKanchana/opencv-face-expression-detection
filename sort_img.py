import glob
from shutil import copyfile

def getImages():
	emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
	participants = glob.glob("source_emotion/*") 
        for participant in participants:
            part = participant[-4:] 
            for f in glob.glob(participant + "/*"):
                for files in glob.glob(f + "/*"):
                    read_file = open(files, 'r')
                    current_folder = files[20:-30]
                    emotion = int(float(read_file.readline()))
                    
                    source_emotion_file = glob.glob("source_images/"+ part + "/" + current_folder + "/*" )[-1]

                    source_neutral_file = glob.glob("source_images/"+ part + "/" + current_folder + "/*" )[0]

                    dest_neut = "sorted_set/neutral/%s" %source_neutral_file[25:] 
                    dest_emot = "sorted_set/%s/%s" %(emotions[emotion], source_emotion_file[25:]) #Do same for emotion containing image
            
                    copyfile(source_neutral_file, dest_neut) 
                    copyfile(source_emotion_file, dest_emot) 








getImages()
