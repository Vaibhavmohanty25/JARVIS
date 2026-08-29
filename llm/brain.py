import os
from dotenv import load_dotenv
from google import genai


class JarvisBrain:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY was not found."
            )

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-3.5-flash"

        print("JARVIS cloud AI brain initialized successfully.")

    def ask(self, question, memory=None):

        try:

            print("JARVIS is thinking...")

            conversation = ""

            # Add previous conversation
            if memory:
                for message in memory.get_messages():

                    role = message["role"]
                    content = message["content"]

                    conversation += (
                        f"{role.upper()}: {content}\n"
                    )

            # Add the new question
            conversation += f"USER: {question}\nASSISTANT:"

            response = self.client.interactions.create(
                model=self.model,
                input=conversation
            )

            answer = response.output_text

            if not answer:
                return "I could not generate a response."

            return answer.strip()

        except Exception as error:

            print(
                f"LLM Error: {type(error).__name__}: {error}"
            )

            return (
                "I'm having trouble accessing my cloud brain."
            )