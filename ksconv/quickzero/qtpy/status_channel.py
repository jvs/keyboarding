import time

import board
import neopixel


class StatusChannel:
    def __init__(self, pixel):
        self._pixel = pixel

    @classmethod
    def create(cls):
        pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
        pixel.brightness = 0.3
        return cls(pixel=pixel)

    def indicate_busy(self):
        self._pixel.fill((0, 0, 255))

    def indicate_error(self, sleep=0):
        self._pixel.fill((0, 0, 255))
        if sleep > 0:
            time.sleep(sleep)

    def indicate_ready(self):
        self._pixel.fill((0, 255, 0))
