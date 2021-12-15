#pip install SpeechRecognition
#in case of error use 'pip install pyaudio' or...
#in case of error use 'pip install pipwin' then 'pipwin install pyaudio'
#if error continued you may need to use python 3.6 or lower as the latest 
#python may not support pyaudio... 
import speech_recognition as sr
import pyttsx3

#audio of system to respond
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# simple function to recognise speech from user
def takecommand():
    #it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='pt-br')
        print('User Said : ' , query)

        print("teste")
        print("teste")
        print("teste")

    except Exception as e:
        print('exception : ',e)

        speak("Sorry, I didn't hear that, Say that again Please")
        return "None"
    return query
while True:
  query = takecommand() # whatever user says will be stored in this variable
  print("The Test got in program is : "+query)