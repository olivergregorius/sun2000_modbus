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
    # 0x030C is not officially documented, yet, but the Huawei support declared it as a valid status (https://www.photovoltaikforum.com/thread/160098-what-s-up-huawei/?postID=4478596#post4478596)
    0x030C:	'Shutdown: battery end-of-discharge SOC',
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
    0x0000: 'offline',
    0x0001: 'standby',
    0x0002: 'running',
    0x0003: 'fault',
    0x0004: 'sleep mode',
}

WorkingModeSettings = {
    0x0000: 'Adaptive',
    0x0001: 'Fixed charge/discharge',
    0x0002: 'Maximise self consumption',
    0x0003: 'Time of Use (LG)',
    0x0004: 'Fully fed to grid',
    0x0005: 'Time of Use (LUNA2000)',
}

ForcibleChargeDischarge = {
    0x0000: 'Stop',
    0x0001: 'Charge',
    0x0002: 'Discharge',
}

ExcessPVEnergyUseInTOU = {
    0x0000: 'Fed to grid',
    0x0001: 'Charge',
}

ActivePowerControlMode = {
    0x0000: 'Unlimited',
    0x0001: 'DI active scheduling',
    0x0005: 'Zero power grid connection',
    0x0006: 'Power-limited grid connection (kW)',
    0x0007: 'Power-limited grid connection (%)',
}

VoltageIndependentOperation = {
    0x0000: '101 V',
    0x0001: '202 V',
}

ProductModel = {
    0x0000: 'None',
    0x0001: 'LG-RESU',
    0x0002: 'HUAWEI-LUNA2000',
}

WorkingMode = {
    0x0000: 'none',
    0x0001: 'Forcible charge/discharge',
    0x0002: 'Time of Use (LG)',
    0x0003: 'Fixed charge/discharge',
    0x0004: 'Maximise self consumption',
    0x0005: 'Fully fed to grid',
    0x0006: 'Time of Use (LUNA2000)',
    0x0007: 'Remote scheduling - maximum self-use',
    0x0008: 'Remote scheduling - full internet access',
    0x0009: 'Remote scheduling - TOU',
    0x000A: 'AI energy management and scheduling',
}

MeterType = {
    0x0000: 'single-phase',
    0x0001: 'three-phase',
}

MeterStatus = {
    0x0000: 'offline',
    0x0001: 'normal',
}

MeterModelDetectionResult = {
    0x0000: 'being identified',
    0x0001: 'The selected model is the same as the actual model of the connected meter',
    0x0002: 'The selected model is different from the actual model of the connected meter',
}
