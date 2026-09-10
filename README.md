# python-test-equipment-controller
Python Test Equipment Controller project (similar to what is used in aerospace, defense, NI hardware, oscilloscopes, power supplies, and electronic test systems), organize your Git repository like a professional software engineering project.
# python-test-equipment-controller

Python Test Equipment Controller for oscilloscopes, power supplies, DMMs, and NI-style hardware.

## Features

- Device abstraction for common lab instruments
- Simulated driver for offline development
- Session and controller orchestration
- CLI scenarios (e.g., basic power test)
- Pytest-based test suite
- GitHub Actions CI

## Quick start

```bash
pip install -e .[dev]
tec --scenario basic-power-test
