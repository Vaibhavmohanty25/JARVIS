# JARVIS — Building My Own Iron Man-Inspired AI Assistant

> *"Sometimes, building your dream project starts with a simple question: what if I tried to build my own JARVIS?"*

This project is my attempt to build a real-world AI assistant inspired by JARVIS from Iron Man.

Obviously, I'm not building a fully autonomous holographic assistant in a basement workshop. Not yet, anyway.

The idea behind this project is to gradually build an assistant that can listen, speak, think, see, remember information, search the web, control parts of a computer, and eventually become more autonomous over time.

Rather than treating JARVIS as a single AI model, I am building it as a collection of different AI systems and tools working together.

> **Tony Stark had JARVIS. I'm building mine.**

---

## What JARVIS Can Do

At its current stage, JARVIS can:

* Listen to voice commands
* Respond using text-to-speech
* Wake up when it hears "Hey Jarvis"
* Answer general questions using an LLM
* Maintain short-term conversation context
* Search Google and YouTube
* Open websites
* Open and close desktop applications
* Take screenshots
* Detect objects through a webcam
* Run computer vision in the background while the assistant continues operating
* Route simple commands locally without unnecessarily calling the LLM

The project is still under active development, and the idea is to continuously add new capabilities.

---

## How It Works

The basic interaction flow looks like this:

```text
User
  |
  v
Wake Word Detection
  |
  v
Speech Recognition
  |
  v
Command Router
  |
  +-----------------------------+
  |                             |
  v                             v
Local Skills                AI Agent / LLM
  |                             |
  +-------------+---------------+
                |
                v
         Action / Response
                |
                v
          Text-to-Speech
```

JARVIS starts in a sleep state and waits for the wake word:

```text
"Hey Jarvis"
```

Once activated, it listens to the user's command, determines the best way to handle it, performs the requested action, and then returns to sleep mode.

---

## Voice Interaction

JARVIS uses Faster Whisper for speech recognition.

The voice pipeline works like this:

```text
Voice Input
    |
    v
Microphone
    |
    v
Faster Whisper
    |
    v
Text Command
    |
    v
JARVIS Processing
```

For example:

```text
You: "Jarvis, explain convolutional neural networks."

JARVIS: "Convolutional neural networks are deep learning models
commonly used for image-related tasks..."
```

---

## The Brain

Not every command needs a large language model.

One of the main ideas behind the project is to use a hybrid architecture where simple tasks are handled locally and more complex tasks are passed to the AI model.

```text
                    User Command
                         |
                         v
                   Command Router
                         |
              +----------+----------+
              |                     |
              v                     v
        Known Command          Complex Request
              |                     |
              v                     v
         Local Skill           AI Agent / LLM
              |                     |
              +----------+----------+
                         |
                         v
                 Response / Action
```

For example:

```text
"Open Calculator"
```

does not need an LLM. JARVIS can recognize the command and execute it immediately.

However:

```text
"Explain the difference between CNNs and Vision Transformers."
```

requires reasoning, so the request is sent to the LLM.

This approach helps reduce unnecessary API calls, improves response time for simple tasks, and keeps the system modular.

---

## Computer Vision

One of the main features of the project is Vision Mode.

JARVIS uses a webcam along with a YOLO-based object detection model to understand what is happening in its environment.

The pipeline looks like this:

```text
Webcam
   |
   v
OpenCV
   |
   v
YOLO Object Detection
   |
   v
Detected Objects
   |
   v
Visual Memory
```

When Vision Mode is activated, JARVIS can detect objects in real time.

Example:

```text
You: "Activate vision mode."

JARVIS: "Vision mode activated."
```

JARVIS can then detect objects such as:

* People
* Laptops
* Mobile phones
* Bottles
* Keyboards
* Books
* Chairs
* And other objects supported by the model

You can then ask:

```text
"What do you see?"
```

JARVIS can respond based on the objects it has recently detected.

For example:

```text
JARVIS: "I can currently see a person, a laptop, and a cell phone."
```

The vision system runs in a separate background thread so that object detection can continue while the rest of JARVIS remains responsive.

---

## System Control

JARVIS can perform basic actions on the computer.

Currently supported commands include:

```text
Open Chrome
Open Notepad
Open Calculator
Open File Explorer
Open VS Code

Close Chrome
Close Notepad
Close Calculator
Close VS Code

Take a screenshot
```

The goal is to gradually expand this into a more capable automation layer where JARVIS can perform multi-step tasks instead of only responding to individual commands.

---

## Web Actions

JARVIS can also perform basic web actions without needing to send every request to the LLM.

Examples:

```text
Search Google for deep learning tutorials
Search YouTube for computer vision projects
Open YouTube
Open GitHub
Open Google
```

These commands are routed directly to local skills.

```text
Command
   |
   v
Local Router
   |
   v
Web Skill
   |
   v
Action Executed
```

---

## Conversation Memory

JARVIS maintains short-term conversation memory to make interactions more contextual.

For example:

```text
You: "Explain CNNs."

JARVIS: "CNNs are deep learning models commonly used for
image processing."

You: "Give me a real-world example."

JARVIS understands that "me" refers to CNNs from the previous
conversation and can continue the discussion.
```

The current memory system is designed for short-term context and will eventually be expanded into a more advanced long-term memory system.

---

## Project Architecture

```text
JARVIS/
|
|-- main.py
|
|-- core/
|   |-- router.py
|   |-- agent_router.py
|   |-- memory.py
|   `-- wake_word_engine.py
|
|-- llm/
|   `-- brain.py
|
|-- voice/
|   |-- listener.py
|   `-- speaker.py
|
|-- vision/
|   |-- __init__.py
|   `-- vision_engine.py
|
|-- skills/
|   |-- system.py
|   |-- utilities.py
|   `-- web.py
|
|-- models/
|   `-- yolo11n.pt
|
|-- screenshots/
|
|-- .env
|-- requirements.txt
`-- README.md
```

---

## Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| Python           | Core application                |
| Faster Whisper   | Speech recognition              |
| OpenWakeWord     | Wake word detection             |
| Text-to-Speech   | Voice responses                 |
| Gemini API       | LLM reasoning                   |
| YOLO             | Real-time object detection      |
| OpenCV           | Camera and image processing     |
| Python Threading | Background vision processing    |
| Subprocess       | System and application control  |
| WebBrowser       | Web actions                     |
| dotenv           | Environment variable management |

---

## Current Capabilities

| Feature                        | Status  |
| ------------------------------ | ------- |
| Voice Commands                 | Working |
| Wake Word Detection            | Working |
| Voice Responses                | Working |
| LLM Integration                | Working |
| Short-Term Conversation Memory | Working |
| Local Command Routing          | Working |
| Google Search                  | Working |
| YouTube Search                 | Working |
| Open Applications              | Working |
| Close Applications             | Working |
| Screenshot Capture             | Working |
| Real-Time Object Detection     | Working |
| Background Vision Processing   | Working |
| Face Recognition               | Planned |
| Gesture Control                | Planned |
| Long-Term Memory               | Planned |
| Multi-Agent Planning           | Planned |

---

## The Road Ahead

This project is still evolving.

The current version focuses on making the core systems work together. The next goal is to make JARVIS more context-aware, autonomous, and capable of interacting with the world around it.

Some planned additions include:

```text
Current JARVIS
      |
      +-- Object Counting
      |
      +-- Object Location Awareness
      |
      +-- Face Recognition
      |
      +-- Hand Gesture Controls
      |
      +-- Screen Understanding
      |
      +-- Long-Term Vector Memory
      |
      +-- RAG-Based Knowledge System
      |
      +-- Multi-Agent Planning
      |
      +-- Smart Device Integration
      |
      `-- Local LLM Support
```

The goal is not to recreate the fictional JARVIS exactly.

The goal is to explore what happens when different AI systems — speech recognition, computer vision, language models, memory, agents, and automation — are integrated into one system.

---

## Why I Built This

I wanted to move beyond building individual machine learning models.

A computer vision model by itself is interesting.

A speech recognition model by itself is interesting.

An LLM by itself is interesting.

But the more interesting engineering challenge is figuring out how these systems can work together.

This project is my attempt to explore that.

```text
Speech AI
    +
Computer Vision
    +
Deep Learning
    +
Large Language Models
    +
AI Agents
    +
Memory
    +
Automation
    =
JARVIS
```

I am building this project module by module, with each new capability becoming part of a larger AI system.

The long-term goal is simple:

> Build an assistant that can perceive, reason, remember, and act.

One module at a time.

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd JARVIS
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Add the YOLO model

Place the required YOLO model inside:

```text
models/yolo11n.pt
```

### 6. Run JARVIS

```bash
python main.py
```

Then say:

```text
Hey Jarvis
```

---

## Built By

**Vaibhav Mohanty**

AI/ML Engineer

> *Tony Stark built JARVIS in a movie. I'm building mine one Python module at a time.*

---

## Project Status

This project is actively being developed.

It is not meant to be a finished product yet. It is an ongoing attempt to understand and build increasingly capable multimodal AI systems.

More capabilities are coming.

Hopefully, no Ultron.
