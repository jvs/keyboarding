import threading
import RPi.GPIO as GPIO


class Buzzer:
    def __init__(self, pin, frequency=110, volume=0.5):
        GPIO.setup(pin, GPIO.OUT)
        self._pin = pin
        self._frequency = frequency
        self._volume = volume
        self._pwm = GPIO.PWM(self._pin, frequency)
        self._is_busy = False

    def start(self, frequency=None, volume=None):
        if self._is_busy:
            self.stop()

        if frequency is not None:
            self._frequency = frequency
            self._pwm.ChangeFrequency(frequency)

        if volume is not None:
            self._volume = volume

        duty_cycle = int((2 ** 16 - 1) * volume)
        self._pwm.start(duty_cycle)
        self._is_busy = True

    def stop(self):
        if self._is_busy:
            self._pwm.stop()
            self._is_busy = False
