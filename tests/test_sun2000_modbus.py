import unittest
from unittest.mock import patch

from pymodbus.exceptions import ModbusIOException, ConnectionException

import sun2000mock
from sun2000_modbus.datatypes import encode, decode, DataType
from sun2000_modbus.inverter import Sun2000
from sun2000_modbus.registers import InverterEquipmentRegister, MeterEquipmentRegister, BatteryEquipmentRegister


class TestDataTypes(unittest.TestCase):
    def test_decode_string(self):
        value = b'SUN2000\x00\x00\x00'
        decoded = decode(value, DataType.STRING)
        self.assertEqual(decoded, 'SUN2000')

    def test_encode_uint16_be(self):
        value = 1234
        encoded = encode(value, DataType.UINT16_BE)
        self.assertEqual(encoded, b'\x04\xD2')

    def test_decode_uint16_be(self):
        value = b'\x04\xD2'
        decoded = decode(value, DataType.UINT16_BE)
        self.assertEqual(decoded, 1234)

    def test_encode_uint32_be(self):
        value = 123456789
        encoded = encode(value, DataType.UINT32_BE)
        self.assertEqual(encoded, b'\x07\x5B\xCD\x15')

    def test_decode_uint32_be(self):
        value = b'\x07\x5B\xCD\x15'
        decoded = decode(value, DataType.UINT32_BE)
        self.assertEqual(decoded, 123456789)

    def test_encode_int16_be(self):
        value = -1234
        encoded = encode(value, DataType.INT16_BE)
        self.assertEqual(encoded, b'\xFB\x2E')

    def test_decode_int16_be(self):
        value = b'\xFB\x2E'
        decoded = decode(value, DataType.INT16_BE)
        self.assertEqual(decoded, -1234)

    def test_encode_int32_be(self):
        value = -123456789
        encoded = encode(value, DataType.INT32_BE)
        self.assertEqual(encoded, b'\xF8\xA4\x32\xEB')

    def test_decode_int32_be(self):
        value = b'\xF8\xA4\x32\xEB'
        decoded = decode(value, DataType.INT32_BE)
        self.assertEqual(decoded, -123456789)

    def test_decode_bitfield16(self):
        value = b'\x3E\x22'
        decoded = decode(value, DataType.BITFIELD16)
        self.assertEqual(decoded, '0011111000100010')

    def test_decode_bitfield32(self):
        value = b'\x3E\x22\xAF\x45'
        decoded = decode(value, DataType.BITFIELD16)
        self.assertEqual(decoded, '00111110001000101010111101000101')

    def test_encode_multidata(self):
        value = b'\x3E\x22\xAF\x45'
        encoded = encode(value, DataType.MULTIDATA)
        self.assertEqual(encoded, b'\x3E\x22\xAF\x45')

    def test_decode_multidata(self):
        value = b'\x3E\x22\xAF\x45'
        decoded = decode(value, DataType.MULTIDATA)
        self.assertEqual(decoded, b'\x3E\x22\xAF\x45')

    def test_decode_invalid(self):
        value = b'\x3E'
        self.assertRaises(ValueError, decode, value, 'invalid')


class TestSun2000(unittest.TestCase):
    def setUp(self) -> None:
        self.test_inverter = Sun2000(host='192.168.8.1', port=123, timeout=3, wait=0, slave=1)

    def test_init(self):
        self.assertEqual(self.test_inverter.inverter.comm_params.host, '192.168.8.1')
        self.assertEqual(self.test_inverter.inverter.comm_params.port, 123)
        self.assertEqual(self.test_inverter.inverter.comm_params.timeout_connect, 3)
        self.assertEqual(self.test_inverter.wait, 0)
        self.assertEqual(self.test_inverter.slave, 1)
        self.assertEqual(self.test_inverter.isConnected(), False)

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_connect_success(self):
        self.test_inverter.connect()
        self.assertTrue(self.test_inverter.isConnected())

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_fail
    )
    def test_connect_fail(self):
        self.test_inverter.connect()
        self.assertFalse(self.test_inverter.isConnected())

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_fail
    )
    def test_read_raw_value_string_from_disconnected_unit(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_raw_value(InverterEquipmentRegister.Model)
        self.assertEqual(str(cm.exception), 'Inverter is not connected')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers_ModbusIOException
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_string_from_unavailable_unit(self):
        self.test_inverter.connect()
        with self.assertRaises(ModbusIOException) as cm:
            self.test_inverter.read_raw_value(InverterEquipmentRegister.Model)
        self.assertEqual(str(cm.exception), 'Modbus Error: [Input/Output] Requested slave is not available')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers_ConnectionException
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_string_connection_unexpectedly_closed(self):
        self.test_inverter.connect()
        with self.assertRaises(ConnectionException) as cm:
            self.test_inverter.read_raw_value(InverterEquipmentRegister.Model)
        self.assertEqual(str(cm.exception), 'Modbus Error: [Connection] Connection unexpectedly closed')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_without_slave_argument_takes_default(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read_raw_value(InverterEquipmentRegister.Model)
        mock_read_holding_registers.assert_called_once_with(address=30000, count=15, slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_with_slave_argument(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read_raw_value(InverterEquipmentRegister.Model, slave=123)
        mock_read_holding_registers.assert_called_once_with(address=30000, count=15, slave=123)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_string(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_raw_value(InverterEquipmentRegister.Model)
        self.assertEqual(result, 'SUN2000')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_uint16be(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_raw_value(InverterEquipmentRegister.ModelID)
        self.assertEqual(result, 429)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_uint32be(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_raw_value(InverterEquipmentRegister.RatedPower)
        self.assertEqual(result, 10000)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_without_slave_argument_takes_default(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read(InverterEquipmentRegister.RatedPower)
        mock_read_holding_registers.assert_called_once_with(address=30073, count=2, slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_with_slave_argument(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read(InverterEquipmentRegister.RatedPower, slave=123)
        mock_read_holding_registers.assert_called_once_with(address=30073, count=2, slave=123)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_uint32be(self):
        self.test_inverter.connect()
        result = self.test_inverter.read(InverterEquipmentRegister.RatedPower)
        self.assertEqual(result, 10000.0)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_formatted_without_slave_argument_takes_default(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read_formatted(InverterEquipmentRegister.RatedPower)
        mock_read_holding_registers.assert_called_once_with(address=30073, count=2, slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_formatted_with_slave_argument(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read_formatted(InverterEquipmentRegister.RatedPower, slave=123)
        mock_read_holding_registers.assert_called_once_with(address=30073, count=2, slave=123)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_formatted_uint32be(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_formatted(InverterEquipmentRegister.RatedPower)
        self.assertEqual(result, '10000.0 W')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_bitfield16(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_raw_value(InverterEquipmentRegister.State1)
        self.assertEqual(result, '0000000000000110')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_bitfield16(self):
        self.test_inverter.connect()
        result = self.test_inverter.read(InverterEquipmentRegister.State1)
        self.assertEqual(result, '0000000000000110')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_formatted_bitfield16(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_formatted(InverterEquipmentRegister.State1)
        self.assertEqual(result, '0000000000000110')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_raw_value_with_mapping(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_raw_value(InverterEquipmentRegister.DeviceStatus)
        self.assertEqual(result, 512)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_formatted_with_mapping(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_formatted(InverterEquipmentRegister.DeviceStatus)
        self.assertEqual(result, 'On-grid')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_returns_float(self):
        self.test_inverter.connect()
        result = self.test_inverter.read(MeterEquipmentRegister.ActivePower)
        self.assertEqual(result, 1000.0)
        self.assertTrue(isinstance(result, float))

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_range_without_slave_argument_takes_default(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read_range(30000, quantity=35)
        mock_read_holding_registers.assert_called_once_with(address=30000, count=35, slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_range_with_slave_argument(self, mock_read_holding_registers):
        self.test_inverter.connect()
        self.test_inverter.read_range(30000, quantity=35, slave=123)
        mock_read_holding_registers.assert_called_once_with(address=30000, count=35, slave=123)

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_range_returns_range_of_register_values(self):
        self.test_inverter.connect()
        result = self.test_inverter.read_range(30000, quantity=35)
        self.assertEqual(result, b'SUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12HV2220100135\x00\x00\x00\x00\x00\x00\x00\x0001074311-002\x00\x00\x00\x00\x00\x00\x00\x00')

        result = self.test_inverter.read_range(30000, end_address=30034)
        self.assertEqual(result, b'SUN2000-10KTL-M1\x00\x00\x00\x00SUN2000-12HV2220100135\x00\x00\x00\x00\x00\x00\x00\x0001074311-002\x00\x00\x00\x00\x00\x00\x00\x00')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    def test_read_range_with_no_right_border(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_range(30000)
        self.assertEqual(str(cm.exception), 'Either parameter quantity or end_address is required and must be greater than 0')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    def test_read_range_with_both_quantity_and_end_address_defined(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_range(30000, quantity=35, end_address=30034)
        self.assertEqual(str(cm.exception), 'Only one parameter quantity or end_address should be defined')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    def test_read_range_with_quantity_set_to_0(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_range(30000, quantity=0)
        self.assertEqual(str(cm.exception), 'Either parameter quantity or end_address is required and must be greater than 0')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    def test_read_range_with_end_address_not_being_greater_than_start_address(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_range(30000, end_address=30000)
        self.assertEqual(str(cm.exception), 'end_address must be greater than start_address')

        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_range(30000, end_address=29999)
        self.assertEqual(str(cm.exception), 'end_address must be greater than start_address')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_fail
    )
    def test_read_range_from_disconnected_unit(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.read_range(30000, quantity=35)
        self.assertEqual(str(cm.exception), 'Inverter is not connected')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers_ConnectionException
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_range_from_unavailable_unit(self):
        self.test_inverter.connect()
        with self.assertRaises(ConnectionException) as cm:
            self.test_inverter.read_range(30000, quantity=35)
        self.assertEqual(str(cm.exception), 'Modbus Error: [Connection] Connection unexpectedly closed')

    @patch(
        'pymodbus.client.ModbusTcpClient.read_holding_registers', sun2000mock.mock_read_holding_registers_ModbusIOException
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_read_range_from_unavailable_unit2(self):
        self.test_inverter.connect()
        with self.assertRaises(ModbusIOException) as cm:
            self.test_inverter.read_range(30000, quantity=35)
        self.assertEqual(str(cm.exception), 'Modbus Error: [Input/Output] Requested slave is not available')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_fail
    )
    def test_write_to_disconnected_unit(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.write(BatteryEquipmentRegister.BackupPowerSOC, 10)
        self.assertEqual(str(cm.exception), 'Inverter is not connected')

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers', sun2000mock.mock_write_registers_ModbusIOException
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_to_unavailable_unit(self):
        self.test_inverter.connect()
        with self.assertRaises(ModbusIOException) as cm:
            self.test_inverter.write(BatteryEquipmentRegister.BackupPowerSOC, 10)
        self.assertEqual(str(cm.exception), 'Modbus Error: [Input/Output] Requested slave is not available')

    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_to_read_only_register(self):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.write(BatteryEquipmentRegister.RunningStatus, 1)
        self.assertEqual(str(cm.exception), 'Register is not writeable')

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers', sun2000mock.mock_write_registers_ConnectionException
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_uint16be_connection_unexpectedly_closed(self):
        self.test_inverter.connect()
        with self.assertRaises(ConnectionException) as cm:
            self.test_inverter.write(BatteryEquipmentRegister.BackupPowerSOC, 10)
        self.assertEqual(str(cm.exception), 'Modbus Error: [Connection] Connection unexpectedly closed')

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_without_slave_argument_takes_default(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(BatteryEquipmentRegister.BackupPowerSOC, 10)
        write_registers_mock.assert_called_once_with(address=47102, values=[10], slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_with_slave_argument(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(BatteryEquipmentRegister.BackupPowerSOC, 10, slave=123)
        write_registers_mock.assert_called_once_with(address=47102, values=[10], slave=123)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_uint16be(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(BatteryEquipmentRegister.BackupPowerSOC, 10)
        write_registers_mock.assert_called_once_with(address=47102, values=[10], slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_uint32be(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(InverterEquipmentRegister.FixedActivePowerDeratedInW, 10200)
        write_registers_mock.assert_called_once_with(address=40126, values=[0, 10200], slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_int16be(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(BatteryEquipmentRegister.MaximumFeedGridPowerInPercentage, -90)
        write_registers_mock.assert_called_once_with(address=47418, values=[65446], slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_int32be(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(BatteryEquipmentRegister.MaximumChargeFromGridPower, -10200)
        write_registers_mock.assert_called_once_with(address=47590, values=[65535, 55336], slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_multidata(self, write_registers_mock):
        self.test_inverter.connect()
        self.test_inverter.write(InverterEquipmentRegister.CosPhiPPnCharacteristicCurve, b'\x01\x02\x03\x04')
        write_registers_mock.assert_called_once_with(address=40133, values=[258, 772], slave=1)

    @patch(
        'pymodbus.client.ModbusTcpClient.write_registers'
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.connect', sun2000mock.connect_success
    )
    @patch(
        'pymodbus.client.ModbusTcpClient.is_socket_open', sun2000mock.connect_success
    )
    def test_write_multidata_invalid(self, write_registers_mock):
        self.test_inverter.connect()
        with self.assertRaises(ValueError) as cm:
            self.test_inverter.write(InverterEquipmentRegister.CosPhiPPnCharacteristicCurve, b'\x01\x02\x03')
        self.assertEqual(str(cm.exception), 'Multidata value length must be a multiple of 2')
