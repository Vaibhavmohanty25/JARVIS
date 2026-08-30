from skills.utilities import get_time, get_date
from vision.vision_engine import VisionEngine
from skills.system import (
    open_chrome,
    open_notepad,
    open_calculator,
    open_file_explorer,
    open_vscode,
    take_screenshot,
    close_chrome,
    close_notepad,
    close_calculator,
    close_vscode,
    close_file_explorer
)

from skills.web import (
    open_google,
    open_youtube,
    open_github,
    google_search,
    youtube_search
)


def route_command(command, vision=None):

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

    elif (
        "open calculator" in command
        or "launch calculator" in command
    ):
        return open_calculator()

    elif (
        "open file explorer" in command
        or "open explorer" in command
        or "open files" in command
    ):
        return open_file_explorer()

    elif (
        "open visual studio code" in command
        or "open vscode" in command
        or "open vs code" in command
    ):
        return open_vscode()

    elif (
        "take a screenshot" in command
        or "take screenshot" in command
        or "capture my screen" in command
    ):
        return take_screenshot()
    
        # ----------------------------
    # CLOSE APPLICATIONS
    # ----------------------------

    elif "close chrome" in command:
        return close_chrome()

    elif "close notepad" in command:
        return close_notepad()

    elif (
        "close calculator" in command
        or "close calc" in command
    ):
        return close_calculator()

    elif (
        "close vscode" in command
        or "close vs code" in command
        or "close visual studio code" in command
    ):
        return close_vscode()

    elif (
        "close file explorer" in command
        or "close explorer" in command
    ):
        return close_file_explorer()
        # ----------------------------
    # VISION COMMANDS
    # ----------------------------

    elif (
        "activate vision mode" in command
        or "start vision mode" in command
        or "turn on vision" in command
    ):

        if vision is None:
            return "Vision system is not available."

        return vision.start_vision_mode()


    elif (
        "stop vision mode" in command
        or "deactivate vision mode" in command
        or "turn off vision" in command
    ):

        if vision is None:
            return "Vision system is not available."

        return vision.stop_vision_mode()


    elif (
        "what do you see" in command
        or "what can you see" in command
        or "what are you seeing" in command
    ):

        if vision is None:
            return "Vision system is not available."

        return vision.get_last_detected_objects()

    # ----------------------------
    # UTILITY COMMANDS
    # ----------------------------

    elif "time" in command:
        return get_time()

    elif "date" in command or "day" in command:
        return get_date()

    # ----------------------------
    # UNKNOWN COMMAND -> GEMINI
    # ----------------------------

    else:
        return None