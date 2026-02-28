<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Smart Priority Based Traffic System Using YOLO system] 🎯

## Basic Details

### Team Name: [Bug Busters]

### Team Members
- Member 1: [Nazrin Nizam N] - [College of Engineering Perumon]
- Member 2: [Krishnaveni M L] - [College of Engineering Perumon]

### Hosted Project Link
[mention your project hosted link here]

## 📌 Project Overview
Our system doesn't just react to traffic; it **understands** the road. 

By leveraging the **YOLO (You Only Look Once)** AI framework, SmartVision transitions traffic management from static, timer-based cycles to a **Vision-to-Action** pipeline. The system identifies vehicle density in real-time and dynamically prioritizes lanes, ensuring that a lane with 50 vehicles isn't held up by a "dumb" timer while an empty lane sits with a green light.



## ❌ The Problem: The "Boring" 60-Second Wait
Traditional traffic light systems are either manually controlled or rely on fixed timers. This leads to massive inefficiencies:
* **Static Latency:** Every lane is forced to wait for a pre-set duration (e.g., 60s), regardless of actual traffic volume.
* **Empty Lane Greening:** Situations where a lane with zero vehicles holds a green light while other lanes are congested.
* **Congestion Cascades:** Poorly timed lights lead to "stop-and-go" traffic, increasing fuel consumption and commuter frustration.

## ✅ The Solution: Density-Based Prioritization
Our approach replaces fixed timers with a **Time-Selective System** based on real-time visual data:

1.  **Vehicle Counting:** Uses YOLO object detection to identify cars, trucks, and motorcycles across all lanes.
2.  **Lane Prioritization:** Ranks lanes based on their current vehicle density.
3.  **Dynamic Timing:** Allocates green-light duration proportionally to the count of vehicles detected.
4.  **OpenCV Integration:** Designed to scale from static image processing to real-time video stream analysis.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used:Python,
- Frameworks used: [streamlit]
- Libraries used: [pandas,YOLO(detecting number of cars)]
- Tools used: [VS Code, Git, Arduino IDE, Gemini,]

**For Hardware:**
- Main components: [ESP32]
- Specifications: [An adaptive traffic light system using ESP32 DEV MODULE operates with a clock spped upto 240MHz ,analyzes uploaded images to detect vehicle density and dynamically controols LED traffic signals by adjusting green time based on traffic priority]
- Tools required: [ESP32 DEV MODULE, breadboard jumper wire, laptop, web development tools]

---

## Features

List the key features of your project:
- Feature 1: [Real time Traffiv monitoring system ]
- Feature 2: [Dynamic signal timing adjustments]
- Feature 3: [Pedistrian aware operation ]
- Feature 4: [reduced traffic congestion]

---

## Implementation

### For Software:

  #### Installation
## Quick setup (PowerShell)
```powershell
cd c:\Users\KRISHNA_VENI\bug
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
# Install CPU PyTorch (or follow https://pytorch.org for GPU)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install streamlit ultralytics pyserial pillow pandas
```

## Files
- app.py — Streamlit app (main)
- yolo11s.pt — Place model weights in repo root

## Run
```powershell
streamlit run app.py
```

### For Hardware:

#### Components Required
[ESP32]

#### Circuit Setup
[Explain how to set up the circuit]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
Image Upload → Vehicle Detection → Density Calculation → Priority Decision → Wi-Fi Transmission → ESP32 → Traffic Signal Control

![Workflow](docs/workflow.png)
Lane images are uploaded through the web interface, where vehicle detection and density analysis are performed; based on the calculated traffic priority, control commands are sent via Wi-Fi to the ESP32 Dev Module, which dynamically adjusts the traffic signals by allocating green time to the lane with higher vehicle density.

---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
