import numpy as np
import sounddevice as sd
from openwakeword.model import Model


class WakeWordEngine:

    def __init__(
        self,
        model_name="hey_jarvis",
        threshold=0.5,
        sample_rate=16000,
        device_id=None
    ):

        print("Loading Hey Jarvis wake word model...")

        self.model = Model(
            wakeword_models=[model_name],
            inference_framework="onnx"
        )

        self.model_name = model_name
        self.threshold = threshold
        self.sample_rate = sample_rate
        self.device_id = device_id

        print("Wake word engine loaded successfully.")


    def wait_for_wake_word(self):

        print("\nJARVIS is sleeping...")
        print("Waiting for: Hey Jarvis")

        block_size = 1280

        # This stream automatically closes when the
        # wake word is detected and this method returns
        with sd.RawInputStream(
            samplerate=self.sample_rate,
            blocksize=block_size,
            dtype="int16",
            channels=1,
            device=self.device_id
        ) as stream:

            while True:

                audio_data, overflowed = stream.read(block_size)

                if overflowed:
                    print("Warning: Audio overflow detected.")

                audio = np.frombuffer(
                    audio_data,
                    dtype=np.int16
                )

                predictions = self.model.predict(audio)

                score = predictions.get(
                    self.model_name,
                    0
                )

                if score >= self.threshold:

                    print(
                        f"\nWake word detected! "
                        f"Confidence: {score:.2f}"
                    )

                    return True