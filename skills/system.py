import os
import subprocess
import webbrowser
from datetime import datetime
def open_calculator():
    try:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    except Exception as error:
        print(f"System error: {error}")
        return "Sorry, I could not open Calculator."


def open_file_explorer():
    try:
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."

    except Exception as error:
        print(f"System error: {error}")
        return "Sorry, I could not open File Explorer."


def open_notepad():
    try:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    except Exception as error:
        print(f"System error: {error}")
        return "Sorry, I could not open Notepad."


def open_chrome():
    try:
        webbrowser.open("https://www.google.com")
        return "Opening Chrome."

    except Exception as error:
        print(f"System error: {error}")
        return "Sorry, I could not open Chrome."


def open_vscode():
    try:
        subprocess.Popen("code")
        return "Opening Visual Studio Code."

    except FileNotFoundError:
        return (
            "I could not find Visual Studio Code. "
            "Make sure the code command is available in your system path."
        )

    except Exception as error:
        print(f"System error: {error}")
        return "Sorry, I could not open Visual Studio Code."


def take_screenshot():
    try:
        import os
        from datetime import datetime
        from PIL import ImageGrab

        # Save screenshots inside the project folder
        screenshots_folder = os.path.join(
            os.getcwd(),
            "screenshots"
        )

        os.makedirs(
            screenshots_folder,
            exist_ok=True
        )

        # Create a unique filename
        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        filename = os.path.join(
            screenshots_folder,
            f"screenshot_{timestamp}.png"
        )

        print("\nTaking screenshot...")

        # Capture the screen
        screenshot = ImageGrab.grab()

        # Save it
        screenshot.save(filename)

        print(f"Screenshot successfully saved to:")
        print(filename)

        return "Screenshot taken successfully."

    except Exception as error:
        print(f"\nScreenshot error: {error}")

        return (
            "Sorry, I could not take the screenshot."
        )
        
def close_application(process_name, display_name):
    """
    Close a Windows application using taskkill.
    """

    try:
        result = subprocess.run(
            [
                "taskkill",
                "/f",
                "/im",
                process_name
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return f"{display_name} closed successfully."

        return f"{display_name} is not currently running."

    except Exception as error:
        print(f"Close application error: {error}")

        return f"Sorry, I could not close {display_name}."


def close_chrome():
    return close_application(
        "chrome.exe",
        "Chrome"
    )


def close_notepad():
    return close_application(
        "notepad.exe",
        "Notepad"
    )


def close_calculator():
    return close_application(
        "CalculatorApp.exe",
        "Calculator"
    )


def close_vscode():
    return close_application(
        "Code.exe",
        "Visual Studio Code"
    )


def close_file_explorer():
    return close_application(
        "explorer.exe",
        "File Explorer"
    )