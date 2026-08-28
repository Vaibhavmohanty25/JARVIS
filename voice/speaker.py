import pyttsx3

class JarvisSpeaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        
        # Speech Settings
        self.engine.setProperty("rate", 180)
        self.engine.setProperty("volume", 1.0)
        
    def speak(self, text):
        print(f"\nJARVIS: {text}")
        
        self.engine.say(text)
        self.engine.runAndWait()