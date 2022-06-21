import logging
import time

from pymodbus.client.sync import ModbusTcpClient

from sun2000_modbus.datatypes import decode
from sun2000_modbus.registers import InverterEquipmentRegister

logging.basicConfig(level=logging.INFO)


class Sun2000:
    def __init__(self, host, port=502, timeout=5, wait=2, slave=0):
        self.wait = wait
        self.connected = False
        self.inverter = ModbusTcpClient(host, port, timeout=timeout, unit_id=slave)

    def connect(self):
        if not self.connected:
            self.connected = self.inverter.connect()
            time.sleep(self.wait)
            if self.connected:
                logging.info("Successfully connected to inverter")
            else:
                logging.error("Connection to inverter failed")

    def read_raw_value(self, register):
        register_value = self.inverter.read_holding_registers(register.value.address, register.value.quantity)

        return decode(register_value.encode()[1:], register.value.data_type)

    def read(self, register):
        raw_value = self.read_raw_value(register)

        if register.value.gain == 1:
            return raw_value
        else:
            return raw_value / register.value.gain

    def read_formatted(self, register):
        value = self.read(register)

        if register.value.unit is not None:
            return f'{value} {register.value.unit}'
        else:
            return value


#### Testing
inv = Sun2000("192.168.200.1", 6607, slave=1)
inv.connect()
# for register in InverterEquipmentRegister:
#     print(f'{register.name}: {inv.read_formatted(register)}')
# for register in BatteryEquipmentRegister:
#     print(f'{register.name}: {inv.read_formatted(register)}')
# for register in MeterEquipmentRegister:
#     print(f'{register.name}: {inv.read_formatted(register)}')
print(f'MaximumReactivePowerAbsorbedFromTheGrid: {inv.read_formatted(InverterEquipmentRegister.State1)}')
