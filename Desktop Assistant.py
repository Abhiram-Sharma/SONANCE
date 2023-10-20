import io
import os
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
import speech_recognition as sr

def transcribe_audio():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        # Record audio from the microphone
        print("Listening...")
        audio = recognizer.listen(source)

        # Try to recognize the speech in the recording
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config)

    audio = AudioSegment(
        data=response.audio_content, 
        sample_width=2, 
        frame_rate=22050, 
        channels=1
    )
    play(audio)


x=transcribe_audio

class DesktopAssistant(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.change_color_scheme()

    def initUI(self):
        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Type your message here...")
        layout.addWidget(self.text_edit)

        start_button = QPushButton('Start Listening', self)
        start_button.clicked.connect(self.start_listening)
        layout.addWidget(start_button)

        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

        self.setWindowTitle('Desktop Assistant')
        self.show()

    def start_listening(self):
        # Add your code to start listening here
        pass
    def change_color_scheme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.black)
        self.setPalette(palette)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop_assistant = DesktopAssistant()
    desktop_assistant.show()
    sys.exit(app.exec_())
