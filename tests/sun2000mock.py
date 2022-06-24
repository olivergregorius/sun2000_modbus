from pymodbus.exceptions import ModbusIOException


class MockedResponse:
    def __init__(self, address, quantity):
        self.address = address
        self.quantity = quantity

    def encode(self):
        return MockedRegisters[(self.address, self.quantity)]


MockedRegisters = {
    # Model - 'SUN2000'
    (30000, 15): b'\x1eSUN2000\x00\x00\x00',

    # ModelID - 429
    (30070, 1): b'\x02\x01\xad',

    # RatedPower - 10000
    (30073, 2): b"\x04\x00\x00'\x10",

    # State1 - '0000000000000110'
    (32000, 1): b'\x02\x00\x06',

    # DeviceStatus - 512
    (32089, 1): b'\x02\x02\x00'
}


def mock_read_holding_registers(self, address, quantity, unit):
    return MockedResponse(address, quantity)


def mock_read_holding_registers_fail(self, address, quantity, unit):
    return ModbusIOException("Requested unit is not available")


def connect_success(self):
    return True


def connect_fail(self):
    return False
