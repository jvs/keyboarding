import time

import board
import RPi.GPIO as GPIO

from accordion import Accordion
from audio_channel import AudioChannel, Note
from buzzer import Buzzer
from keyboard_channel import KeyboardChannel


buzzer_pin = 12

startup_song = [
    Note(frequency=200),
    Note(frequency=400, duration=0.2),
    Note(frequency=1000, duration=0.2),
]


def run():
    buzzer = Buzzer(pin=buzzer_pin)
    audio_channel = AudioChannel(buzzer=buzzer)
    audio_channel.play_song(startup_song)
    audio_channel.wait()

    accordion = Accordion(audio_channel=audio_channel)

    keyboard_channel = KeyboardChannel()
    keyboard_channel.set_handler(accordion)
    keyboard_channel.start()

    while True:
        time.sleep(0.1)


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        run()
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
