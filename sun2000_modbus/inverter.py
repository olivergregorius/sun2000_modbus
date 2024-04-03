import logging
import time

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException, ConnectionException

from . import datatypes

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_format = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(log_format)
logger.addHandler(handler)


class Sun2000:
    def __init__(self, host, port=502, timeout=5, wait=2, unit=0): # some models need unit=1
        self.wait = wait
        self.unit = unit
        self.inverter = ModbusTcpClient(host, port, timeout=timeout)

    def connect(self):
        if not self.isConnected():
            self.inverter.connect()
            time.sleep(self.wait)
            if self.isConnected():
                logger.info('Successfully connected to inverter')
                return True
            else:
                logger.error('Connection to inverter failed')
                return False

    def disconnect(self):
        """Close the underlying tcp socket"""
        # Some Sun2000 models with the SDongle WLAN-FE require the TCP connection to be closed
        # as soon as possible. Leaving the TCP connection open for an extended time may cause 
        # dongle reboots and/or FusionSolar portal updates to be delayed or even paused. 
        self.inverter.close()

    def isConnected(self):
        """Check if underlying tcp socket is open"""
        return self.inverter.is_socket_open()

    @property
    def connected(self):
        return self.isConnected()

    def read_raw_value(self, register):
        if not self.isConnected():
            raise ValueError('Inverter is not connected')

        try:
            register_value = self.inverter.read_holding_registers(register.value.address, register.value.quantity, unit=self.unit)
            if type(register_value) == ModbusIOException:
                logger.error("Inverter unit did not respond")
                raise register_value
        except ConnectionException:
            logger.error("A connection error occurred")
            raise

        return datatypes.decode(register_value.encode()[1:], register.value.data_type)

    def read(self, register):
        raw_value = self.read_raw_value(register)

        if register.value.gain is None:
            return raw_value
        else:
            return raw_value / register.value.gain

    def read_formatted(self, register, use_locale=False):
        value = self.read(register)

        if register.value.unit is not None:
            if use_locale:
                return f'{value:n} {register.value.unit}'
            else:
                return f'{value} {register.value.unit}'
        elif register.value.mapping is not None:
            return register.value.mapping.get(value, 'undefined')
        else:
            return value

    def read_range(self, start_address, quantity=0, end_address=0):
        if quantity == 0 and end_address == 0:
            raise ValueError("Either parameter quantity or end_address is required and must be greater than 0")
        if quantity != 0 and end_address != 0:
            raise ValueError("Only one parameter quantity or end_address should be defined")
        if end_address != 0 and end_address <= start_address:
            raise ValueError("end_address must be greater than start_address")

        if not self.isConnected():
            raise ValueError('Inverter is not connected')

        if end_address != 0:
            quantity = end_address - start_address + 1
        try:
            register_range_value = self.inverter.read_holding_registers(start_address, quantity, unit=self.unit)
            if type(register_range_value) == ModbusIOException:
                logger.error("Inverter unit did not respond")
                raise register_range_value
        except ConnectionException:
            logger.error("A connection error occurred")
            raise

        return datatypes.decode(register_range_value.encode()[1:], datatypes.DataType.MULTIDATA)
