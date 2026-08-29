import json


class IntentClassifier:

    def __init__(self, brain):

        # Use the existing JARVIS brain
        self.brain = brain


    def classify(self, command):

        prompt = f"""
You are an intent classifier for a desktop AI assistant named JARVIS.

Classify the user's command into exactly ONE of these intents:

- open_website
- google_search
- youtube_search
- open_application
- get_time
- get_date
- general_question

Extract the main target or search query.

Examples:

User: "Search YouTube for Python tutorials"
Response:
{{
    "intent": "youtube_search",
    "target": "Python tutorials"
}}

User: "Find machine learning videos on YouTube"
Response:
{{
    "intent": "youtube_search",
    "target": "machine learning videos"
}}

User: "Take me to YouTube"
Response:
{{
    "intent": "open_website",
    "target": "YouTube"
}}

User: "What time is it?"
Response:
{{
    "intent": "get_time",
    "target": ""
}}

Return ONLY valid JSON.
Do not use markdown.
Do not explain your answer.

User command:
"{command}"
"""

        try:

            response = self.brain.ask(prompt)

            print("\nRaw AI classification:")
            print(response)

            # Clean possible markdown formatting
            response = response.replace(
                "```json",
                ""
            )

            response = response.replace(
                "```",
                ""
            )

            response = response.strip()

            result = json.loads(response)

            return result

        except Exception as error:

            print(
                f"\nIntent classification error: {error}"
            )

            return {
                "intent": "general_question",
                "target": command
            }