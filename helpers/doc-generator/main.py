from sun2000_modbus.datatypes import DataType
from sun2000_modbus.registers import InverterEquipmentRegister, BatteryEquipmentRegister, MeterEquipmentRegister


datatype_mapping = {
    DataType.STRING: 'String',
    DataType.UINT16_BE: 'Number',
    DataType.UINT32_BE: 'Number',
    DataType.INT16_BE: 'Number',
    DataType.INT32_BE: 'Number',
    DataType.BITFIELD16: 'Binary String/Bitfield',
    DataType.BITFIELD32: 'Binary String/Bitfield',
    DataType.MULTIDATA: 'Bytestring',
}


def omit_none(gain) -> str:
    if gain:
        return gain
    return ''

def process_register(register, filename) -> None:
    with open(f'output/{filename}', 'w') as inverter_docs:
        inverter_docs.write('| Name | Type | Gain | Unit | Access Type |\n')
        inverter_docs.write('| :- | :- | :- | :- | :- |\n')
        for item in register:
            inverter_docs.write(f'| {item.name} | {datatype_mapping[item.value.data_type]} | {omit_none(item.value.gain)} | {omit_none(item.value.unit)} | {item.value.access_type.name} |\n')

def main() -> None:
    process_register(InverterEquipmentRegister, 'inverter.md')
    process_register(BatteryEquipmentRegister, 'battery.md')
    process_register(MeterEquipmentRegister, 'meter.md')

if __name__ == "__main__":
    main()
