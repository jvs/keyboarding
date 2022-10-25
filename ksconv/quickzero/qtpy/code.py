from keyboard import Keyboard
from input_channel import InputChannel
from status_channel import StatusChannel


status_channel = StatusChannel.create()
input_channel = InputChannel.create(status_channel=status_channel)
keyboard = Keyboard()


while True:
    status_channel.indicate_ready()
    try:
        command, keycode = input_channel.read_command()

        if command == 1:
            keyboard.press(keycode)
        elif command == 2:
            keyboard.release(keycode)
        else:
            status_channel.indicate_error(sleep=0.1)
    except Exception:
        status_channel.indicate_error(sleep=0.1)
