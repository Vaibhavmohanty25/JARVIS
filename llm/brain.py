import os
from dotenv import load_dotenv
from google import genai
import httpx


class JarvisBrain:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY was not found. "
                "Check your .env file."
            )

        self.client = genai.Client(
            api_key=api_key,
            http_options={
                "timeout": 60_000
            }
        )

        self.model = "gemini-3.7-flash"

        print("JARVIS cloud AI brain initialized successfully.")

    def ask(self, question):

        try:

            print("JARVIS is thinking...")

            response = self.client.interactions.create(
                model=self.model,
                input=question
            )

            answer = response.output_text

            if not answer:
                return "I could not generate a response."

            return answer.strip()

        except Exception as error:

            print("\n" + "=" * 60)
            print("GEMINI API ERROR:")
            print(f"Type: {type(error).__name__}")
            print(f"Details: {repr(error)}")
            print("=" * 60 + "\n")

            return "I'm having trouble connecting to my cloud brain right now."