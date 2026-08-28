from voice.listener import JarvisListener
from voice.speaker import JarvisSpeaker

def main():

    print("\n" + "=" * 45)
    print("          JARVIS INITIALIZING")
    print("=" * 45)

    # Create speech listener
    listener = JarvisListener()
    speaker = JarvisSpeaker()
    speaker.speak("Jarvis is now online. What is up Vaibhav!")
    print("\nJARVIS is ready.")
    print("Say 'exit', 'quit', or 'stop' to close.\n")

    # Main loop
    while True:

        # Listen to user
        command = listener.listen(duration=5)

        # Check if speech was detected
        if command:
            print(f"\nYou said: {command}")

            # Convert command to lowercase
            command_lower = command.lower().strip()

            # Exit commands
            if command_lower in ["exit", "quit", "stop"]:
                speaker.speak("\n Goodbye!   Shutting down JARVIS.")
                break
            else:
                speaker.speak(f"I heard you say: {command}")

        else:
            print("\nJARVIS: I couldn't understand that. Please try again.")


if __name__ == "__main__":
    main()