from __future__ import annotations
from .base import TestDevice


class DigitalMultimeter(TestDevice):
    def initialize(self) -> None:
        self._driver.write("*RST")
        self._driver.write("CONF:VOLT:DC")

    def shutdown(self) -> None:
        # DMM usually just idle
        pass

    def identify(self) -> str:
        return self._driver.query("*IDN?")

    def measure_dc_voltage(self) -> float:
        resp = self._driver.query("READ?")
        return float(resp)
