import mouse


class MouseChannel:
    def __init__(self):
        self._handler = None
        self._currently_down = set()

    def set_handler(self, handler):
        self._handler = handler

    def start(self):
        mouse.hook(self._on_mouse_event)

    def _on_mouse_event(self, event):
        if not hasattr(event, 'event_type'):
            return

        button = event.button
        event_type = event.event_type

        is_down = event_type == 'down'
        is_up = event_type == 'up'

        if not is_down and not is_up:
            return

        if is_down:
            self._currently_down.add(button)
        elif is_up:
            self._currently_down.discard(button)

        if self._handler is not None:
            if is_down:
                self._handler.on_mouse_down(button)
            elif is_up:
                self._handler.on_mouse_up(button)
