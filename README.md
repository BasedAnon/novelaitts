NovelAI TTS Qt GUI

A simple and user-friendly PySide6 GUI to generate and play speech using NovelAI's text-to-speech (TTS) engine.

FEATURES

Real-time audio preview

Voice identity via seed (e.g. Raid, Ember+Raid)

Export audio in .mp3, .wav, or .opus format

API key managed via .env file

Easy to configure and extend

PROJECT STRUCTURE

tts.py -> Main GUI script

.env -> Stores your NovelAI API key (not committed)

requirements.txt -> Python dependencies

README.txt -> This file

GETTING STARTED

Clone the repository

git clone https://github.com/YOUR_USERNAME/novelai-tts-gui.git cd novelai-tts-gui

Install dependencies (it is recommended to use a virtual environment)

pip install -r requirements.txt

Configure your API key

Create a .env file in the root of the project with the following line:

NOVELAI_API_KEY=your_novelai_api_key_here

Alternatively, you can copy and edit an example:

cp .env.example .env

Run the app

python tts.py

USAGE

Enter the text you want the voice to speak.

Enter a voice seed, such as Raid, Ember, or a blend like Ember+Raid.

Optionally check "Use Opus format" if you want the audio processed internally in opus format.

Choose the output format: mp3, wav, or opus.

Click "Generate & Play" to preview the audio.

Click "Save Audio" to export it to a file.

VOICE TIPS

Voice seeds are case-sensitive. Raid and raid produce different results.

You can blend voices using a plus sign, like Ember+Raid.

Longer text samples will better reflect changes in voice seed and rhythm.

DEPENDENCIES

PySide6: for the Qt GUI

requests: for sending API calls

python-dotenv: for loading API key from .env

LICENSE

MIT License — free to use, modify, and distribute.
Do whatever you want, just don’t blame me.
