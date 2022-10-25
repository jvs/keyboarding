from machine import mem32


class InputChannel:
    I2C1_BASE = 0x40048000
    IO_BANK0_BASE = 0x40014000

    mem_rw =  0x0000
    mem_xor = 0x1000
    mem_set = 0x2000
    mem_clr = 0x3000

    IC_CON = 0
    IC_SAR = 8
    IC_DATA_CMD = 0x10
    IC_ENABLE = 0x6c
    IC_STATUS = 0x70

    def __init__(self):
        self._sda = 22
        self._scl = 23
        self._device_address = 0x41
        self._i2c_base = self.I2C1_BASE

    @classmethod
    def create(cls, status_channel):
        self = cls()

        # Disable DW_apb_i2c.
        self._clr_reg(self.IC_ENABLE, 1)

        # Set device address.
        self._clr_reg(self.IC_SAR, 0x1ff)
        self._set_reg(self.IC_SAR, self._device_address & 0x1ff)

        # Write IC_CON 7 bit, enable in slave-only.
        self._clr_reg(self.IC_CON, 0b01001001)

        # Set SDA PIN.
        mem32[self.IO_BANK0_BASE | self.mem_clr | (4 + 8 * self._sda)] = 0x1f
        mem32[self.IO_BANK0_BASE | self.mem_set | (4 + 8 * self._sda)] = 3

        # Set SLA PIN.
        mem32[self.IO_BANK0_BASE | self.mem_clr | (4 + 8 * self._scl)] = 0x1f
        mem32[self.IO_BANK0_BASE | self.mem_set | (4 + 8 * self._scl)] = 3

        # Enable i2c.
        self._set_reg(self.IC_ENABLE, 1)

        return self

    def read(self):
        while not self._is_ready():
            pass
        return mem32[self._i2c_base | self.IC_DATA_CMD] & 0xff

    def _is_ready(self):
        # Get IC_STATUS.
        status = mem32[self._i2c_base | self.IC_STATUS]

        # Check RFNE receive fifio not empty.
        return bool(status & 8)

    def _clr_reg(self, reg, data):
        self._write_reg(reg, data, method=self.mem_clr)

    def _set_reg(self, reg, data):
        self._write_reg(reg, data, method=self.mem_set)

    def _write_reg(self, reg, data, method=0):
        mem32[self._i2c_base | method | reg] = data
