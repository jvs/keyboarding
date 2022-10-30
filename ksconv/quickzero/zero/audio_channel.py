from collections import deque
from dataclasses import dataclass
import threading
import time

from buzzer import Buzzer


@dataclass
class Note:
    frequency: float = None
    volume: float = None
    duration: float = 0.1


class AudioChannel:
    def __init__(self, buzzer_pin: int):
        self._buzzer = Buzzer(pin=buzzer_pin)
        self._thread = None

    def play_song(self, song: 'list[Note]'):
        self.stop_song()
        self._thread = _PlaybackThread(self._buzzer, song)
        self._thread.start()

    def stop_song(self):
        if self._thread is not None:
            self._thread.stop()
            self._thread.join()
            self._thread = None

    def wait(self):
        if self._thread is not None:
            self._thread.join()
            self._thread = None


class _PlaybackThread(threading.Thread):
    def __init__(self, buzzer: 'Buzzer', song: 'list[Note]'):
        threading.Thread.__init__(self)
        self._buzzer = buzzer
        self._song = deque(song)
        self._is_alive = True
        self._deadline = None

    def run(self):
        while self._is_alive:
            if self._deadline is not None and self._deadline > time.time():
                time.sleep(0.01)
                continue

            self._buzzer.stop()
            self._deadline = None

            if self._song:
                note = self._song.popleft()
                self._buzzer.start(frequency=note.frequency, volume=note.volume)
                self._deadline = time.time() + note.duration
            else:
                break

    def stop(self):
        self._is_alive = False
