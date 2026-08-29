class WakeWordDetector:

    def __init__(self, wake_words=None):

        if wake_words is None:
            wake_words = ["jarvis"]

        self.wake_words = wake_words


    def detect(self, text):

        if not text:
            return False

        text = text.lower().strip()

        return any(word in text for word in self.wake_words)


    def extract_command(self, text):

        if not text:
            return ""

        text = text.lower().strip()

        for word in self.wake_words:

            if word in text:

                # Get everything after the wake word
                command = text.split(word, 1)[1].strip()

                # Remove common punctuation
                command = command.lstrip(" ,.!?:;")

                return command

        return ""