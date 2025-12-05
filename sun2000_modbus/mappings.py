DeviceStatus = {
    0x0000:	'Standby: initialization',
    0x0001:	'Standby: insulation resistance detection',
    0x0002:	'Standby: sunlight detection',
    0x0003:	'Standby: grid detecting',
    0x0100:	'Starting',
    0x0200:	'On-grid',
    0x0201:	'Grid connected: power limited',
    0x0202:	'Grid connected: self derating',
    0x0203:	'Off-grid operation',
    0x0300:	'OFF: unexpected shutdown',
    0x0301:	'OFF: instructed shutdown',
    0x0302:	'OFF: OVGR',
    0x0303:	'OFF: communication interrupted',
    0x0304:	'OFF: power limited',
    0x0305:	'OFF: manual startup required',
    0x0307:	'Shutdown: rapid shutdown',
    0x030A:	'Shutdown: commanded rapid shutdown',
    0x030B:	'Shutdown: the backup power system is abnormal',
    0x0401:	'Grid scheduling: cosPhi-P curve',
    0x0402:	'Grid scheduling: Q-U curve',
    0x0403:	'Grid scheduling: PF-U curve',
    0x0405:	'Grid scheduling: Q-P curve',
    0x0600:	'Inspecting ongoing',
    0x0700:	'AFCI check',
    0x0800:	'I-V curve scanning',
    0x0A00:	'Running: grid-disconnected and charged',
    0x0A01:	'Standby: the backup power system is abnormal',
    0xA000:	'Standby: no irradiation',
}

LicenseStatus = {
    0x0000: 'No License',
    0x0001: 'Normal',
    0x0002: 'In grace period',
    0x0003: 'Revoked',
    0x0004: 'SN not match',
    0x0005: 'Expired',
}

ModuleStatus4G = {
    0x0000: 'Card not found',
    0x0001: 'Card registration failed',
    0x0002: 'No connection',
    0x0003: 'Low signal strength',
    0x0004: 'Medium signal strength',
    0x0005: 'High signal strength',
    0x0006: 'Connected',
    0x0100: 'Card in position',
    0x0101: 'PIN required',
    0x0102: 'PUK required',
    0xFFFF: 'Module not found',
}

PINVerificationStatus4G = {
    0x0000: 'Initial state',
    0x0001: 'Verifying...',
}

ChargeDischargeMode = {
    0x0000: 'N/A',
    0x0001: 'Forced charge/discharge',
    0x0002: 'Time-of-use',
    0x0003: 'Fixed charge and discharge',
    0x0004: 'Max. self-consumption',
    0x0005: 'Fully fed to grid',
    0x0006: 'TOU',
    0x0007: 'Remote scheduling - Max. self-consumption',
    0x0008: 'Remote scheduling - Fully fed to grid',
    0x0009: 'Remote scheduling - TOU',
    0x000A: 'AI control',
    0x000B: 'Remote scheduling - AI control',
    0x000C: 'Three-party scheduling',
}

QUCharacteristicCurveMode = {
    0x0000: 'non-hysteresis',
    0x0001: 'hysteresis',
}

RemoteChargeDischargeControlMode = {
    0x0000: 'Local control',
    0x0001: 'Remote control - Max. self-consumption',
    0x0002: 'Remote control - Fully fed to grid',
    0x0003: 'Remote control - TOU',
    0x0004: 'Remote control - AI control',
    0x0005: 'Remote control - Three-party scheduling',
}

PeakShaving = {
    0x0000: 'Disabled',
    0x0001: 'Active power limit',
    0x0002: 'Apparent power limit',
}

BackupBoxModel = {
    0x0000: 'Backup Box - B0/B1',
    0x0001: 'Compatible Third Party Backup Box',
    0x0002: 'SmartGuard',
    0x0003: 'No Backup Box',
}

RunningStatus = {
    0: 'offline',
    1: 'standby',
    2: 'running',
    3: 'fault',
    4: 'sleep mode',
}

WorkingMode = {
    0: 'none',
    1: 'Forcible charge/discharge',
    2: 'Time of Use (LG)',
    3: 'Fixed charge/discharge',
    4: 'Maximise self consumption',
    5: 'Fully fed to grid',
    6: 'Time of Use (LUNA2000)',
}

ProductModel = {
    0: 'None',
    1: 'LG-RESU',
    2: 'HUAWEI-LUNA2000',
}

WorkingModeSettings = {
    0: 'Adaptive',
    1: 'Fixed charge/discharge',
    2: 'Maximise self consumption',
    3: 'Time of Use (LG)',
    4: 'Fully fed to grid',
    5: 'Time of Use (LUNA2000)',
}

ChargeFromGridFunction = {
    0: 'Disable',
    1: 'Enable',
}

ForcibleChargeDischarge = {
    0: 'Stop',
    1: 'Charge',
    2: 'Discharge',
}

ForcibleChargeDischargeSettingMode = {
    0: 'Duration',
}

ExcessPVEnergyUseInTOU = {
    0: 'Fed to grid',
    1: 'Charge',
}

SwitchToOffGrid = {
    0: 'Switch from grid-tied to off-grid',
}

VoltageIndependentOperation = {
    0: '101 V',
    1: '202 V',
}

MeterStatus = {
    0: 'offline',
    1: 'online',
}

MeterType = {
    0: 'single-phase',
    1: 'three-phase',
}

MeterModelDetectionResult = {
    0: 'being identified',
    1: 'The selected model is the same as the actual model of the connected meter',
    2: 'The selected model is different from the actual model of the connected meter',
}

ActivePowerControlMode = {
    0: 'Unlimited',
    1: 'DI active scheduling',
    5: 'Zero power grid connection',
    6: 'Powerlimited grid connection (kW)',
    7: 'Powerlimited grid connection (%)',
}
