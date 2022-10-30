import board
import busio


class InputChannel:
    def __init__(self, tx=board.GP0, rx=board.GP1, baudrate=9600):
        self._uart = busio.UART(
            tx=tx,
            rx=rx,
            baudrate=baudrate,
            bits=8,
            parity=None,
            stop=1,
            timeout=1,
        )

    def read_byte(self):
        received = self._uart.read(1)
        if received is not None:
            return received[0]
