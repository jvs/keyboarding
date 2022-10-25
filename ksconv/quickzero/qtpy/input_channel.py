import board
import busio


class InputChannel:
    def __init__(self, i2c, device_address, status_channel):
        self._i2c = i2c
        self._device_address = device_address
        self._status_channel = status_channel
        self._buffer = bytearray(2)

    @classmethod
    def create(cls, status_channel):
        while True:
            try:
                status_channel.indicate_busy()
                i2c = board.STEMMA_I2C()
                break
            except Exception:
                status_channel.indicate_error(sleep=1)

        while True:
            status_channel.indicate_busy()

            while not i2c.try_lock():
                status_channel.indicate_error(sleep=0.1)

            try:
                device_addresses = i2c.scan()
            finally:
                i2c.unlock()

            if len(device_addresses) == 1:
                status_channel.indicate_ready()
                return cls(
                    i2c=i2c,
                    device_address=device_addresses[0],
                    status_channel=status_channel,
                )
            else:
                status_channel.indicate_error(sleep=0.25)

    def read_command(self):
        while not self._i2c.try_lock():
            self._status_channel.indicate_error(sleep=0.1)

        try:
            self._i2c.readfrom_into(self._device_address, self._buffer)
            return self._buffer
        finally:
            self._i2c.unlock()
