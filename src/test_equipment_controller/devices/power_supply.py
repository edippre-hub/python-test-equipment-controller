from __future__ import annotations
from .base import TestDevice


class PowerSupply(TestDevice):
    def initialize(self) -> None:
        self._driver.write("*RST")
        self._driver.write("OUTP OFF")

    def shutdown(self) -> None:
        self._driver.write("OUTP OFF")

    def identify(self) -> str:
        return self._driver.query("*IDN?")

    def set_output(self, voltage: float, current: float) -> None:
        self._driver.write(f"VOLT {voltage}")
        self._driver.write(f"CURR {current}")

    def enable_output(self, enable: bool = True) -> None:
        self._driver.write(f"OUTP {'ON' if enable else 'OFF'}")
