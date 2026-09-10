from __future__ import annotations
import argparse
from rich.console import Console

from .core.controller import TestEquipmentController

console = Console()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Python Test Equipment Controller (simulated)."
    )
    parser.add_argument(
        "--scenario",
        choices=["basic-power-test"],
        default="basic-power-test",
        help="Test scenario to run.",
    )
    args = parser.parse_args()

    controller = TestEquipmentController()
    session = controller.create_simulated_session("default")
    session.initialize_all()

    if args.scenario == "basic-power-test":
        voltage = controller.run_basic_power_test("default")
        console.print(f"[green]Measured voltage:[/green] {voltage:.3f} V")

    session.shutdown_all()

