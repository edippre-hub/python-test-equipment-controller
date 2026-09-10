
# **Python Test Equipment Controller — Architecture Document**  
*Version 1.0 — September 2026*  
*Author: Eva Dippre*

---

## **1. Overview**

The **Python Test Equipment Controller (TEC)** is a modular, extensible framework for controlling electronic test equipment such as:

- Oscilloscopes  
- Power supplies  
- Digital multimeters (DMMs)  
- NI / VISA‑based instruments  
- Simulated instruments for offline development  

The architecture follows professional software engineering patterns used in aerospace, defense, and automated test systems (ATE). It supports:

- Device abstraction  
- Driver abstraction  
- Session orchestration  
- CLI scenario execution  
- Unit testing  
- CI/CD automation  

---

## **2. High-Level Architecture**

```
+-----------------------------------------------------------+
|                 Test Equipment Controller                 |
|-----------------------------------------------------------|
|  CLI Layer (tec)                                          |
|-----------------------------------------------------------|
|  Core Layer                                               |
|    - Controller                                           |
|    - Session                                              |
|-----------------------------------------------------------|
|  Device Layer                                             |
|    - Oscilloscope                                         |
|    - PowerSupply                                          |
|    - DigitalMultimeter                                    |
|-----------------------------------------------------------|
|  Driver Layer                                             |
|    - NI VISA Driver (future)                              |
|    - Simulated Driver                                     |
|-----------------------------------------------------------|
|  Config Layer                                             |
|    - profiles.yaml                                        |
+-----------------------------------------------------------+
```

---

## **3. Architectural Goals**

### **3.1 Modularity**
Each device type is isolated in its own module. Drivers are interchangeable.

### **3.2 Extensibility**
New instruments can be added by implementing the `TestDevice` abstract base class.

### **3.3 Testability**
The simulated driver enables:

- Offline development  
- Deterministic unit tests  
- CI/CD execution without hardware  

### **3.4 Maintainability**
Clear separation of concerns:

- Device logic  
- Driver logic  
- Session orchestration  
- CLI interface  

---

## **4. Core Components**

### **4.1 Controller**
`TestEquipmentController` orchestrates:

- Session creation  
- Device registration  
- Test scenario execution  

It acts as the “test executive” similar to NI TestStand or aerospace test sequencers.

### **4.2 Session**
A `Session` represents a test bench configuration:

- Contains multiple devices  
- Handles initialization and shutdown  
- Provides lookup by device name  

Sessions allow multiple benches (e.g., “RF Bench”, “Power Bench”, “Environmental Bench”).

---

## **5. Device Layer**

All devices inherit from:

### **`TestDevice` (Abstract Base Class)**

Defines required behaviors:

- `initialize()`  
- `shutdown()`  
- `identify()`  

This enforces consistency across all instruments.

### **Device Implementations**

| Device Type       | Capabilities |
|-------------------|--------------|
| Oscilloscope      | Autoscale, run/stop, Vpp measurement |
| PowerSupply       | Voltage/current set, output enable   |
| DigitalMultimeter | DC voltage measurement               |

Each device uses SCPI‑style commands, matching real aerospace test equipment.

---

## **6. Driver Layer**

### **6.1 SimulatedDriver**
Provides:

- Deterministic responses  
- Random measurement values  
- No hardware dependency  

Used for:

- CI/CD  
- Unit tests  
- Development without lab access  

### **6.2 NI VISA Driver (Future)**
Will support:

- GPIB  
- USB‑TMC  
- Serial  
- TCP/IP instruments  

Using `pyvisa`.

---

## **7. Configuration Layer**

### **profiles.yaml**
Defines bench configurations:

```yaml
default:
  description: "Simulated bench with oscilloscope, PSU, and DMM."
  devices:
    - Scope1
    - PSU1
    - DMM1
```

Future enhancements:

- Multiple benches  
- Hardware resource mapping  
- Calibration profiles  

---

## **8. CLI Layer**

The CLI (`tec`) provides:

- Scenario selection  
- Session initialization  
- Execution of automated tests  

Example:

```bash
tec --scenario basic-power-test
```

---

## **9. Test Architecture**

### **Unit Tests**
Located in `tests/`:

- `test_controller.py`  
- `test_devices.py`  
- `test_simulated_driver.py`  

### **CI/CD**
GitHub Actions workflow:

- Installs dependencies  
- Runs pytest  
- Generates coverage  

Ensures reliability and repeatability.

---

## **10. Future Enhancements**

### **Hardware Integration**
- NI VISA driver  
- Keysight / Tektronix instrument profiles  
- PXI chassis support  

### **Advanced Test Sequencing**
- JSON/YAML scenario definitions  
- Automated pass/fail criteria  
- Logging and data capture  

### **Aerospace/Defense Features**
- Deterministic timing  
- Safety interlocks  
- Redundant measurement validation  
- Calibration tracking  

---

## **11. Summary**

The **Python Test Equipment Controller** is a professional, modular, extensible framework suitable for:

- Aerospace ground test systems  
- Defense electronics validation  
- Automated manufacturing test  
- Lab automation  
- Education and simulation  

Its architecture follows industry best practices and is designed for long-term maintainability and scalability.
