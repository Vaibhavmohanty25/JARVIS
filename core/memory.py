class ConversationMemory:

    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.messages = []

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

        self._trim_memory()

    def add_jarvis_message(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })

        self._trim_memory()

    def get_messages(self):
        return self.messages

    def _trim_memory(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def clear(self):
        self.messages = []