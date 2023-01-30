import keyboard


_scancode_map = {
    29: 'left ctrl',
    42: 'left shift',
    54: 'right shift',
    56: 'left alt',
    97: 'right ctrl',
    99: 'print screen',
    100: 'right alt',
    125: 'left gui',
}

_unicode_map = {
    '\u2212': '-',
}


class KeyboardChannel:
    def __init__(self):
        self._handler = None
        self._currently_down = set()

    def set_handler(self, handler):
        self._handler = handler

    def start(self):
        keyboard.hook(self._on_keyboard_event, suppress=True)

    def simulate(self, event_type: str, key: str):
        is_down = event_type == 'down'
        is_up = event_type == 'up'

        if not is_down and not is_up:
            return

        if is_down:
            self._currently_down.add(key)
        elif is_up:
            self._currently_down.discard(key)

        if self._handler is not None:
            if is_down:
                self._handler.on_key_down(key)
            elif is_up:
                self._handler.on_key_up(key)

    def _on_keyboard_event(self, event):
        event_type = event.event_type
        key = _scancode_map.get(event.scan_code, event.name)
        key = _unicode_map.get(key, key)
        self.simulate(event_type, key)
