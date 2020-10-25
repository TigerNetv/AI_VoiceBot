import speech_recognition as sr
import webbrowser
import pyttsx3
import time



t = time.localtime()
engine = pyttsx3.init() # object creation


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



r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:

def RecordAudio(ask=False):
    with sr.Microphone() as source: # microphone as source
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            engine.runAndWait()
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine.say('I did not get that, try again')
            engine.runAndWait()
        except sr.RequestError:
            engine.say('Sorry, the service is down') # error: recognizer is not connected
            engine.runAndWait()
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()



def respond(voice_data):
    if 'what is your name' in voice_data or 'name' in voice_data:
        engine.say('Intelligence AI Version 0.1 made by Ariel')
        engine.runAndWait()
    if 'commands' in voice_data or 'help' in voice_data or 'hope' in voice_data:
        engine.say('For Check my name say, Name')
        engine.say('For Search say, Search')
        engine.say('For Music say, Music')
        engine.say('For Time say, Time')
        engine.say('For Search location say, location')
        engine.say('For Youtube say, Youtube')
        engine.runAndWait()
    if 'search' in voice_data or 'google' in voice_data:
        engine.say('What do you want to search for?')
        engine.runAndWait()        
        search = RecordAudio()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        engine.say('Here is what i found for ' + search)
        engine.runAndWait()
    if 'location' in voice_data:
        engine.say('What location you want to search?')
        engine.runAndWait()
        location = RecordAudio()
        url ='https://google.com/maps/place/' + location
        webbrowser.get().open(url)
        engine.say('Here is the location of ' + location)
    if 'youtube' in voice_data or 'music' in voice_data or 'YouTube' in voice_data:
        engine.say('what do you want to search for?')
        engine.runAndWait()
        youtube = RecordAudio()
        url = 'https://www.youtube.com/results?search_query=' + youtube
        webbrowser.get().open(url)
    if 'time' in voice_data:
        engine.say(time.asctime(t))
        engine.runAndWait()
    if 'exit' in voice_data:
        exit()
