import RPi.GPIO as GPIO


class Buzzer:
    def __init__(self, pin, frequency=400):
        GPIO.setup(pin, GPIO.OUT)
        self._pin = pin
        self._frequency = frequency
        self._pwm = GPIO.PWM(self._pin, frequency)
        self._is_busy = False

    def start(self, frequency=None):
        if self._is_busy:
            self.stop()

        if frequency is not None:
            self._frequency = frequency
            self._pwm.ChangeFrequency(frequency)

        duty_cycle = 50
        self._pwm.start(duty_cycle)
        self._is_busy = True

    def stop(self):
        if self._is_busy:
            self._pwm.stop()
            self._is_busy = False
