import sys
import tempfile
import requests
import os
from dotenv import load_dotenv  # Load .env file
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QTextEdit, QCheckBox, QFileDialog, QComboBox
)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("NOVELAI_API_KEY")

API_URL = "https://api.novelai.net/ai/generate-voice"

class TTSWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NovelAI TTS")
        self.setGeometry(100, 100, 400, 360)

        self.text_input = QTextEdit()
        self.voice_seed_input = QLineEdit()
        self.opus_checkbox = QCheckBox("Use Opus format")
        self.format_selector = QComboBox()
        self.format_selector.addItems(["mp3", "wav", "opus"])

        self.play_button = QPushButton("Generate & Play")
        self.save_button = QPushButton("Save Audio")
        self.status_label = QLabel("Status: Idle")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter text to synthesize:"))
        layout.addWidget(self.text_input)
        layout.addWidget(QLabel("Voice Seed or Blend (e.g., Raid or Ember+Raid):"))
        layout.addWidget(self.voice_seed_input)
        layout.addWidget(self.opus_checkbox)
        layout.addWidget(QLabel("Save Format:"))
        layout.addWidget(self.format_selector)
        layout.addWidget(self.play_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

        self.play_button.clicked.connect(self.generate_and_play)
        self.save_button.clicked.connect(self.save_audio_dialog)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.last_audio_data = None
        self.last_audio_ext = None

    def generate_and_play(self):
        if not API_KEY:
            self.status_label.setText("Error: API key not found. Check .env file.")
            return

        text = self.text_input.toPlainText().strip()
        seed = self.voice_seed_input.text().strip()
        opus = self.opus_checkbox.isChecked()

        if not text:
            self.status_label.setText("Status: Please enter some text.")
            return

        self.status_label.setText("Status: Generating audio...")

        try:
            params = {
                "text": text,
                "voice": -1,
                "seed": seed,
                "opus": str(opus).lower(),
                "version": "v2"
            }

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "audio/mpeg"
            }

            request_url = requests.Request('GET', API_URL, params=params).prepare().url
            print("Final Request URL:", request_url)
            print("Headers:", headers)

            response = requests.get(API_URL, headers=headers, params=params)

            if response.status_code != 200:
                print("Error response text:", response.text)
                self.status_label.setText(f"Error: {response.status_code}")
                return

            ext = ".webm" if opus else ".mp3"
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as f:
                f.write(response.content)
                audio_file_path = f.name

            self.last_audio_data = response.content
            self.last_audio_ext = ext

            self.player.setSource(QUrl.fromLocalFile(audio_file_path))
            self.player.play()
            self.status_label.setText("Status: Playing audio.")

        except Exception as e:
            print("Exception during TTS request:", e)
            self.status_label.setText(f"Error: {str(e)}")

    def save_audio_dialog(self):
        if not self.last_audio_data:
            self.status_label.setText("No audio to save. Please generate first.")
            return

        file_format = self.format_selector.currentText()
        default_ext = f".{file_format}"
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Audio", f"output{default_ext}", f"*.{file_format}")

        if file_path:
            if not file_path.lower().endswith(default_ext):
                file_path += default_ext

            try:
                with open(file_path, 'wb') as f:
                    f.write(self.last_audio_data)
                self.status_label.setText(f"Saved to: {file_path}")
            except Exception as e:
                self.status_label.setText(f"Save failed: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TTSWindow()
    window.show()
    sys.exit(app.exec())
