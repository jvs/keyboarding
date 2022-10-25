# import usb_hid
# from adafruit_hid.keyboard import Keyboard


class Keyboard:
    def __init__(self):
        self._keyboard = None

    def press(self, keycode):
        print('press', keycode)
        # if self._keyboard is None:
        #     self._keyboard = Keyboard(usb_hid.devices)

        # try:
        #     return self._keyboard.press(keycode)
        # except Exception:
        #     self._keyboard = None
        #     raise

    def release(self, keycode):
        print('release', keycode)
        # if self._keyboard is None:
        #     self._keyboard = Keyboard(usb_hid.devices)

        # try:
        #     return self._keyboard.release(keycode)
        # except Exception:
        #     self._keyboard = None
        #     raise
