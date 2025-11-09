import pytz
# import cv2
# from PIL import Image, ImageTk
from datetime import date, datetime
# import paho.mqtt.client as mqtt
import socket
import threading
import time


''' Function to add Date and Time Stamp to the Log Messages '''
class WiFiClient:

    def __init__(self, host="localhost", port=12345):
        self.host = host
        self.port = port
        self.sock = None
        self.server_addr = (host, port)
        self.lock = threading.Lock()
        self.create_socket()


    def create_socket(self):
        """Initialize UDP socket"""
        with self.lock:
            try:
                if self.sock:
                    self.sock.close()
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # Set timeout for non-blocking operations
                self.sock.settimeout(1.0)
                print(f"UDP client initialized for {self.host}:{self.port}")
            except Exception as e:
                print(f"Failed to initialize UDP socket: {e}")
                self.sock = None


    def connect(self):
        """Initialize UDP socket (UDP is connectionless)"""
        self.create_socket()


    def disconnect(self):
        """Close UDP socket"""
        with self.lock:
            if self.sock:
                try:
                    self.sock.close()
                    print("UDP client socket closed")
                except Exception as e:
                    print(f"Error closing UDP socket: {e}")
                finally:
                    self.sock = None


    def send_command(self, message):
        """Send a UDP command to the server"""
        with self.lock:
            if not self.sock:
                print("UDP socket not initialized")
                self.create_socket()
                if not self.sock:
                    return False

            try:
                # Send the message to the server
                self.sock.sendto(message.encode(), self.server_addr)
                print(f"Sent UDP command: {message}")
                return True
            except Exception as e:
                print(f"Failed to send UDP command: {e}")
                return False



def btCommand(command):
    print(f"Sending command over BT: {command}")
    pass

def rfCommand(command):
    print(f"Sending command over RF: {command}")
    pass


''' PLaceholder Class to Accomodate WebCam Feed '''

# class CameraFeed:
#     def __init__(self, camera_index=0):
#         self.camera_index = camera_index
#         self.cap = cv2.VideoCapture(self.camera_index)
#         if not self.cap.isOpened():
#             print("Error: Could not open camera.")
#             self.cap = None

#     def get_frame(self):
#         if self.cap:
#             ret, frame = self.cap.read()
#             if ret:
#                 # Convert the frame to RGB (OpenCV uses BGR by default)
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 img = Image.fromarray(frame)
#                 img = img.resize((200, 150))  # Match your camera_label size
#                 imgtk = ImageTk.PhotoImage(image=img)
#                 self.camera_label.imgtk = imgtk  # Keep reference
#                 self.camera_label.configure(image=imgtk, text="")  # Remove text when showing image
#                 return frame
#             else:
#                 print("Error: Could not read frame.")
#                 return None
#         return None

#     def release(self):
#         if hasattr(self, 'cap'):
#             self.cap.release()
#             self.camera_label.configure(image="", text="Camera Feed")


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