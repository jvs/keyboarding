import time

from input_channel import InputChannel
from keyboard import Keyboard


channel = InputChannel()
keyboard = Keyboard()


while True:
    try:
        command = channel.read_byte()

        if command != 1 and command != 2:
            raise Exception(f'Unexpected command: {command}')

        keycode = channel.read_byte()

        if command == 1:
            keyboard.press(keycode)
        else:
            keyboard.release(keycode)
    except Exception as exc:
        print(str(exc))
        time.sleep(0.2)
