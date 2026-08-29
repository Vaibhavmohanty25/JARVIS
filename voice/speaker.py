import pyttsx3

class JarvisSpeaker:
    def __init__(self):
        self.rate = 180
        self.volume = 1.0
        
    def speak(self, text):
        print(f"\nJARVIS: {text}")
        engine = pyttsx3.init()
        engine.setProperty("rate", self.rate)
        engine.setProperty("volume", self.volume)
        engine.say(text)
        engine.runAndWait()
        
        engine.stop()