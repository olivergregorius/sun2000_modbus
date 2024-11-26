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

| Parameter | Description                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------|
| host      | IP address                                                                                                                          |
| port      | Port, usually 502, changed to 6607 on newer firmware versions.                                                                      |
| timeout   | Connection timeout                                                                                                                  |
| wait      | Time to wait after connection before a register read can be performed. Increases stability.                                         |
| slave     | Number of inverter unit to be read, used in cascading scenarios. Defaults to 0, but some devices need it to be set to other values. |

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

## Registers

The following registers are provided by the Sun2000's Modbus interface and can be read accordingly. Documentation can be found
[here](https://javierin.com/wp-content/uploads/sites/2/2021/09/Solar-Inverter-Modbus-Interface-Definitions.pdf).

### InverterEquipmentRegister

| Name                                    | Type                   | Gain | Unit | Remark                             |
|-----------------------------------------|------------------------|------|------|------------------------------------|
| Model                                   | String                 |      |      |                                    |
| SN                                      | String                 |      |      |                                    |
| PN                                      | String                 |      |      |                                    |
| FirmwareVerion                          | String                 |      |      |                                    |
| SoftwareVerion                          | String                 |      |      |                                    |
| ProtocolVerion                          | String                 |      |      |                                    |
| ModelID                                 | Number                 | 1    |      |                                    |
| NumberOfPVStrings                       | Number                 | 1    |      |                                    |
| NumberOfMPPTrackers                     | Number                 | 1    |      |                                    |
| RatedPower                              | Number                 | 1    | W    |                                    |
| MaximumActivePower                      | Number                 | 1    | W    |                                    |
| MaximumApparentPower                    | Number                 | 1000 | kVA  |                                    |
| MaximumReactivePowerFedToTheGrid        | Number                 | 1000 | kvar |                                    |
| MaximumReactivePowerAbsorbedFromTheGrid | Number                 | 1000 | kvar |                                    |
| State1                                  | Binary String/Bitfield |      |      |                                    |
| State2                                  | Binary String/Bitfield |      |      |                                    |
| State3                                  | Binary String/Bitfield |      |      |                                    |
| Alarm1                                  | Binary String/Bitfield |      |      |                                    |
| Alarm2                                  | Binary String/Bitfield |      |      |                                    |
| Alarm3                                  | Binary String/Bitfield |      |      |                                    |
| PV1Voltage                              | Number                 | 10   | V    |                                    |
| PV1Current                              | Number                 | 100  | A    |                                    |
| PV2Voltage                              | Number                 | 10   | V    |                                    |
| PV2Current                              | Number                 | 100  | A    |                                    |
| PV3Voltage                              | Number                 | 10   | V    |                                    |
| PV3Current                              | Number                 | 100  | A    |                                    |
| PV4Voltage                              | Number                 | 10   | V    |                                    |
| PV4Current                              | Number                 | 100  | A    |                                    |
| PV5Voltage                              | Number                 | 10   | V    |                                    |
| PV5Current                              | Number                 | 100  | A    |                                    |
| PV6Voltage                              | Number                 | 10   | V    |                                    |
| PV6Current                              | Number                 | 100  | A    |                                    |
| PV7Voltage                              | Number                 | 10   | V    |                                    |
| PV7Current                              | Number                 | 100  | A    |                                    |
| PV8Voltage                              | Number                 | 10   | V    |                                    |
| PV8Current                              | Number                 | 100  | A    |                                    |
| PV9Voltage                              | Number                 | 10   | V    |                                    |
| PV9Current                              | Number                 | 100  | A    |                                    |
| PV10Voltage                             | Number                 | 10   | V    |                                    |
| PV10Current                             | Number                 | 100  | A    |                                    |
| PV11Voltage                             | Number                 | 10   | V    |                                    |
| PV11Current                             | Number                 | 100  | A    |                                    |
| PV12Voltage                             | Number                 | 10   | V    |                                    |
| PV12Current                             | Number                 | 100  | A    |                                    |
| PV13Voltage                             | Number                 | 10   | V    |                                    |
| PV13Current                             | Number                 | 100  | A    |                                    |
| PV14Voltage                             | Number                 | 10   | V    |                                    |
| PV14Current                             | Number                 | 100  | A    |                                    |
| PV15Voltage                             | Number                 | 10   | V    |                                    |
| PV15Current                             | Number                 | 100  | A    |                                    |
| PV16Voltage                             | Number                 | 10   | V    |                                    |
| PV16Current                             | Number                 | 100  | A    |                                    |
| PV17Voltage                             | Number                 | 10   | V    |                                    |
| PV17Current                             | Number                 | 100  | A    |                                    |
| PV18Voltage                             | Number                 | 10   | V    |                                    |
| PV18Current                             | Number                 | 100  | A    |                                    |
| PV19Voltage                             | Number                 | 10   | V    |                                    |
| PV19Current                             | Number                 | 100  | A    |                                    |
| PV20Voltage                             | Number                 | 10   | V    |                                    |
| PV20Current                             | Number                 | 100  | A    |                                    |
| PV21Voltage                             | Number                 | 10   | V    |                                    |
| PV21Current                             | Number                 | 100  | A    |                                    |
| PV22Voltage                             | Number                 | 10   | V    |                                    |
| PV22Current                             | Number                 | 100  | A    |                                    |
| PV23Voltage                             | Number                 | 10   | V    |                                    |
| PV23Current                             | Number                 | 100  | A    |                                    |
| PV24Voltage                             | Number                 | 10   | V    |                                    |
| PV24Current                             | Number                 | 100  | A    |                                    |
| InputPower                              | Number                 | 1    | W    |                                    |
| LineVoltageBetweenPhasesAAndB           | Number                 | 10   | V    |                                    |
| LineVoltageBetweenPhasesBAndC           | Number                 | 10   | V    |                                    |
| LineVoltageBetweenPhasesCAndA           | Number                 | 10   | V    |                                    |
| PhaseAVoltage                           | Number                 | 10   | V    |                                    |
| PhaseBVoltage                           | Number                 | 10   | V    |                                    |
| PhaseCVoltage                           | Number                 | 10   | V    |                                    |
| PhaseACurrent                           | Number                 | 1000 | A    |                                    |
| PhaseBCurrent                           | Number                 | 1000 | A    |                                    |
| PhaseCCurrent                           | Number                 | 1000 | A    |                                    |
| PeakActivePowerOfCurrentDay             | Number                 | 1    | W    |                                    |
| ActivePower                             | Number                 | 1    | W    |                                    |
| ReactivePower                           | Number                 | 1000 | kvar |                                    |
| PowerFactor                             | Number                 | 1000 |      |                                    |
| GridFrequency                           | Number                 | 100  | Hz   |                                    |
| Efficiency                              | Number                 | 100  | %    |                                    |
| InternalTemperature                     | Number                 | 10   | °C   |                                    |
| InsulationResistance                    | Number                 | 1000 | MOhm |                                    |
| DeviceStatus                            | Number                 | 1    |      |                                    |
| FaultCode                               | Number                 | 1    |      |                                    |
| StartupTime                             | Number                 | 1    |      |                                    |
| ShutdownTime                            | Number                 | 1    |      |                                    |
| AccumulatedEnergyYield                  | Number                 | 100  | kWh  |                                    |
| DailyEnergyYield                        | Number                 | 100  | kWh  |                                    |
| ActiveAdjustmentMode                    | Number                 | 1    |      |                                    |
| ActiveAdjustmentValue                   | Number                 | 1    |      |                                    |
| ActiveAdjustmentCommand                 | Number                 | 1    |      |                                    |
| ReactiveAdjustmentMode                  | Number                 | 1    |      |                                    |
| ReactiveAdjustmentValue                 | Number                 | 1    |      |                                    |
| ReactiveAdjustmentCommand               | Number                 | 1    |      |                                    |
| PowerMeterCollectionActivePower         | Number                 | 1    | W    |                                    |
| TotalNumberOfOptimizers                 | Number                 | 1    |      |                                    |
| NumberOfOnlineOptimizers                | Number                 | 1    |      |                                    |
| FeatureData                             | Number                 | 1    |      |                                    |
| SystemTime                              | Number                 | 1    |      |                                    |
| QUCharacteristicCurveMode               | Number                 | 1    |      |                                    |
| QUDispatchTriggerPower                  | Number                 | 1    | %    |                                    |
| FixedActivePowerDeratedInKW             | Number                 | 10   | kW   |                                    |
| ReactivePowerCompensationInPF           | Number                 | 1000 |      |                                    |
| ReactivePowerCompensationQS             | Number                 | 1000 |      |                                    |
| ActivePowerPercentageDerating           | Number                 | 10   | %    |                                    |
| FixedActivePowerDeratedInW              | Number                 | 1    | W    |                                    |
| ReactivePowerCompensationAtNight        | Number                 | 1000 | kvar |                                    |
| CosPhiPPnCharacteristicCurve            | Bytestring             |      |      |                                    |
| QUCharacteristicCurve                   | Bytestring             |      |      |                                    |
| PFUCharacteristicCurve                  | Bytestring             |      |      |                                    |
| ReactivePowerAdjustmentTime             | Number                 | 1    | s    |                                    |
| QUPowerPercentageToExitScheduling       | Number                 | 1    | %    |                                    |
| Startup                                 | Number                 | 1    |      | Write only, not available for read |
| Shutdown                                | Number                 | 1    |      | Write only, not available for read |
| GridCode                                | Number                 | 1    |      |                                    |
| ReactivePowerChangeGradient             | Number                 | 1000 | %/s  |                                    |
| ActivePowerChangeGradient               | Number                 | 1000 | %/s  |                                    |
| ScheduleInstructionValidDuration        | Number                 | 1    | s    |                                    |
| TimeZone                                | Number                 | 1    | min  |                                    |

### BatteryEquipmentRegister

| Name                                   | Type       | Gain | Unit    | Remark                             |
|----------------------------------------|------------|------|---------|------------------------------------|
| RunningStatus                          | Number     | 1    |         |                                    |
| WorkingModeSettings                    | Number     | 1    |         |                                    |
| BusVoltage                             | Number     | 10   | V       |                                    |
| BusCurrent                             | Number     | 10   | A       |                                    |
| ChargeDischargePower                   | Number     | 1    | W       |                                    |
| MaximumChargePower                     | Number     | 1    | W       |                                    |
| MaximumDischargePower                  | Number     | 1    | W       |                                    |
| RatedCapacity                          | Number     | 1    | Wh      |                                    |
| SOC                                    | Number     | 10   | %       |                                    |
| BackupPowerSOC                         | Number     | 10   | %       |                                    |
| TotalCharge                            | Number     | 100  | kWh     |                                    |
| TotalDischarge                         | Number     | 100  | kWh     |                                    |
| CurrentDayChargeCapacity               | Number     | 100  | kWh     |                                    |
| CurrentDayDischargeCapacity            | Number     | 100  | kWh     |                                    |
| TimeOfUseElectricityPricePeriods       | Bytestring |      |         |                                    |
| MaximumChargingPower                   | Number     | 1    | W       |                                    |
| MaximumDischargingPower                | Number     | 1    | W       |                                    |
| ChargingCutoffCapacity                 | Number     | 10   | %       |                                    |
| DischargeCutoffCapacity                | Number     | 10   | %       |                                    |
| ForcedChargingAndDischargingPeriod     | Number     | 1    | minutes |                                    |
| ChargeFromGridFunction                 | Number     | 1    |         |                                    |
| GridChargeCutoffSOC                    | Number     | 10   | %       |                                    |
| ForcibleChargeDischarge                | Number     | 1    |         | Write only, not available for read |
| FixedChargingAndDischargingPeriods     | Bytestring |      |         |                                    |
| PowerOfChargeFromGrid                  | Number     | 0.1  | W       |                                    |
| MaximumPowerOfChargeFromGrid           | Number     | 0.1  | W       |                                    |
| ForcibleChargeDischargeSettingMode     | Number     | 1    |         |                                    |
| ForcibleChargePower                    | Number     | 0.1  | W       |                                    |
| ForcibleDischargePower                 | Number     | 0.1  | W       |                                    |
| TimeOfUseChargingAndDischargingPeriods | Bytestring |      |         |                                    |
| ExcessPVEnergyUseInTOU                 | Number     | 1    |         |                                    |
| ActivePowerControlMode                 | Number     | 1    |         |                                    |
| MaximumFeedGridPowerInKW               | Number     | 1000 | kW      |                                    |
| MaximumFeedGridPowerInPercentage       | Number     | 10   | %       |                                    |
| MaximumChargeFromGridPower             | Number     | 0.1  | W       |                                    |
| SwitchToOffGrid                        | Number     | 1    |         |                                    |
| VoltageInIndependentOperation          | Number     | 1    |         |                                    |
| Unit1ProductModel                      | Number     | 1    |         |                                    |
| Unit1SN                                | String     |      |         |                                    |
| Unit1No                                | Number     | 1    |         |                                    |
| Unit1SoftwareVersion                   | String     |      |         |                                    |
| Unit1DCDCVersion                       | String     |      |         |                                    |
| Unit1BMSVersion                        | String     |      |         |                                    |
| Unit1RunningStatus                     | Number     | 1    |         |                                    |
| Unit1WorkingMode                       | Number     | 1    |         |                                    |
| Unit1BusVoltage                        | Number     | 10   | V       |                                    |
| Unit1BusCurrent                        | Number     | 10   | A       |                                    |
| Unit1BatterySOC                        | Number     | 10   | %       |                                    |
| Unit1ChargeAndDischargePower           | Number     | 1    | W       |                                    |
| Unit1RemainingChargeDischargeTime      | Number     | 1    | minutes |                                    |
| Unit1RatedChargePower                  | Number     | 1    | W       |                                    |
| Unit1RatedDischargePower               | Number     | 1    | W       |                                    |
| Unit1CurrentDayChargeCapacity          | Number     | 100  | kWh     |                                    |
| Unit1CurrentDayDischargeCapacity       | Number     | 100  | kWh     |                                    |
| Unit1TotalCharge                       | Number     | 100  | kWh     |                                    |
| Unit1TotalDischarge                    | Number     | 100  | kWh     |                                    |
| Unit1BatteryTemperature                | Number     | 10   | °C      |                                    |
| Unit1FaultID                           | Number     | 1    |         |                                    |
| Unit2ProductModel                      | Number     | 1    |         |                                    |
| Unit2SN                                | String     |      |         |                                    |
| Unit2No                                | Number     | 1    |         |                                    |
| Unit2SoftwareVersion                   | String     |      |         |                                    |
| Unit2RunningStatus                     | Number     | 1    |         |                                    |
| Unit2BusVoltage                        | Number     | 10   | V       |                                    |
| Unit2BusCurrent                        | Number     | 10   | A       |                                    |
| Unit2BatterySOC                        | Number     | 10   | %       |                                    |
| Unit2ChargeAndDischargePower           | Number     | 1    | W       |                                    |
| Unit2CurrentDayChargeCapacity          | Number     | 100  | kWh     |                                    |
| Unit2CurrentDayDischargeCapacity       | Number     | 100  | kWh     |                                    |
| Unit2TotalCharge                       | Number     | 100  | kWh     |                                    |
| Unit2TotalDischarge                    | Number     | 100  | kWh     |                                    |
| Unit2BatteryTemperature                | Number     | 10   | °C      |                                    |
| Unit1BatteryPack1SN                    | String     |      |         |                                    |
| Unit1BatteryPack1No                    | Number     | 1    |         |                                    |
| Unit1BatteryPack1FirmwareVersion       | String     |      |         |                                    |
| Unit1BatteryPack1WorkingStatus         | Number     | 1    |         |                                    |
| Unit1BatteryPack1Voltage               | Number     | 10   | V       |                                    |
| Unit1BatteryPack1Current               | Number     | 10   | A       |                                    |
| Unit1BatteryPack1SOC                   | Number     | 10   | %       |                                    |
| Unit1BatteryPack1ChargeDischargePower  | Number     | 1    | W       |                                    |
| Unit1BatteryPack1TotalCharge           | Number     | 100  | kWh     |                                    |
| Unit1BatteryPack1TotalDischarge        | Number     | 100  | kWh     |                                    |
| Unit1BatteryPack1MinimumTemperature    | Number     | 10   | °C      |                                    |
| Unit1BatteryPack1MaximumTemperature    | Number     | 10   | °C      |                                    |
| Unit1BatteryPack2SN                    | String     |      |         |                                    |
| Unit1BatteryPack2No                    | Number     | 1    |         |                                    |
| Unit1BatteryPack2FirmwareVersion       | String     |      |         |                                    |
| Unit1BatteryPack2WorkingStatus         | Number     | 1    |         |                                    |
| Unit1BatteryPack2Voltage               | Number     | 10   | V       |                                    |
| Unit1BatteryPack2Current               | Number     | 10   | A       |                                    |
| Unit1BatteryPack2SOC                   | Number     | 10   | %       |                                    |
| Unit1BatteryPack2ChargeDischargePower  | Number     | 1    | W       |                                    |
| Unit1BatteryPack2TotalCharge           | Number     | 100  | kWh     |                                    |
| Unit1BatteryPack2TotalDischarge        | Number     | 100  | kWh     |                                    |
| Unit1BatteryPack2MinimumTemperature    | Number     | 10   | °C      |                                    |
| Unit1BatteryPack2MaximumTemperature    | Number     | 10   | °C      |                                    |
| Unit1BatteryPack3SN                    | String     |      |         |                                    |
| Unit1BatteryPack3No                    | Number     | 1    |         |                                    |
| Unit1BatteryPack3FirmwareVersion       | String     |      |         |                                    |
| Unit1BatteryPack3WorkingStatus         | Number     | 1    |         |                                    |
| Unit1BatteryPack3Voltage               | Number     | 10   | V       |                                    |
| Unit1BatteryPack3Current               | Number     | 10   | A       |                                    |
| Unit1BatteryPack3SOC                   | Number     | 10   | %       |                                    |
| Unit1BatteryPack3ChargeDischargePower  | Number     | 1    | W       |                                    |
| Unit1BatteryPack3TotalCharge           | Number     | 100  | kWh     |                                    |
| Unit1BatteryPack3TotalDischarge        | Number     | 100  | kWh     |                                    |
| Unit1BatteryPack3MinimumTemperature    | Number     | 10   | °C      |                                    |
| Unit1BatteryPack3MaximumTemperature    | Number     | 10   | °C      |                                    |
| Unit2BatteryPack1SN                    | String     |      |         |                                    |
| Unit2BatteryPack1No                    | Number     | 1    |         |                                    |
| Unit2BatteryPack1FirmwareVersion       | String     |      |         |                                    |
| Unit2BatteryPack1WorkingStatus         | Number     | 1    |         |                                    |
| Unit2BatteryPack1Voltage               | Number     | 10   | V       |                                    |
| Unit2BatteryPack1Current               | Number     | 10   | A       |                                    |
| Unit2BatteryPack1SOC                   | Number     | 10   | %       |                                    |
| Unit2BatteryPack1ChargeDischargePower  | Number     | 1    | W       |                                    |
| Unit2BatteryPack1TotalCharge           | Number     | 100  | kWh     |                                    |
| Unit2BatteryPack1TotalDischarge        | Number     | 100  | kWh     |                                    |
| Unit2BatteryPack1MinimumTemperature    | Number     | 10   | °C      |                                    |
| Unit2BatteryPack1MaximumTemperature    | Number     | 10   | °C      |                                    |
| Unit2BatteryPack2SN                    | String     |      |         |                                    |
| Unit2BatteryPack2No                    | Number     | 1    |         |                                    |
| Unit2BatteryPack2FirmwareVersion       | String     |      |         |                                    |
| Unit2BatteryPack2WorkingStatus         | Number     | 1    |         |                                    |
| Unit2BatteryPack2Voltage               | Number     | 10   | V       |                                    |
| Unit2BatteryPack2Current               | Number     | 10   | A       |                                    |
| Unit2BatteryPack2SOC                   | Number     | 10   | %       |                                    |
| Unit2BatteryPack2ChargeDischargePower  | Number     | 1    | W       |                                    |
| Unit2BatteryPack2TotalCharge           | Number     | 100  | kWh     |                                    |
| Unit2BatteryPack2TotalDischarge        | Number     | 100  | kWh     |                                    |
| Unit2BatteryPack2MinimumTemperature    | Number     | 10   | °C      |                                    |
| Unit2BatteryPack2MaximumTemperature    | Number     | 10   | °C      |                                    |
| Unit2BatteryPack3SN                    | String     |      |         |                                    |
| Unit2BatteryPack3No                    | Number     | 1    |         |                                    |
| Unit2BatteryPack3FirmwareVersion       | String     |      |         |                                    |
| Unit2BatteryPack3WorkingStatus         | Number     | 1    |         |                                    |
| Unit2BatteryPack3Voltage               | Number     | 10   | V       |                                    |
| Unit2BatteryPack3Current               | Number     | 10   | A       |                                    |
| Unit2BatteryPack3SOC                   | Number     | 10   | %       |                                    |
| Unit2BatteryPack3ChargeDischargePower  | Number     | 1    | W       |                                    |
| Unit2BatteryPack3TotalCharge           | Number     | 100  | kWh     |                                    |
| Unit2BatteryPack3TotalDischarge        | Number     | 100  | kWh     |                                    |
| Unit2BatteryPack3MinimumTemperature    | Number     | 10   | °C      |                                    |
| Unit2BatteryPack3MaximumTemperature    | Number     | 10   | °C      |                                    |

### MeterEquipmentRegister

| Name                      | Type   | Gain | Unit |
|---------------------------|--------|------|------|
| MeterStatus               | Number | 1    |      |
| APhaseVoltage             | Number | 10   | V    |
| BPhaseVoltage             | Number | 10   | V    |
| CPhaseVoltage             | Number | 10   | V    |
| APhaseCurrent             | Number | 100  | A    |
| BPhaseCurrent             | Number | 100  | A    |
| CPhaseCurrent             | Number | 100  | A    |
| ActivePower               | Number | 1    | W    |
| ReactivePower             | Number | 1    | var  |
| PowerFactor               | Number | 1000 |      |
| GridFrequency             | Number | 100  | Hz   |
| PositiveActiveElectricity | Number | 100  | kWh  |
| ReverseActivePower        | Number | 100  | kWh  |
| AccumulatedReactivePower  | Number | 100  | kvar |
| MeterType                 | Number | 1    |      |
| ABLineVoltage             | Number | 10   | V    |
| BCLineVoltage             | Number | 10   | V    |
| CALineVoltage             | Number | 10   | V    |
| APhaseActivePower         | Number | 1    | W    |
| BPhaseActivePower         | Number | 1    | W    |
| CPhaseActivePower         | Number | 1    | W    |
| MeterModelDetectionResult | Number | 1    |      |
