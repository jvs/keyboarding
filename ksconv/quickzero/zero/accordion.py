from collections import deque

from notes import notes


layout = '''
    `1234567890-=
    qwertyuiop[]\\
    asdfghjkl;'
    zxcvbnm,./
'''


class Accordion:
    def __init__(self, audio_channel: 'AudioChannel'):
        self._audio_channel = audio_channel
        self._layout = _build_layout(layout)
        self._current_key = None

    def on_key_down(self, key: str):
        if self._current_key == key:
            return
        if key in self._layout:
            self._current_key = key
            self._audio_channel.start(self._layout[key])

    def on_key_up(self, key: str):
        if self._current_key == key:
            self._audio_channel.stop()
            self._current_key = None


def _build_layout(layout_string, min_frequency=30, steps=2):
    result = {}

    index = 0
    while notes[index][1] <= min_frequency:
        index += 1

    for c in layout_string:
        if c == ' ' or c == '\n':
            continue
        result[c] = notes[index][1]
        index += steps

    print('layout:')
    print(result)
    return result
