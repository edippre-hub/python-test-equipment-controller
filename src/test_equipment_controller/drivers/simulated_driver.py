from __future__ import annotations
import random


class SimulatedDriver:
    def __init__(self, name: str) -> None:
        self.name = name
        self._last_command = ""

    def write(self, command: str) -> None:
        self._last_command = command

    def query(self, command: str) -> str:
        self._last_command = command
        if command == "*IDN?":
            return f"{self.name},SIMULATED,0.1"
        if "MEASure:VPP?" in command or "READ?" in command:
            return f"{random.uniform(0.1, 5.0):.3f}"
        return "0"
