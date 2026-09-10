from test_equipment_controller.core.controller import TestEquipmentController


def test_basic_power_test_runs():
    controller = TestEquipmentController()
    controller.create_simulated_session("default")
    voltage = controller.run_basic_power_test("default")
    assert 0.0 < voltage < 10.0
