from skills.utilities import get_time, get_date
from skills.system import open_chrome, open_notepad
def route_command(command):
    command_lower = command.lower().strip()

    if "time" in command_lower:
        return get_time()
    elif "date" in command_lower or "day" in command_lower:
        return get_date()
    elif "open chrome" in command_lower:
        return open_chrome()
    elif "open notepad" in command_lower:
        return open_notepad()
    elif any(word in command for word in ["exit", "quit", "stop"]):
        return "Gooodbye, shutting down JARVIS."
    else:
        return "I'm sorry, I don't recognize that command."