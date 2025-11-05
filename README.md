# sun2000_modbus

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/olivergregorius/sun2000_modbus/build.yml?branch=main&label=Python%20Build&logo=github)](https://github.com/olivergregorius/sun2000_modbus/actions/workflows/build.yml)
[![Python Versions](https://img.shields.io/pypi/pyversions/sun2000_modbus?label=Python)](https://pypi.org/project/sun2000_modbus/)
[![GitHub](https://img.shields.io/github/license/olivergregorius/sun2000_modbus?label=License)](https://github.com/olivergregorius/sun2000_modbus/blob/HEAD/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/sun2000_modbus?label=PyPI)](https://pypi.org/project/sun2000_modbus/)

## Introduction

This library is intended for reading Huawei Sun2000 inverter metrics from registers via Modbus TCP. Access to the Modbus interface is established by connecting
to the device's internal Wifi access point. For information about how to connect to this internal AP consult the official documentation of the device.

## Requirements

- Python >= 3.9

## Disclaimer

By using the content in this repository, you acknowledge that you do so at your own risk. I am not liable for any damages or issues that may arise from use of
this library.

## Usage

sun2000_modbus provides easy and comfortable access to your inverter's Modbus TCP interface. The following example gives a short introduction about how to read
a register:

```python
from sun2000_modbus import inverter
from sun2000_modbus import registers

inverter = inverter.Sun2000(host='192.168.8.1')
inverter.connect()
if inverter.isConnected():
    input_power = inverter.read_formatted(registers.InverterEquipmentRegister.InputPower)
    print(input_power)
```

The above code snippet prints out the current input power value, e.g. `8.342 kW`.

### Connection configuration

During instantiation of a Sun2000 object the following parameters are accepted:

| Parameter | Description                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| host      | IP address                                                                                                                                     |
| port      | Port, usually 502, changed to 6607 on newer firmware versions.                                                                                 |
| timeout   | Connection timeout                                                                                                                             |
| wait      | Time to wait after connection before a register read can be performed. Increases stability.                                                    |
| slave     | Number of inverter unit to be read by default, used in cascading scenarios. Defaults to 0, but some devices need it to be set to other values. |

### Read metrics

Several methods are provided to return the read register values in different formats:

| Method         | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| read_raw_value | Returns the raw value converted to its readable form                                            |
| read           | Returns the postprocessed value, e.g. a float value is calculated according to its defined gain |
| read_formatted | Returns the postprocessed value suffixed with its unit, if defined                              |

Looking at the [above example](#usage) the different methods would return the following values for the input power metric:

| Method         | Returned value |
|----------------|----------------|
| read_raw_value | 8342           |
| read           | 8.342          |
| read_formatted | 8.342 kW       |

Furthermore, a method `read_range` exists accepting the address of the register to start reading and either a quantity of registers or the address of the last
register to be read. The result is returned as byte-string for further processing.

Each `read*` method accepts a `slave` argument which is used in cascading scenarios to address the desired inverter unit.

### Write settings

For writing a register the `write` method can be used, taking the register address and the value as arguments.

Furthermore, the `write` method accepts a `slave` argument which is used in cascading scenarios to address the desired inverter unit.

## Registers

The following registers are provided by the Sun2000's Modbus interface and can be read accordingly. Documentation can be found
[here](https://javierin.com/wp-content/uploads/sites/2/2021/09/Solar-Inverter-Modbus-Interface-Definitions.pdf).

### InverterEquipmentRegister

| Name                                    | Type                   | Gain | Unit | Access Type |
|-----------------------------------------|------------------------|------|------|-------------|
| Model                                   | String                 |      |      | RO          |
| SN                                      | String                 |      |      | RO          |
| PN                                      | String                 |      |      | RO          |
| FirmwareVerion                          | String                 |      |      | RO          |
| SoftwareVerion                          | String                 |      |      | RO          |
| ProtocolVerion                          | String                 |      |      | RO          |
| ModelID                                 | Number                 | 1    |      | RO          |
| NumberOfPVStrings                       | Number                 | 1    |      | RO          |
| NumberOfMPPTrackers                     | Number                 | 1    |      | RO          |
| RatedPower                              | Number                 | 1    | W    | RO          |
| MaximumActivePower                      | Number                 | 1    | W    | RO          |
| MaximumApparentPower                    | Number                 | 1000 | kVA  | RO          |
| MaximumReactivePowerFedToTheGrid        | Number                 | 1000 | kvar | RO          |
| MaximumReactivePowerAbsorbedFromTheGrid | Number                 | 1000 | kvar | RO          |
| State1                                  | Binary String/Bitfield |      |      | RO          |
| State2                                  | Binary String/Bitfield |      |      | RO          |
| State3                                  | Binary String/Bitfield |      |      | RO          |
| Alarm1                                  | Binary String/Bitfield |      |      | RO          |
| Alarm2                                  | Binary String/Bitfield |      |      | RO          |
| Alarm3                                  | Binary String/Bitfield |      |      | RO          |
| PV1Voltage                              | Number                 | 10   | V    | RO          |
| PV1Current                              | Number                 | 100  | A    | RO          |
| PV2Voltage                              | Number                 | 10   | V    | RO          |
| PV2Current                              | Number                 | 100  | A    | RO          |
| PV3Voltage                              | Number                 | 10   | V    | RO          |
| PV3Current                              | Number                 | 100  | A    | RO          |
| PV4Voltage                              | Number                 | 10   | V    | RO          |
| PV4Current                              | Number                 | 100  | A    | RO          |
| PV5Voltage                              | Number                 | 10   | V    | RO          |
| PV5Current                              | Number                 | 100  | A    | RO          |
| PV6Voltage                              | Number                 | 10   | V    | RO          |
| PV6Current                              | Number                 | 100  | A    | RO          |
| PV7Voltage                              | Number                 | 10   | V    | RO          |
| PV7Current                              | Number                 | 100  | A    | RO          |
| PV8Voltage                              | Number                 | 10   | V    | RO          |
| PV8Current                              | Number                 | 100  | A    | RO          |
| PV9Voltage                              | Number                 | 10   | V    | RO          |
| PV9Current                              | Number                 | 100  | A    | RO          |
| PV10Voltage                             | Number                 | 10   | V    | RO          |
| PV10Current                             | Number                 | 100  | A    | RO          |
| PV11Voltage                             | Number                 | 10   | V    | RO          |
| PV11Current                             | Number                 | 100  | A    | RO          |
| PV12Voltage                             | Number                 | 10   | V    | RO          |
| PV12Current                             | Number                 | 100  | A    | RO          |
| PV13Voltage                             | Number                 | 10   | V    | RO          |
| PV13Current                             | Number                 | 100  | A    | RO          |
| PV14Voltage                             | Number                 | 10   | V    | RO          |
| PV14Current                             | Number                 | 100  | A    | RO          |
| PV15Voltage                             | Number                 | 10   | V    | RO          |
| PV15Current                             | Number                 | 100  | A    | RO          |
| PV16Voltage                             | Number                 | 10   | V    | RO          |
| PV16Current                             | Number                 | 100  | A    | RO          |
| PV17Voltage                             | Number                 | 10   | V    | RO          |
| PV17Current                             | Number                 | 100  | A    | RO          |
| PV18Voltage                             | Number                 | 10   | V    | RO          |
| PV18Current                             | Number                 | 100  | A    | RO          |
| PV19Voltage                             | Number                 | 10   | V    | RO          |
| PV19Current                             | Number                 | 100  | A    | RO          |
| PV20Voltage                             | Number                 | 10   | V    | RO          |
| PV20Current                             | Number                 | 100  | A    | RO          |
| PV21Voltage                             | Number                 | 10   | V    | RO          |
| PV21Current                             | Number                 | 100  | A    | RO          |
| PV22Voltage                             | Number                 | 10   | V    | RO          |
| PV22Current                             | Number                 | 100  | A    | RO          |
| PV23Voltage                             | Number                 | 10   | V    | RO          |
| PV23Current                             | Number                 | 100  | A    | RO          |
| PV24Voltage                             | Number                 | 10   | V    | RO          |
| PV24Current                             | Number                 | 100  | A    | RO          |
| InputPower                              | Number                 | 1    | W    | RO          |
| LineVoltageBetweenPhasesAAndB           | Number                 | 10   | V    | RO          |
| LineVoltageBetweenPhasesBAndC           | Number                 | 10   | V    | RO          |
| LineVoltageBetweenPhasesCAndA           | Number                 | 10   | V    | RO          |
| PhaseAVoltage                           | Number                 | 10   | V    | RO          |
| PhaseBVoltage                           | Number                 | 10   | V    | RO          |
| PhaseCVoltage                           | Number                 | 10   | V    | RO          |
| PhaseACurrent                           | Number                 | 1000 | A    | RO          |
| PhaseBCurrent                           | Number                 | 1000 | A    | RO          |
| PhaseCCurrent                           | Number                 | 1000 | A    | RO          |
| PeakActivePowerOfCurrentDay             | Number                 | 1    | W    | RO          |
| ActivePower                             | Number                 | 1    | W    | RO          |
| ReactivePower                           | Number                 | 1000 | kvar | RO          |
| PowerFactor                             | Number                 | 1000 |      | RO          |
| GridFrequency                           | Number                 | 100  | Hz   | RO          |
| Efficiency                              | Number                 | 100  | %    | RO          |
| InternalTemperature                     | Number                 | 10   | °C   | RO          |
| InsulationResistance                    | Number                 | 1000 | MOhm | RO          |
| DeviceStatus                            | Number                 | 1    |      | RO          |
| FaultCode                               | Number                 | 1    |      | RO          |
| StartupTime                             | Number                 | 1    |      | RO          |
| ShutdownTime                            | Number                 | 1    |      | RO          |
| AccumulatedEnergyYield                  | Number                 | 100  | kWh  | RO          |
| DailyEnergyYield                        | Number                 | 100  | kWh  | RO          |
| ActiveAdjustmentMode                    | Number                 | 1    |      | RO          |
| ActiveAdjustmentValue                   | Number                 | 1    |      | RO          |
| ActiveAdjustmentCommand                 | Number                 | 1    |      | RO          |
| ReactiveAdjustmentMode                  | Number                 | 1    |      | RO          |
| ReactiveAdjustmentValue                 | Number                 | 1    |      | RO          |
| ReactiveAdjustmentCommand               | Number                 | 1    |      | RO          |
| PowerMeterCollectionActivePower         | Number                 | 1    | W    | RO          |
| TotalNumberOfOptimizers                 | Number                 | 1    |      | RO          |
| NumberOfOnlineOptimizers                | Number                 | 1    |      | RO          |
| FeatureData                             | Number                 | 1    |      | RO          |
| SystemTime                              | Number                 | 1    |      | RW          |
| QUCharacteristicCurveMode               | Number                 | 1    |      | RW          |
| QUDispatchTriggerPower                  | Number                 | 1    | %    | RW          |
| FixedActivePowerDeratedInKW             | Number                 | 10   | kW   | RW          |
| ReactivePowerCompensationInPF           | Number                 | 1000 |      | RW          |
| ReactivePowerCompensationQS             | Number                 | 1000 |      | RW          |
| ActivePowerPercentageDerating           | Number                 | 10   | %    | RW          |
| FixedActivePowerDeratedInW              | Number                 | 1    | W    | RW          |
| ReactivePowerCompensationAtNight        | Number                 | 1000 | kvar | RW          |
| CosPhiPPnCharacteristicCurve            | Bytestring             |      |      | RW          |
| QUCharacteristicCurve                   | Bytestring             |      |      | RW          |
| PFUCharacteristicCurve                  | Bytestring             |      |      | RW          |
| ReactivePowerAdjustmentTime             | Number                 | 1    | s    | RW          |
| QUPowerPercentageToExitScheduling       | Number                 | 1    | %    | RW          |
| Startup                                 | Number                 | 1    |      | WO          |
| Shutdown                                | Number                 | 1    |      | WO          |
| GridCode                                | Number                 | 1    |      | RW          |
| ReactivePowerChangeGradient             | Number                 | 1000 | %/s  | RW          |
| ActivePowerChangeGradient               | Number                 | 1000 | %/s  | RW          |
| ScheduleInstructionValidDuration        | Number                 | 1    | s    | RW          |
| TimeZone                                | Number                 | 1    | min  | RW          |

### BatteryEquipmentRegister

| Name                                   | Type       | Gain | Unit    | Access Type |
|----------------------------------------|------------|------|---------|-------------|
| RunningStatus                          | Number     | 1    |         | RO          |
| WorkingModeSettings                    | Number     | 1    |         | RW          |
| BusVoltage                             | Number     | 10   | V       | RO          |
| BusCurrent                             | Number     | 10   | A       | RO          |
| ChargeDischargePower                   | Number     | 1    | W       | RO          |
| MaximumChargePower                     | Number     | 1    | W       | RO          |
| MaximumDischargePower                  | Number     | 1    | W       | RO          |
| RatedCapacity                          | Number     | 1    | Wh      | RO          |
| SOC                                    | Number     | 10   | %       | RO          |
| BackupPowerSOC                         | Number     | 10   | %       | RW          |
| TotalCharge                            | Number     | 100  | kWh     | RO          |
| TotalDischarge                         | Number     | 100  | kWh     | RO          |
| CurrentDayChargeCapacity               | Number     | 100  | kWh     | RO          |
| CurrentDayDischargeCapacity            | Number     | 100  | kWh     | RO          |
| TimeOfUseElectricityPricePeriods       | Bytestring |      |         | RW          |
| MaximumChargingPower                   | Number     | 1    | W       | RW          |
| MaximumDischargingPower                | Number     | 1    | W       | RW          |
| ChargingCutoffCapacity                 | Number     | 10   | %       | RW          |
| DischargeCutoffCapacity                | Number     | 10   | %       | RW          |
| ForcedChargingAndDischargingPeriod     | Number     | 1    | minutes | RW          |
| ChargeFromGridFunction                 | Number     | 1    |         | RW          |
| GridChargeCutoffSOC                    | Number     | 10   | %       | RW          |
| ForcibleChargeDischarge                | Number     | 1    |         | WO          |
| FixedChargingAndDischargingPeriods     | Bytestring |      |         | RW          |
| PowerOfChargeFromGrid                  | Number     | 0.1  | W       | RW          |
| MaximumPowerOfChargeFromGrid           | Number     | 0.1  | W       | RW          |
| ForcibleChargeDischargeSettingMode     | Number     | 1    |         | RW          |
| ForcibleChargePower                    | Number     | 0.1  | W       | RW          |
| ForcibleDischargePower                 | Number     | 0.1  | W       | RW          |
| TimeOfUseChargingAndDischargingPeriods | Bytestring |      |         | RW          |
| ExcessPVEnergyUseInTOU                 | Number     | 1    |         | RW          |
| ActivePowerControlMode                 | Number     | 1    |         | RW          |
| MaximumFeedGridPowerInKW               | Number     | 1000 | kW      | RW          |
| MaximumFeedGridPowerInPercentage       | Number     | 10   | %       | RW          |
| MaximumChargeFromGridPower             | Number     | 0.1  | W       | RW          |
| SwitchToOffGrid                        | Number     | 1    |         | RW          |
| VoltageInIndependentOperation          | Number     | 1    |         | RW          |
| Unit1ProductModel                      | Number     | 1    |         | RW          |
| Unit1SN                                | String     |      |         | RO          |
| Unit1No                                | Number     | 1    |         | RW          |
| Unit1SoftwareVersion                   | String     |      |         | RO          |
| Unit1DCDCVersion                       | String     |      |         | RO          |
| Unit1BMSVersion                        | String     |      |         | RO          |
| Unit1RunningStatus                     | Number     | 1    |         | RO          |
| Unit1WorkingMode                       | Number     | 1    |         | RO          |
| Unit1BusVoltage                        | Number     | 10   | V       | RO          |
| Unit1BusCurrent                        | Number     | 10   | A       | RO          |
| Unit1BatterySOC                        | Number     | 10   | %       | RO          |
| Unit1ChargeAndDischargePower           | Number     | 1    | W       | RO          |
| Unit1RemainingChargeDischargeTime      | Number     | 1    | minutes | RO          |
| Unit1RatedChargePower                  | Number     | 1    | W       | RO          |
| Unit1RatedDischargePower               | Number     | 1    | W       | RO          |
| Unit1CurrentDayChargeCapacity          | Number     | 100  | kWh     | RO          |
| Unit1CurrentDayDischargeCapacity       | Number     | 100  | kWh     | RO          |
| Unit1TotalCharge                       | Number     | 100  | kWh     | RO          |
| Unit1TotalDischarge                    | Number     | 100  | kWh     | RO          |
| Unit1BatteryTemperature                | Number     | 10   | °C      | RO          |
| Unit1FaultID                           | Number     | 1    |         | RO          |
| Unit2ProductModel                      | Number     | 1    |         | RW          |
| Unit2SN                                | String     |      |         | RO          |
| Unit2No                                | Number     | 1    |         | RW          |
| Unit2SoftwareVersion                   | String     |      |         | RO          |
| Unit2RunningStatus                     | Number     | 1    |         | RO          |
| Unit2BusVoltage                        | Number     | 10   | V       | RO          |
| Unit2BusCurrent                        | Number     | 10   | A       | RO          |
| Unit2BatterySOC                        | Number     | 10   | %       | RO          |
| Unit2ChargeAndDischargePower           | Number     | 1    | W       | RO          |
| Unit2CurrentDayChargeCapacity          | Number     | 100  | kWh     | RO          |
| Unit2CurrentDayDischargeCapacity       | Number     | 100  | kWh     | RO          |
| Unit2TotalCharge                       | Number     | 100  | kWh     | RO          |
| Unit2TotalDischarge                    | Number     | 100  | kWh     | RO          |
| Unit2BatteryTemperature                | Number     | 10   | °C      | RO          |
| Unit1BatteryPack1SN                    | String     |      |         | RO          |
| Unit1BatteryPack1No                    | Number     | 1    |         | RW          |
| Unit1BatteryPack1FirmwareVersion       | String     |      |         | RO          |
| Unit1BatteryPack1WorkingStatus         | Number     | 1    |         | RO          |
| Unit1BatteryPack1Voltage               | Number     | 10   | V       | RO          |
| Unit1BatteryPack1Current               | Number     | 10   | A       | RO          |
| Unit1BatteryPack1SOC                   | Number     | 10   | %       | RO          |
| Unit1BatteryPack1ChargeDischargePower  | Number     | 1    | W       | RO          |
| Unit1BatteryPack1TotalCharge           | Number     | 100  | kWh     | RO          |
| Unit1BatteryPack1TotalDischarge        | Number     | 100  | kWh     | RO          |
| Unit1BatteryPack1MinimumTemperature    | Number     | 10   | °C      | RO          |
| Unit1BatteryPack1MaximumTemperature    | Number     | 10   | °C      | RO          |
| Unit1BatteryPack2SN                    | String     |      |         | RO          |
| Unit1BatteryPack2No                    | Number     | 1    |         | RW          |
| Unit1BatteryPack2FirmwareVersion       | String     |      |         | RO          |
| Unit1BatteryPack2WorkingStatus         | Number     | 1    |         | RO          |
| Unit1BatteryPack2Voltage               | Number     | 10   | V       | RO          |
| Unit1BatteryPack2Current               | Number     | 10   | A       | RO          |
| Unit1BatteryPack2SOC                   | Number     | 10   | %       | RO          |
| Unit1BatteryPack2ChargeDischargePower  | Number     | 1    | W       | RO          |
| Unit1BatteryPack2TotalCharge           | Number     | 100  | kWh     | RO          |
| Unit1BatteryPack2TotalDischarge        | Number     | 100  | kWh     | RO          |
| Unit1BatteryPack2MinimumTemperature    | Number     | 10   | °C      | RO          |
| Unit1BatteryPack2MaximumTemperature    | Number     | 10   | °C      | RO          |
| Unit1BatteryPack3SN                    | String     |      |         | RO          |
| Unit1BatteryPack3No                    | Number     | 1    |         | RW          |
| Unit1BatteryPack3FirmwareVersion       | String     |      |         | RO          |
| Unit1BatteryPack3WorkingStatus         | Number     | 1    |         | RO          |
| Unit1BatteryPack3Voltage               | Number     | 10   | V       | RO          |
| Unit1BatteryPack3Current               | Number     | 10   | A       | RO          |
| Unit1BatteryPack3SOC                   | Number     | 10   | %       | RO          |
| Unit1BatteryPack3ChargeDischargePower  | Number     | 1    | W       | RO          |
| Unit1BatteryPack3TotalCharge           | Number     | 100  | kWh     | RO          |
| Unit1BatteryPack3TotalDischarge        | Number     | 100  | kWh     | RO          |
| Unit1BatteryPack3MinimumTemperature    | Number     | 10   | °C      | RO          |
| Unit1BatteryPack3MaximumTemperature    | Number     | 10   | °C      | RO          |
| Unit2BatteryPack1SN                    | String     |      |         | RO          |
| Unit2BatteryPack1No                    | Number     | 1    |         | RW          |
| Unit2BatteryPack1FirmwareVersion       | String     |      |         | RO          |
| Unit2BatteryPack1WorkingStatus         | Number     | 1    |         | RO          |
| Unit2BatteryPack1Voltage               | Number     | 10   | V       | RO          |
| Unit2BatteryPack1Current               | Number     | 10   | A       | RO          |
| Unit2BatteryPack1SOC                   | Number     | 10   | %       | RO          |
| Unit2BatteryPack1ChargeDischargePower  | Number     | 1    | W       | RO          |
| Unit2BatteryPack1TotalCharge           | Number     | 100  | kWh     | RO          |
| Unit2BatteryPack1TotalDischarge        | Number     | 100  | kWh     | RO          |
| Unit2BatteryPack1MinimumTemperature    | Number     | 10   | °C      | RO          |
| Unit2BatteryPack1MaximumTemperature    | Number     | 10   | °C      | RO          |
| Unit2BatteryPack2SN                    | String     |      |         | RO          |
| Unit2BatteryPack2No                    | Number     | 1    |         | RW          |
| Unit2BatteryPack2FirmwareVersion       | String     |      |         | RO          |
| Unit2BatteryPack2WorkingStatus         | Number     | 1    |         | RO          |
| Unit2BatteryPack2Voltage               | Number     | 10   | V       | RO          |
| Unit2BatteryPack2Current               | Number     | 10   | A       | RO          |
| Unit2BatteryPack2SOC                   | Number     | 10   | %       | RO          |
| Unit2BatteryPack2ChargeDischargePower  | Number     | 1    | W       | RO          |
| Unit2BatteryPack2TotalCharge           | Number     | 100  | kWh     | RO          |
| Unit2BatteryPack2TotalDischarge        | Number     | 100  | kWh     | RO          |
| Unit2BatteryPack2MinimumTemperature    | Number     | 10   | °C      | RO          |
| Unit2BatteryPack2MaximumTemperature    | Number     | 10   | °C      | RO          |
| Unit2BatteryPack3SN                    | String     |      |         | RO          |
| Unit2BatteryPack3No                    | Number     | 1    |         | RW          |
| Unit2BatteryPack3FirmwareVersion       | String     |      |         | RO          |
| Unit2BatteryPack3WorkingStatus         | Number     | 1    |         | RO          |
| Unit2BatteryPack3Voltage               | Number     | 10   | V       | RO          |
| Unit2BatteryPack3Current               | Number     | 10   | A       | RO          |
| Unit2BatteryPack3SOC                   | Number     | 10   | %       | RO          |
| Unit2BatteryPack3ChargeDischargePower  | Number     | 1    | W       | RO          |
| Unit2BatteryPack3TotalCharge           | Number     | 100  | kWh     | RO          |
| Unit2BatteryPack3TotalDischarge        | Number     | 100  | kWh     | RO          |
| Unit2BatteryPack3MinimumTemperature    | Number     | 10   | °C      | RO          |
| Unit2BatteryPack3MaximumTemperature    | Number     | 10   | °C      | RO          |

### MeterEquipmentRegister

| Name                      | Type   | Gain | Unit | Access Type |
|---------------------------|--------|------|------|-------------|
| MeterStatus               | Number | 1    |      | RO          |
| APhaseVoltage             | Number | 10   | V    | RO          |
| BPhaseVoltage             | Number | 10   | V    | RO          |
| CPhaseVoltage             | Number | 10   | V    | RO          |
| APhaseCurrent             | Number | 100  | A    | RO          |
| BPhaseCurrent             | Number | 100  | A    | RO          |
| CPhaseCurrent             | Number | 100  | A    | RO          |
| ActivePower               | Number | 1    | W    | RO          |
| ReactivePower             | Number | 1    | var  | RO          |
| PowerFactor               | Number | 1000 |      | RO          |
| GridFrequency             | Number | 100  | Hz   | RO          |
| PositiveActiveElectricity | Number | 100  | kWh  | RO          |
| ReverseActivePower        | Number | 100  | kWh  | RO          |
| AccumulatedReactivePower  | Number | 100  | kvar | RO          |
| MeterType                 | Number | 1    |      | RO          |
| ABLineVoltage             | Number | 10   | V    | RO          |
| BCLineVoltage             | Number | 10   | V    | RO          |
| CALineVoltage             | Number | 10   | V    | RO          |
| APhaseActivePower         | Number | 1    | W    | RO          |
| BPhaseActivePower         | Number | 1    | W    | RO          |
| CPhaseActivePower         | Number | 1    | W    | RO          |
| MeterModelDetectionResult | Number | 1    |      | RO          |
