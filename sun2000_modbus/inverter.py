import logging
import time

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException

from . import datatypes

logging.basicConfig(level=logging.INFO)


class Sun2000:
    def __init__(self, host, port=502, timeout=5, wait=2, unit=0):
        self.wait = wait
        self.connected = False
        self.unit = unit
        self.inverter = ModbusTcpClient(host, port, timeout=timeout)

    def connect(self):
        if not self.connected:
            self.connected = self.inverter.connect()
            time.sleep(self.wait)
            if self.connected:
                logging.info('Successfully connected to inverter')
            else:
                logging.error('Connection to inverter failed')

    def read_raw_value(self, register):
        if not self.connected:
            raise ValueError('Inverter is not connected')

        register_value = self.inverter.read_holding_registers(register.value.address, register.value.quantity, unit=self.unit)
        if type(register_value) == ModbusIOException:
            logging.error("Inverter unit did not respond")
            raise register_value

        return datatypes.decode(register_value.encode()[1:], register.value.data_type)

    def read(self, register):
        raw_value = self.read_raw_value(register)

        if register.value.gain is None:
            return raw_value
        else:
            return raw_value / register.value.gain

    def read_formatted(self, register):
        value = self.read(register)

        if register.value.unit is not None:
            return f'{value} {register.value.unit}'
        elif register.value.mapping is not None:
            return register.value.mapping.get(value, 'undefined')
        else:
            return value
