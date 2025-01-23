from enum import Enum


class DataType(Enum):
    STRING = 'string'
    UINT16_BE = 'uint16'
    UINT32_BE = 'uint32'
    INT16_BE = 'int16'
    INT32_BE = 'int32'
    BITFIELD16 = 'bitfield16'
    BITFIELD32 = 'bitfield32'
    MULTIDATA = 'multidata'


def decode_string(value):
    return value.decode('utf-8', 'replace').strip('\0')


def encode_uint_be(value, length):
    return int.to_bytes(value, length=length, byteorder='big', signed=False)


def decode_uint_be(value):
    return int.from_bytes(value, byteorder='big', signed=False)


def encode_int_be(value, length):
    return int.to_bytes(value, length=length, byteorder='big', signed=True)


def decode_int_be(value):
    return int.from_bytes(value, byteorder='big', signed=True)


def decode_bitfield(value):
    return ''.join(format(byte, '08b') for byte in value)


def encode(value, data_type):
    if data_type == DataType.UINT16_BE:
        return encode_uint_be(value, 2)
    elif data_type == DataType.UINT32_BE:
        return encode_uint_be(value, 4)
    elif data_type == DataType.INT16_BE:
        return encode_int_be(value, 2)
    elif data_type == DataType.INT32_BE:
        return encode_int_be(value, 4)
    elif data_type == DataType.MULTIDATA:
        if len(value) % 2 != 0:
            raise ValueError('Multidata value length must be a multiple of 2')
        return value
    else:
        raise ValueError('Writing is not supported for register type')


def decode(value, data_type):
    if data_type == DataType.STRING:
        return decode_string(value)
    elif data_type == DataType.UINT16_BE or data_type == DataType.UINT32_BE:
        return decode_uint_be(value)
    elif data_type == DataType.INT16_BE or data_type == DataType.INT32_BE:
        return decode_int_be(value)
    elif data_type == DataType.BITFIELD16 or data_type == DataType.BITFIELD32:
        return decode_bitfield(value)
    elif data_type == DataType.MULTIDATA:
        return value
    else:
        raise ValueError('Unknown register type')
