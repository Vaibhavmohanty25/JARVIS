from core.intent_classifier import IntentClassifier

from skills.web import (
    open_google,
    open_youtube,
    open_github,
    google_search,
    youtube_search
)

from skills.system import (
    open_chrome,
    open_notepad
)

from skills.utilities import (
    get_time,
    get_date
)


class AgentRouter:

    def __init__(self, brain):

        self.classifier = IntentClassifier(brain)

    def execute(self, command):

        result = self.classifier.classify(command)

        intent = result.get("intent")
        target = result.get("target", "").lower().strip()

        print(f"\nDetected Intent: {intent}")
        print(f"Detected Target: {target}")

        # -------------------------
        # OPEN WEBSITE
        # -------------------------

        if intent == "open_website":

            if "youtube" in target:
                return open_youtube()

            elif "google" in target:
                return open_google()

            elif "github" in target:
                return open_github()

            else:
                return None


        # -------------------------
        # GOOGLE SEARCH
        # -------------------------

        elif intent == "google_search":

            return google_search(target)


        # -------------------------
        # YOUTUBE SEARCH
        # -------------------------

        elif intent == "youtube_search":

            return youtube_search(target)


        # -------------------------
        # OPEN APPLICATION
        # -------------------------

        elif intent == "open_application":

            if "chrome" in target:
                return open_chrome()

            elif "notepad" in target:
                return open_notepad()

            else:
                return None


        # -------------------------
        # TIME
        # -------------------------

        elif intent == "get_time":

            return get_time()


        # -------------------------
        # DATE
        # -------------------------

        elif intent == "get_date":

            return get_date()


        # -------------------------
        # GENERAL QUESTION
        # -------------------------

        else:

            return None