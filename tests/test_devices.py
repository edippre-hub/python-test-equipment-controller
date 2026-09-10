from test_equipment_controller.devices.oscilloscope import Oscilloscope
from test_equipment_controller.devices.power_supply import PowerSupply
from test_equipment_controller.devices.dmm import DigitalMultimeter
from test_equipment_controller.drivers.simulated_driver import SimulatedDriver


def test_oscilloscope_identify():
    scope = Oscilloscope("Scope1", "SIM::OSC", SimulatedDriver("OSC"))
    idn = scope.identify()
    assert "SIMULATED" in idn


def test_power_supply_output():
    psu = PowerSupply("PSU1", "SIM::PSU", SimulatedDriver("PSU"))
    psu.initialize()
    psu.set_output(5.0, 1.0)
    psu.enable_output(True)


def test_dmm_measure():
    dmm = DigitalMultimeter("DMM1", "SIM::DMM", SimulatedDriver("DMM"))
    dmm.initialize()
    v = dmm.measure_dc_voltage()
    assert v > 0.0
