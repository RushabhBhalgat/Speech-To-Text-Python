import speech_recognition as sr
import pyttsx3


#initializing the recognizer
r = sr.Recognizer()

def SpeakText(command):
    #initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop
while(1):
    try:
        #use the microphone for input
        with sr.Microphone() as source2:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2, duration=0.3)

            #listen to the input from user
            print("Listening ...")
            audio2 = r.listen(source2)

            # using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did You Say " + MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown Error occured")
    

