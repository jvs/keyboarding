import keyboard

from keycodes import keycodes, keynames


class KeyboardChannel:
    def __init__(self):
        self._handler = None

    def set_handler(self, handler):
        self._handler = handler

    def start(self):
        keyboard.hook(self._on_keyboard_event, suppress=True)

    def _on_keyboard_event(self, event):
        if self._handler is None:
            return

        is_down = event.event_type == 'down'
        is_up = event.event_type == 'up'

        name = keynames.get(event.scan_code, event.name)
        print('keyboard event:', repr(name), is_down, is_up)

        if is_down:
            self._handler.on_key_down(name)
        elif is_up:
            self._handler.on_key_up(name)
