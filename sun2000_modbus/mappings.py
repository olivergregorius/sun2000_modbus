DeviceStatus = {
    0x0000:	'Standby: initializing',
    0x0001:	'Standby: detecting insulation resistance',
    0x0002:	'Standby: detecting irradiation',
    0x0003:	'Standby: Grid detecting',
    0x0100:	'Starting',
    0x0200:	'On-grid',
    0x0201:	'Grid connection: power limited',
    0x0202:	'Grid connection: self-derating',
    0x0203:	'Off-grid Running',
    0x0300:	'Shutdown: fault',
    0x0301:	'Shutdown: command',
    0x0302:	'Shutdown: OVGR',
    0x0303:	'Shutdown: communication disconnected',
    0x0304:	'Shutdown: power limited',
    0x0305:	'Shutdown: manual startup required',
    0x0306:	'Shutdown: DC switches disconnected',
    0x0307:	'Shutdown: rapid cutoff',
    0x0308:	'Shutdown: input underpowered',
    0x0401:	'Grid scheduling: cosPhi-P curve',
    0x0402:	'Grid scheduling: Q-U curve',
    0x0403:	'Grid scheduling: PF-U curve',
    0x0404:	'Grid scheduling: dry contact',
    0x0405:	'Grid scheduling: Q-P curve',
    0x0500:	'Spot-check ready',
    0x0501:	'Spot-checking',
    0x0600:	'Inspecting',
    0x0700:	'AFCI self check',
    0x0800:	'I-V scanning',
    0x0900:	'DC input detection',
    0x0A00:	'Running: off-grid charging',
    0xA000:	'Standby: no irradiation'
}

RunningStatus = {
    0: 'offline',
    1: 'standby',
    2: 'running',
    3: 'fault',
    4: 'sleep mode'
}

WorkingMode = {
    0: 'none',
    1: 'Forcible charge/discharge',
    2: 'Time of Use (LG)',
    3: 'Fixed charge/discharge',
    4: 'Maximise self consumption',
    5: 'Fully fed to grid',
    6: 'Time of Use (LUNA2000)'
}

ProductModel = {
    0: 'None',
    1: 'LG-RESU',
    2: 'HUAWEI-LUNA2000'
}

WorkingModeSettings = {
    0: 'Adaptive',
    1: 'Fixed charge/discharge',
    2: 'Maximise self consumption',
    3: 'Time of Use (LG)',
    4: 'Fully fed to grid',
    5: 'Time of Use (LUNA2000)'
}

ChargeFromGridFunction = {
    0: 'Disable',
    1: 'Enable'
}

ForcibleChargeDischarge = {
    0: 'Stop',
    1: 'Charge',
    2: 'Discharge'
}

ForcibleChargeDischargeSettingMode = {
    0: 'Duration'
}

ExcessPVEnergyUseInTOU = {
    0: 'Fed to grid',
    1: 'Charge'
}

SwitchToOffGrid = {
    0: 'Switch from grid-tied to off-grid'
}

VoltageIndependentOperation = {
    0: '101 V',
    1: '202 V'
}

MeterStatus = {
    0: 'offline',
    1: 'online'
}

MeterType = {
    0: 'single-phase',
    1: 'three-phase'
}

MeterModelDetectionResult = {
    0: 'being identified',
    1: 'The selected model is the same as the actual model of the connected meter',
    2: 'The selected model is different from the actual model of the connected meter'
}

ActivePowerControlMode = {
    0: 'Unlimited',
    1: 'DI active scheduling',
    5: 'Zero power grid connection',
    6: 'Powerlimited grid connection (kW)',
    7: 'Powerlimited grid connection (%)'
}
