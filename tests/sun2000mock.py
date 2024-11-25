from pymodbus.exceptions import ModbusIOException, ConnectionException


class MockedResponse:
    def __init__(self, address, quantity):
        self.address = address
        self.quantity = quantity

    def encode(self):
        return MockedRegisters[(self.address, self.quantity)]


MockedRegisters = {
    # InverterEquipmentRegister.Model - 'SUN2000'
    (30000, 15): b'\x1eSUN2000\x00\x00\x00',

    # InverterEquipmentRegister.ModelID - 429
    (30070, 1): b'\x02\x01\xad',

    # InverterEquipmentRegister.RatedPower - 10000
    (30073, 2): b"\x04\x00\x00'\x10",

    # InverterEquipmentRegister.State1 - '0000000000000110'
    (32000, 1): b'\x02\x00\x06',

    # InverterEquipmentRegister.DeviceStatus - 512
    (32089, 1): b'\x02\x02\x00',

    # MeterEquipmentRegister.ActivePower - 1000
    (37113, 2): b'\x04\x03\xe8',

    # Range of Registers
    (30000, 35): b'FSUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12HV2220100135\x00\x00\x00\x00\x00\x00\x00\x0001074311-002\x00\x00\x00\x00\x00\x00\x00\x00'
}


def mock_read_holding_registers(self, address, quantity, slave):
    return MockedResponse(address, quantity)


def mock_read_holding_registers_ModbusIOException(self, address, quantity, slave):
    return ModbusIOException("Requested slave is not available")


def mock_read_holding_registers_ConnectionException(self, address, quantity, slave):
    raise ConnectionException("Connection unexpectedly closed")


def connect_success(self):
    return True


def connect_fail(self):
    return False
