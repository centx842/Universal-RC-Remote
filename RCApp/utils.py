import cv2
import pytz
import time
# import yaml
import socket
import threading
from PIL import Image, ImageTk
from datetime import date, datetime



''' PLaceholder Class to Accomodate WebCam Feed '''
class CameraFeed:

    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None
        self.camera_label = None
        self.thread = None
        self.running = False
        self._lock = threading.RLock()
        self._frame_size = (200, 150)  # default resize for label
        

    def set_label(self, camera_label):
        self.camera_label = camera_label
        return True


    def connect(self):
                
        #Create a VideoCapture Class from Library w.r.t Camera Indexing
        try: 
            self.cap = cv2.VideoCapture(self.camera_index)
            if not self.cap or not self.cap.isOpened():
                print(f"Error: Could not open camera index {self.camera_index}")
                if self.cap:
                    self.cap.release()
                    self.cap = None     # Ensure proper working when feed restarted...
                return False
            print(f"Camera connected (index={self.camera_index})")
            return True
        except Exception as e:
            print(f"Camera Connection Error: {e}")
            return False
        

    def start_stream(self):
        
        # Verify working of Capture Object and TKinter App's Camera Label defined...
        if not self.cap or not self.camera_label:
            print("Camera not properly initialized")
            return
        
        # Ensure Camera is not already working
        if self.running:
            print("Stream Already Running")
            return

        self.running = True
        self.thread = threading.Thread(target=self.camera_loop, daemon=True)
        self.thread.start()
        print("Camera Stream started in new Thread")
       

    def camera_loop(self):
        
        try:
            while True:
                with self._lock:
                    if not self.running:
                        break
                    cap = self.cap
                
                # Safety: no capture object available
                if not cap:
                    time.sleep(0.05)
                    continue

                # Transient Read Failure: wait and retry
                ret, frame = cap.read()
                if not ret or frame is None:
                    time.sleep(0.03)
                    continue

                # Convert color and resize into TKinter compatible Image
                try:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    img = img.resize(self._frame_size)
                    imgtk = ImageTk.PhotoImage(image=img)

                    # Schedule update on main thread; use after_idle or after(0)
                    if self.camera_label:
                        try:
                            self.camera_label.after(0, self.update_cam_label, imgtk)
                        except Exception:
                            # widget might be destroyed; stop streaming
                            with self._lock:
                                self.running = False
                            break
                except Exception as e:
                    print(f"Camera processing error: {e}")
                    time.sleep(0.03)
                    continue

                # modest sleep to avoid maxing CPU; frame pacing handled by camera read speed
                time.sleep(0.017)  # ~60 FPS cap
        
        
        except Exception as e:
            print(f"Camera loop exception: {e}")
        finally:
            # ensure resources cleaned up if loop exits unexpectedly
            with self._lock:
                self.running = False


    def update_cam_label(self, imgtk):
        self.camera_label.imgtk = imgtk                     # Make reference of newly compatible Image
        self.camera_label.configure(image=imgtk, text="")   # Ensure to remove text when showing image
            
    
    def disconnect(self, wait=True):
        with self._lock:
            self.running = False

        if self.thread and wait:
            self.thread.join(timeout=2.0)

        # release capture and clear label
        self.release()
        self.thread = None
        print("Camera disconnected")


    def release(self):
        
        with self._lock:
            # Destroy Capture Object
            if self.cap:
                self.cap.release()
                self.cap = None
        
        # Destroy Camera Label
        if self.camera_label:
            try:
                self.camera_label.configure(image="", text="Camera Feed")
                # drop reference
                if hasattr(self.camera_label, "imgtk"):
                    delattr(self.camera_label, "imgtk")
            except Exception:
                pass



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



''' Global Configuration Handling '''

config = None

def load_config(config_file):
    with open(config_file, 'r') as f:
        # return yaml.safe_load(f)
        pass

def set_config(config_file):
    global config
    config = load_config(config_file)
