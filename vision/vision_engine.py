import os
import cv2
import threading
from ultralytics import YOLO


class VisionEngine:

    def __init__(self, model_name="models/yolo11n.pt"):

        print("Loading JARVIS vision model...")

        if not os.path.exists(model_name):
            raise FileNotFoundError(
                f"YOLO model not found at: {model_name}"
            )

        self.model = YOLO(model_name)

        # Store detected objects
        self.last_detected_objects = []

        # Vision state
        self.is_running = False
        self.vision_thread = None
        self.cap = None

        # Protect shared object data
        self.lock = threading.Lock()

        print("JARVIS vision model loaded successfully.")


    # ==========================================
    # BACKGROUND VISION LOOP
    # ==========================================

    def _vision_loop(self):

        print("\nJARVIS Vision Mode started.")
        print("Webcam is now active.")

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():

            print("Error: Could not access webcam.")

            self.is_running = False

            return


        while self.is_running:

            success, frame = self.cap.read()

            if not success:

                print("Error: Could not read webcam frame.")

                break


            # Run YOLO detection
            results = self.model(
                frame,
                verbose=False
            )


            detected_objects = set()

            annotated_frame = frame.copy()


            for result in results:

                annotated_frame = result.plot()

                if result.boxes is not None:

                    for class_id in result.boxes.cls:

                        class_name = self.model.names[
                            int(class_id)
                        ]

                        detected_objects.add(
                            class_name
                        )


            # Update shared object memory safely
            with self.lock:

                self.last_detected_objects = list(
                    detected_objects
                )


            # Show webcam window
            cv2.imshow(
                "JARVIS Vision Mode",
                annotated_frame
            )


            # Optional: Press Q to stop vision
            if cv2.waitKey(1) & 0xFF == ord("q"):

                self.is_running = False

                break


        # Cleanup
        if self.cap is not None:

            self.cap.release()


        cv2.destroyAllWindows()

        self.is_running = False

        print("\nJARVIS Vision Mode stopped.")


    # ==========================================
    # START VISION MODE
    # ==========================================

    def start_vision_mode(self):

        if self.is_running:

            return "Vision mode is already active."


        self.is_running = True


        # Start vision in background
        self.vision_thread = threading.Thread(
            target=self._vision_loop,
            daemon=True
        )

        self.vision_thread.start()


        return "Vision mode activated."


    # ==========================================
    # STOP VISION MODE
    # ==========================================

    def stop_vision_mode(self):

        if not self.is_running:

            return "Vision mode is not currently active."


        print("\nStopping vision mode...")

        self.is_running = False


        # Wait for thread to finish
        if (
            self.vision_thread is not None
            and self.vision_thread.is_alive()
        ):

            self.vision_thread.join(
                timeout=3
            )


        return "Vision mode stopped."


    # ==========================================
    # WHAT DOES JARVIS SEE?
    # ==========================================

    def get_last_detected_objects(self):

        with self.lock:

            objects = list(
                self.last_detected_objects
            )


        if not objects:

            return (
                "I cannot see any recognizable objects right now."
            )


        if len(objects) == 1:

            return (
                f"I can currently see a {objects[0]}."
            )


        # Make the list sound natural
        if len(objects) == 2:

            object_text = (
                f"{objects[0]} and {objects[1]}"
            )

        else:

            object_text = (
                ", ".join(objects[:-1])
                + f", and {objects[-1]}"
            )


        return (
            f"I can currently see {object_text}."
        )