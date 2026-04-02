# 🎧 Sound Map of Your Room (Real-Time Audio Visualization)

Sound Map is a real-time visualization system built using Python 🐍, Pygame 🎮, NumPy 📊, and SoundDevice 🎤.

The system captures ambient audio from your microphone and converts it into a dynamic terrain-like visual map, where sound intensity is represented through color and motion.

---

# ✨ Features

🎤 Real-Time Audio Capture  
- Captures live microphone input  
- Detects even low-level sounds  

🌊 Dynamic Terrain Visualization  
- Converts sound into flowing grid-based terrain  
- Smooth motion using rolling arrays  

🎨 Color-Based Intensity Mapping  
- Low sound → darker colors  
- High sound → brighter colors  

⚡ Smooth & Responsive Rendering  
- Uses smoothing and decay for natural transitions  
- Real-time updates using Pygame  

🔇 Noise Filtering & Amplification  
- Removes background noise  
- Amplifies subtle sounds  

---

# 📂 Project Structure

Sound-Map/
│── Sound Map.py
│── requirements.txt
│── README.md
│── LICENSE

---

# ⚙️ Installation

1️⃣ Clone the Repository  

git clone https://github.com/rsamwilson2323-cloud/Sound-Map.git  
cd Sound-Map  

---

2️⃣ Install Dependencies  

pip install -r requirements.txt  

---

# 📦 Requirements

numpy  
pygame  
sounddevice  

---

# ▶️ Usage

Run the project  

python "Sound Map.py"

🎧 The system will start listening automatically  

To stop the program  
Press ENTER ⏎  

---

# 🧠 How It Works

🎤 Audio Processing  
Captures microphone input using SoundDevice  

📊 Signal Processing  
Uses NumPy to filter noise and smooth sound  

🌊 Terrain Generation  
Creates rolling terrain updated by sound  

🎮 Rendering  
Pygame draws real-time colored grid  

---

# ⚙️ Key Parameters

NOISE_FLOOR = 0.005  
GAIN = 22.0  
SMOOTHING = 0.80  
DECAY = 0.975  

---

# 📸 Example Output

Low Sound → Dark Grid  
Medium Sound → Mixed Colors  
High Sound → Bright Terrain  

---

# 🚀 Future Improvements

🔊 Sound alerts  
🌈 Better color themes  
🧠 AI sound detection  
📊 Sound analytics  
📱 App version  

---

# ⚠️ Disclaimer

This project is for educational and creative purposes only.

---

# 👨‍💻 Author

Sam Wilson  

GitHub: https://github.com/rsamwilson2323-cloud  
LinkedIn: https://www.linkedin.com/in/sam-wilson-14b554385  

---

# 📜 License

MIT License
