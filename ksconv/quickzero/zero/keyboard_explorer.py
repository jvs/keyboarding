import time
from input_channel import InputChannel


class KeyboardExplorer:
    @classmethod
    def run(cls):
        explorer = cls()
        keyboard_channel = InputChannel.create()
        keyboard_channel.set_handler(explorer)
        keyboard_channel.start()

        while True:
            time.sleep(0.1)

    def on_key_down(self, key: str):
        print('down:', repr(key))

    def on_key_up(self, key: str):
        print('up:', repr(key))


if __name__ == '__main__':
    KeyboardExplorer.run()
