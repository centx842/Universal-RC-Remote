import pytz
import cv2
from PIL import Image, ImageTk
from datetime import date, datetime
import paho.mqtt.client as mqtt


''' Placeholder Classes and Functions to simulate sending a command over WiFi, Bluetooth or RF Hardware'''
class MQTTClient:
    def __init__(self, broker="localhost", port=1883, topic="rc/commands"):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        # self.client.connect(self.broker, self.port)

    def send_command(self, message):
        self.client.publish(self.topic, message)

def btCommand(command):
    print(f"Sending command over BT: {command}")
    pass

def rfCommand(command):
    print(f"Sending command over RF: {command}")
    pass


''' PLaceholder Class to Accomodate WebCam Feed '''

class CameraFeed:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            self.cap = None

    def get_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                # Convert the frame to RGB (OpenCV uses BGR by default)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = img.resize((200, 150))  # Match your camera_label size
                imgtk = ImageTk.PhotoImage(image=img)
                self.camera_label.imgtk = imgtk  # Keep reference
                self.camera_label.configure(image=imgtk, text="")  # Remove text when showing image
                return frame
            else:
                print("Error: Could not read frame.")
                return None
        return None

    def release(self):
        if hasattr(self, 'cap'):
            self.cap.release()
            self.camera_label.configure(image="", text="Camera Feed")


''' Function to add Date and Time Stamp to the Log Messages '''
def add_time_stamp():
    
    # Define the date
    date_today = date.today()
    date_str = date_today.isoformat()

    # Get the current time in the specified timezone
    timezone = pytz.timezone('Asia/Karachi')
    current_time_str = datetime.now(timezone).strftime("%H:%M:%S")

    # Concatenating Date and Time onto TimeStamp
    dt_stamp_msg = f" EVENT --- [{date_str} | {current_time_str}] --> "

    return dt_stamp_msg