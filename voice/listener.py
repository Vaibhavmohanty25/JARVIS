import os
import tempfile

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


class JarvisListener:
    def __init__(self, model_size="base.en"):
        print("Loading speech recognition model...")

        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

        print("Speech recognition model loaded successfully.")

    def listen(self, duration=5, sample_rate=16000):
        """
        Record audio from the microphone and convert speech to text.
        """

        print(f"\nListening for {duration} seconds...")
        print("Speak now!")

        # Record audio from microphone
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )

        # Wait until recording is complete
        sd.wait()

        print("Processing your speech...")

        # Create a temporary WAV file
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_file:

            temp_path = temp_file.name

        try:
            # Save recorded audio
            write(
                temp_path,
                sample_rate,
                audio
            )

            # Convert speech to text
            segments, info = self.model.transcribe(
                temp_path,
                beam_size=5
            )

            # Combine all recognized segments
            text = ""

            for segment in segments:
                text += segment.text

            return text.strip()

        except Exception as error:
            print(f"Speech recognition error: {error}")
            return ""

        finally:
            # Delete temporary audio file
            if os.path.exists(temp_path):
                os.remove(temp_path)