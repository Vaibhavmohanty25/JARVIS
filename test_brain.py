from llm.brain import JarvisBrain


brain = JarvisBrain()

question = input("Ask JARVIS something: ")

answer = brain.ask(question)

print("\nJARVIS:")
print(answer)