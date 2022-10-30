import board
import RPi.GPIO as GPIO

from audio_channel import AudioChannel, Note

buzzer_pin = 12


def run():
    audio = AudioChannel(pin=buzzer_pin)
    song = [
        Note(frequency=200),
        Note(frequency=400, duration=1.0),
        Note(frequency=1000, duration=2.0),
        Note(frequency=500, duration=4.0),
        Note(frequency=200),
    ]
    audio.play_song(song)
    audio.wait()


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        run()
    finally:
        GPIO.cleanup()

