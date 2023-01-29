from collections import deque

from notes import notes

layout = '''
    `: C
    1: D#
    2: F#
    3: A
    4: C
    5: D#
    6: F#
    7: A
    8: C
    9: D#
    0: F#
    -: A
    =: C

    q: E
    w: G
    e: A#
    r: C#
    t: E
    y: G
    u: A#
    i: A#
    o: E
    p: G
    [: A#
    ]: C#
    \\: E

    a: F
    s: G#
    d: B
    f: D
    g: F
    h: G#
    j: B
    k: D
    l: F
    ;: G#
    ': B

    z: F#
    x: A
    c: C
    v: D#
    b: F#
    n: A
    m: C
    ,: D#
    .: F#
    /: A
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


def _build_layout(layout_string, min_frequency=400):
    result = {}
    next_notes = deque(notes)
    print('notes:')
    print(next_notes)

    for line in layout_string.split('\n'):
        line = line.strip()
        if not line:
            continue
        key, note = line.split(': ')
        print('looking for', repr(key), repr(note))

        while next_notes:
            next_note, next_frequency = next_notes.popleft()
            print('  considering', repr(next_note), repr(next_frequency))
            if next_frequency < min_frequency:
                print('     too low')
                continue
            if note == next_note:
                print('      found!')
                result[key] = next_frequency
                break
            else:
                print('      wrong note')

    print('\nlayout:')
    print(result)
    return result
