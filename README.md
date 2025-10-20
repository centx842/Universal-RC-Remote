# Universal RC Remote Control App

This project is designed to create a small, versatile remote control application for RC toys, styled after the familiar button layout of an Xbox controller. Built with Python and HTML, this app operates as both a desktop .NET application and a mobile application, offering seamless control over RC toys via Bluetooth, Wi-Fi, and RF communication modes.

## Features

- **Xbox-Inspired Button Layout**: The app mirrors the intuitive design of an Xbox controller, making it easy to control RC toys with a familiar interface.
- **Cross-Platform Support**:
  - **Desktop**: Runs as a .NET application on Windows.
  - **Mobile**: Compatible with Android and iOS devices.
- **Communication Options**:
  - Bluetooth: For short-range, direct connections.
  - Wi-Fi: For networked control over greater distances.
  - RF (Radio Frequency): For robust, hardware-supported communication.
- **Mode Switching**: A dedicated button or UI element allows users to switch between Bluetooth, Wi-Fi, and RF modes effortlessly.
- **Tech Stack**:
  - **Python**: Powers the backend logic and communication protocols.
  - **HTML**: Crafts a responsive, visually appealing frontend interface.

## Requirements

To develop and run this app, you'll need:

- **Python 3.x**: For backend development and communication handling.
- **.NET Framework**: For the desktop application (Windows).
- **Mobile Development Tools**: Android Studio (for Android) and Xcode (for iOS).
- **Communication Libraries**: Specific libraries for Bluetooth (e.g., PyBluez), Wi-Fi (e.g., sockets), and RF (e.g., PySerial or hardware-specific modules).

## How It Works

- **Frontend**: The HTML-based interface replicates an Xbox controller layout, capturing user inputs (e.g., button presses, joystick movements) and sending them to the backend.
- **Backend**: Python processes these inputs and communicates with the RC toy using the selected mode (Bluetooth, Wi-Fi, or RF).
- **Mode Switching**: A UI toggle updates the backend to use the chosen communication protocol dynamically.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/centx842/Universal-RC-Remote.git
   ```
   
2. **Check for current Python Version**:
   - First check your Python Version on Windows or Ubuntu Machine (using either 'python', 'python3', or even 'python310' in case of Ubuntu Machine)
     ```bash
     python --version
     ```
   - If Python version appears, proceed to the next step otherwise Install from Python.org.
  
3. **Creating an Environment**: 
   - Move into your Project Folder:
     ```bash
     cd path\to\your\project
     ```
   - Create your Environment Folder within the Project Folder:
     ```bash
     python -m venv <env_name>
     ```

### 4. **Activate the Virtual Environment**

* **For Windows:**

  ```bash
  <env_name>\Scripts\activate
  ```

* **For Linux/macOS:**

  ```bash
  source <env_name>/bin/activate
  ```

Once activated, upgrade the essential build tools:

```bash
pip install --upgrade pip setuptools wheel build
```

---

### 5. **Install Dependencies**

* **Python:**

  ```bash
  pip install -r requirements.txt
  ```

  *(Update this file with any additional libraries as needed.)*

* **.NET:**
  Ensure the **.NET SDK/Runtime** is installed and available in your system PATH.

* **Mobile:**
  Install and configure **Android Studio** and/or **Xcode** depending on your target platform.

---

### 6. **Run the Application**

* **Desktop:**

  ```bash
  python main.py
  ```

## Development Notes

- **Desktop**: Integrate Python with .NET using tools like IronPython or subprocesses.
- **Mobile**: Consider frameworks like BeeWare or Kivy for Python-based mobile apps with HTML frontends.
- **Communication**: Test with actual RC toys to ensure compatibility across all modes.

---

## ⚙️ **Build Binary**

### 🐧 **For Linux / macOS**

```bash
pyinstaller --onefile --add-data "images:images" main.py
```

📁 Add more resources later:

```bash
pyinstaller --onefile \
  --add-data "images:images" \
  --add-data "sounds:sounds" \
  --add-data "config:config" main.py
```

▶️ **Run the Binary**

```bash
cd dist
./main
```

---

### 🪟 **For Windows**

```powershell
pyinstaller --onefile --add-data "images;images" main.py
```

📁 Add more resources later:

```powershell
pyinstaller --onefile `
  --add-data "images;images" `
  --add-data "sounds;sounds" `
  --add-data "config;config" main.py
```

▶️ **Run the Binary**

```powershell
cd dist
main.exe
```

---

## Contributing

We’d love your help! Please check the [contributing guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
