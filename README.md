🎙️ NovelAI TTS Qt GUI
A simple and user-friendly PySide6 GUI to generate and play speech using NovelAI's text-to-speech (TTS) engine. Supports:

🎧 Real-time audio preview

🧬 Voice identity via seed (e.g. Raid, Ember+Raid, etc.)

🔊 Exporting audio in .mp3, .wav, or .opus format

📁 API key management via .env file

📦 Features
Generate speech using NovelAI's /ai/generate-voice endpoint

Preview audio instantly in-app

Save TTS output to file in your preferred format

Cross-platform GUI using PySide6

Easy to configure and extend

📂 Project Structure
bash
Copy
Edit
.
├── tts.py               # Main GUI script
├── .env                 # Store your NovelAI API key securely
├── requirements.txt     # Python dependencies
└── README.md            # You’re reading it
🚀 Getting Started
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/novelai-tts-gui.git
cd novelai-tts-gui
2. Install dependencies
Make sure you’re in a virtual environment, then:

bash
Copy
Edit
pip install -r requirements.txt
3. Configure your API key
Create a .env file with your NovelAI token:

ini
Copy
Edit
NOVELAI_API_KEY=your_novelai_api_key_here
Or copy the example:

bash
Copy
Edit
cp .env.example .env
4. Run the app
bash
Copy
Edit
python tts.py
💡 Usage
Enter the text you want spoken.

Specify a voice seed like Raid, Ember, or a blend like Ember+Raid.

Choose whether to use .opus internally.

Pick a format to save (.mp3, .wav, or .opus).

Click Generate & Play to listen.

Click Save Audio to export the result.

🎤 Voice Tips
Voice seed values are case-sensitive and may reflect specific speaker styles (e.g. Raid is different from raid).

You can blend voices using +, like Ember+Raid.

🛠️ Built With
PySide6 — for the Qt GUI

Requests — to make HTTP API calls

python-dotenv — to securely manage your API key

📄 License
MIT – do whatever you want, just don’t blame me.
