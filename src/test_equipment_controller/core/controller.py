from __future__ import annotations
from typing import Dict

from .session import Session
from ..devices.oscilloscope import Oscilloscope
from ..devices.power_supply import PowerSupply
from ..devices.dmm import DigitalMultimeter
from ..drivers.simulated_driver import SimulatedDriver


class TestEquipmentController:
    def __init__(self) -> None:
        self.sessions: Dict[str, Session] = {}

    def create_simulated_session(self, name: str = "default") -> Session:
        session = Session(name)

        scope_driver = SimulatedDriver("OSC")
        psu_driver = SimulatedDriver("PSU")
        dmm_driver = SimulatedDriver("DMM")

        scope = Oscilloscope("Scope1", "SIM::OSC", scope_driver)
        psu = PowerSupply("PSU1", "SIM::PSU", psu_driver)
        dmm = DigitalMultimeter("DMM1", "SIM::DMM", dmm_driver)

        session.add_device(scope)
        session.add_device(psu)
        session.add_device(dmm)

        self.sessions[name] = session
        return session

    def run_basic_power_test(self, session_name: str = "default") -> float:
        session = self.sessions[session_name]
        psu: PowerSupply = session.get_device("PSU1")  # type: ignore[assignment]
        dmm: DigitalMultimeter = session.get_device("DMM1")  # type: ignore[assignment]

        psu.initialize()
        psu.set_output(5.0, 1.0)
        psu.enable_output(True)

        voltage = dmm.measure_dc_voltage()

        psu.enable_output(False)
        psu.shutdown()

        return voltage
