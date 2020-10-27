import pyttsx3
import speech_recognition as sr
from RecordAudio import *

loopbot = 1


r = sr.Recognizer()

engine = pyttsx3.init() # object creation





print("")
print("                                         ----------------------------------------------------")
print("                                         | Welcome to Intelligence AI Version 0.01 By Ariel |")
print("                                         ----------------------------------------------------")
print("")


#Microphone Check 
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Audio Device with name \"{1}\" found for `(device_index={0})`".format(index, name))





##Rates 

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 130)     # setting up new voice rate


#Volume

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

#Voice
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

engine.say("Intelligence AI Version 0.01")
engine.say("For help say, help")
engine.runAndWait()



while loopbot == 1:
    voice_data = RecordAudio()
    respond(voice_data)

