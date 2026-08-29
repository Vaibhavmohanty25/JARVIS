from voice.listener import JarvisListener
from voice.speaker import JarvisSpeaker

from core.memory import ConversationMemory
from core.wake_word_engine import WakeWordEngine
from core.agent_router import AgentRouter
from core.router import route_command
from llm.brain import JarvisBrain


def process_command(
    command,
    speaker,
    brain,
    memory,
    agent_router
):

    # Normalize the command
    command_lower = command.lower().strip()

    # ------------------------------------------
    # EXIT COMMANDS
    # ------------------------------------------

    if any(
        word in command_lower
        for word in ["exit", "quit", "stop", "shutdown"]
    ):
        speaker.speak("Goodbye. Shutting down Jarvis.")
        return False

    # ------------------------------------------
    # CLEAR MEMORY COMMAND
    # ------------------------------------------

    if "clear memory" in command_lower:

        memory.clear()

        speaker.speak(
            "Conversation memory cleared."
        )

        return True

     # ==========================================
    # STEP 1: FAST LOCAL ROUTER
    # No Gemini API call
    # ==========================================

    response = route_command(command)

    if response:

        print(
            "\nLocal skill detected. "
            "Executing without cloud AI..."
        )

        speaker.speak(response)

        return True
    # ==========================================
    # STEP 2: AI AGENT ROUTER
    # Only used for more flexible commands
    # ==========================================

    print(
        "\nNo exact local skill found."
    )

    print(
        "JARVIS is analyzing your request..."
    )

    response = agent_router.execute(command)

    if response:

        speaker.speak(response)

        return True
    # ==========================================
    # STEP 3: GEMINI CONVERSATION
    # ==========================================

    print(
        "\nNo skill found."
    )

    print(
        "Sending request to JARVIS AI brain..."
    )

    # Save user message
    memory.add_user_message(command)

    # Ask Gemini
    response = brain.ask(
        command,
        memory
    )

    # Save response
    memory.add_jarvis_message(response)

    # Speak response
    speaker.speak(response)

    return True


def main():

    print("\n" + "=" * 55)
    print("            JARVIS INITIALIZING")
    print("=" * 55)

    # ------------------------------------------
    # INITIALIZE CORE MODULES
    # ------------------------------------------

    listener = JarvisListener()

    speaker = JarvisSpeaker()

    brain = JarvisBrain()

    memory = ConversationMemory(
        max_messages=10
    )

    agent_router = AgentRouter(brain)

    # ------------------------------------------
    # INITIALIZE WAKE WORD ENGINE
    # ------------------------------------------

    wake_engine = WakeWordEngine(
        model_name="hey_jarvis",
        threshold=0.5,

        # Change this if you used a specific
        # microphone device ID during testing
        device_id=None
    )

    # ------------------------------------------
    # STARTUP MESSAGE
    # ------------------------------------------

    speaker.speak(
        "Jarvis is online. "
        "Say Hey Jarvis to wake me up."
    )

    print("\nJARVIS is ready.")
    print("Waiting for wake word...")

    running = True

    # ==========================================
    # MAIN JARVIS LOOP
    # ==========================================

    while running:

        # --------------------------------------
        # SLEEP MODE
        # --------------------------------------

        wake_engine.wait_for_wake_word()

        print("\nJARVIS ACTIVATED!")

        # --------------------------------------
        # ACTIVE MODE
        # --------------------------------------

        speaker.speak(
            "Yes, how can I help?"
        )

        # Listen for user command
        command = listener.listen(
            duration=6
        )

        # --------------------------------------
        # NO COMMAND HEARD
        # --------------------------------------

        if not command:

            speaker.speak(
                "I didn't hear anything. "
                "Going back to sleep."
            )

            continue

        print(f"\nYou said: {command}")

        # --------------------------------------
        # PROCESS COMMAND
        # --------------------------------------

        running = process_command(
            command=command,
            speaker=speaker,
            brain=brain,
            memory=memory,
            agent_router=agent_router
        )

        # --------------------------------------
        # RETURN TO SLEEP MODE
        # --------------------------------------

        if running:

            print(
                "\nTask completed. "
                "Returning to sleep mode..."
            )

    # ==========================================
    # SHUTDOWN
    # ==========================================

    print("\nJARVIS has shut down.")


if __name__ == "__main__":
    main()