import keyboard


_keynames = {
    29: 'left ctrl',
    42: 'left shift',
    54: 'right shift',
    56: 'left alt',
    97: 'right ctrl',
    99: 'print screen',
    100: 'right alt',
    125: 'left gui',
}

_ascii_names = {
    '\u2212': '-',
}


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

        name = _keynames.get(event.scan_code, event.name)
        name = _ascii_names.get(name, name)

        if is_down:
            self._handler.on_key_down(name)
        elif is_up:
            self._handler.on_key_up(name)
