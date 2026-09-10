from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List

from ..devices.base import TestDevice


@dataclass
class SessionConfig:
    name: str
    devices: List[str]


class Session:
    def __init__(self, name: str) -> None:
        self.name = name
        self._devices: Dict[str, TestDevice] = {}

    def add_device(self, device: TestDevice) -> None:
        self._devices[device.name] = device

    def initialize_all(self) -> None:
        for d in self._devices.values():
            d.initialize()

    def shutdown_all(self) -> None:
        for d in self._devices.values():
            d.shutdown()

    def get_device(self, name: str) -> TestDevice:
        return self._devices[name]
