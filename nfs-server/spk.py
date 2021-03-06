# -*- coding: utf-8 -*-

import sys #extra
import time #extra
from time import sleep
from threading import Thread
import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS

#sys.setdefaultencoding('utf8')  #sys.setdefaultencoding('utf8')


mic_name = "USB Audio Device: - (hw:1,0)"
sample_rate = 8000
chunk_size = 2048

def writeen(writeString):
    print(writeString)

def speaken(audioString):
    tts = gTTS(text=audioString, lang='pt')
    sfile = audioString.strip("?!@#$%*()_*'+- .,")
    sfile = sfile.replace(" ", "")
    sfile = sfile.replace(",", "")
    sfile = sfile.replace("'", "")
    #os.system('omxplayer /home/pi/Music/' + sfile + '.mp3') # reproduzir som 
    os.system('mplayer /home/gchinellato/Projects/Toy-Robot/nfs-server' + sfile + '.mp3')
    
def songfile(audioString):
    tts = gTTS(text=audioString, lang='pt')
    sfile = audioString.strip("?!@#$%*()_*'+- .,")
    sfile = sfile.replace(" ", "")
    sfile = sfile.replace(",", "")
    sfile = sfile.replace("'", "")

    #if os.path.isfile("/home/pi/Music/" +  sfile + ".mp3"):
    if os.path.isfile("/home/gchinellato/Projects/Toy-Robot/nfs-server" +  sfile + ".mp3"):
        Thread(target=speaken, args=(audioString,)).start()
        time.sleep(.85)
        Thread(target=writeen, args=(audioString,)).start()
    else:
        #tts.save("/home/pi/Music/" + sfile + ".mp3")
        tts.save("/home/gchinellato/Projects/Toy-Robot/nfs-server" + sfile + ".mp3")
        Thread(target=speaken, args=(audioString,)).start()
        time.sleep(.95)
        Thread(target=writeen, args=(audioString,)).start()

def speakpt(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='pt', slow=False)
    tts.save("/home/pi/Music/audio.mp3")
    os.system("omxplayer /home/pi/Music/audio.mp3")
    #os.remove("audio.mp3") #remove temperory file

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 2, sample_rate = 48000) as source:
        #print("Say something..")
        audio = r.record(source, duration = 2)
        #audio = r.listen(source)
    data = ""
    try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='en-us') #en-us pt-BR'
        print("I understand: " + data) 
    except sr.UnknownValueError:
        print("")#("I could not understand")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data


def jarvis(data):
    ###english###
    
    if "how are you" in data:
        Thread(target=songfile, args=("I'm fine",)).start() 
 
    if "what time is it" in data:
        speaken(ctime())
 
    if "yes" in data:
        Thread(target=songfile, args=("yes",)).start()        
        time.sleep(2.0)
        #Thread(target=answer, args=("yes",)).start()
        
    if "yeah" in data:
        Thread(target=songfile, args=("yes",)).start()        
        time.sleep(2.0)
        #Thread(target=answer, args=("yes",)).start()
        
    if "no" in data:
        Thread(target=songfile, args=("no",)).start()        
        time.sleep(2.0)
        #Thread(target=answer, args=("no",)).start()       
        
    if "what is your name" in data:
        Thread(target=songfile, args=("I don't know my name",)).start()        
        time.sleep(2.3)
        #Thread(target=answer, args=("no",)).start()  
        
    if "what's your name" in data:
        Thread(target=songfile, args=("I don't know my name",)).start()        
        time.sleep(2.3)
        #Thread(target=answer, args=("no",)).start() 

    ###Portugues###
#    if "Como você esta" in data:
#        speakpt("Eu estou bem")
# 
#    if "diga sim" in data:
#        speak("yes")
#        #answer("y")
#        
#    if "diga não" in data:
#        speakpt("Não")
#        #answer("n")
#        
#    if "Qual é o seu nome" in data:
#        speakpt("Eu ainda não sei meu nome")
#        
#    if "Qual seu nome" in data:
#        speakpt("Eu ainda não sei meu nome")

#Thread(target=songfile, args=("Hi, what can I do for you?",)).start()
songfile('Eu sou o aiStaur')  
time.sleep(.5)


#while 1:
#    data = recordAudio()
#    jarvis(data)


