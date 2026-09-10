from __future__ import annotations
from .base import TestDevice


class Oscilloscope(TestDevice):
    def initialize(self) -> None:
        self._driver.write("*RST")
        self._driver.write(":AUTOSCALE")
        self._driver.write(":RUN")

    def shutdown(self) -> None:
        self._driver.write(":STOP")

    def identify(self) -> str:
        return self._driver.query("*IDN?")

    def measure_peak_to_peak(self, channel: int = 1) -> float:
        self._driver.write(f":MEASure:VPP CHANnel{channel}")
        resp = self._driver.query(":MEASure:VPP?")
        return float(resp)
