import os
import subprocess


def open_chrome():
    chrome_paths = [ r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ]
    for path in chrome_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return "Opening google chrome"
        
    return "I could not find Google Chrome on your computer. "

def open_notepad():
    subprocess.Popen("notepad.exe")
    
    return "Opening notepad"