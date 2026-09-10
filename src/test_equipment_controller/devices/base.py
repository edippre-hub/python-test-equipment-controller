from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol


class Driver(Protocol):
    def write(self, command: str) -> None: ...
    def query(self, command: str) -> str: ...


class TestDevice(ABC):
    def __init__(self, name: str, resource: str, driver: Driver) -> None:
        self.name = name
        self.resource = resource
        self._driver = driver

    @abstractmethod
    def initialize(self) -> None:
        ...

    @abstractmethod
    def shutdown(self) -> None:
        ...

    @abstractmethod
    def identify(self) -> str:
        ...
