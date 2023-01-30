from keyboard_channel import KeyboardChannel
from mouse_channel import MouseChannel


class InputChannel:
    def __init__(self, keyboard_channel, mouse_channel):
        self._keyboard_channel = keyboard_channel
        self._mouse_channel = mouse_channel
        self._handler = None

    @classmethod
    def create(cls):
        keyboard_channel = KeyboardChannel()
        mouse_channel = MouseChannel()
        return cls(keyboard_channel, mouse_channel)

    def set_handler(self, handler):
        self._handler = handler

    def start(self):
        self._keyboard_channel.set_handler(self)
        self._mouse_channel.set_handler(self)

        self._keyboard_channel.start()
        self._mouse_channel.start()

    def on_key_down(self, key: str):
        if self._handler:
            self._handler.on_key_down(key)

    def on_key_up(self, key: str):
        if self._handler:
            self._handler.on_key_up(key)

    def on_mouse_down(self, button: str):
        self._keyboard_channel.simulate('down', 'mouse ' + button)

    def on_mouse_up(self, button: str):
        self._keyboard_channel.simulate('up', 'mouse ' + button)
