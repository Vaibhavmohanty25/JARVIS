from skills.utilities import get_time, get_date
from skills.system import open_chrome, open_notepad
from skills.web import (
    open_google,
    open_youtube,
    open_github,
    google_search,
    youtube_search
)


def route_command(command):

    command = command.lower().strip()

    # ----------------------------
    # WEB SEARCH COMMANDS
    # ----------------------------

    if "search youtube for" in command:

        query = command.replace(
            "search youtube for",
            ""
        ).strip()

        return youtube_search(query)


    elif "search youtube" in command:

        query = command.replace(
            "search youtube",
            ""
        ).strip()

        return youtube_search(query)


    elif "search google for" in command:

        query = command.replace(
            "search google for",
            ""
        ).strip()

        return google_search(query)


    elif "google search for" in command:

        query = command.replace(
            "google search for",
            ""
        ).strip()

        return google_search(query)


    elif command.startswith("search for"):

        query = command.replace(
            "search for",
            "",
            1
        ).strip()

        return google_search(query)


    # ----------------------------
    # OPEN WEBSITES
    # ----------------------------

    elif "open youtube" in command:
        return open_youtube()


    elif "open github" in command:
        return open_github()


    elif "open google" in command:
        return open_google()


    # ----------------------------
    # SYSTEM COMMANDS
    # ----------------------------

    elif "open chrome" in command:
        return open_chrome()


    elif "open notepad" in command:
        return open_notepad()


    # ----------------------------
    # UTILITY COMMANDS
    # ----------------------------

    elif "time" in command:
        return get_time()


    elif "date" in command or "day" in command:
        return get_date()


    # Unknown command → Gemini
    else:
        return None