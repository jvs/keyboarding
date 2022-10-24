import time

import board
import busio

# i2c = board.I2C()

i2c = busio.I2C(board.SCL1, board.SDA1)

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)
        break

finally:
    i2c.unlock()
