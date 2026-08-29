from voice.listener import JarvisListener
from voice.speaker import JarvisSpeaker
from core.router import route_command


def main():

    print("\n" + "=" * 45)
    print("          JARVIS INITIALIZING")
    print("=" * 45)

    # Initialize modules
    listener = JarvisListener()
    speaker = JarvisSpeaker()

    # Startup message
    speaker.speak("Jarvis is now online. What is up Vaibhav!")

    print("\nJARVIS is ready.")
    print("Try commands like:")
    print("- What time is it?")
    print("- What is today's date?")
    print("- Open Chrome")
    print("- Open Notepad")
    print("Say 'exit', 'quit', or 'stop' to close.\n")

    # Main loop
    while True:

        # Listen to the user
        command = listener.listen(duration=5)

        # If speech was detected
        if command:

            print(f"\nYou said: {command}")

            # Normalize the command
            command_lower = command.lower().strip()

            # Exit commands
            if command_lower in ["exit", "quit", "stop"]:
                speaker.speak("Goodbye! Shutting down Jarvis.")
                break

            # Send command to the router
            response = route_command(command)

            # If the router understands the command
            if response:
                speaker.speak(response)

            # If the command is unknown
            else:
                speaker.speak(
                    "I don't know how to do that yet."
                )

        # If no speech was detected
        else:
            speaker.speak(
                "I couldn't understand that. Please try again."
            )


if __name__ == "__main__":
    main()