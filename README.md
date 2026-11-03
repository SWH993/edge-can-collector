# 🚗 Edge CAN Collector & Simulator

Lightweight, containerized Edge/OT telemetry pipeline designed for Linux systems. This project bridges physical-layer/simulated automotive/industrial **CAN-bus** networks with modern containerization and **DevSecOps** pipelines.

---

## 🏗️ Architecture & Tech Stack

* **OS / Environment:** Debian Linux with virtual CAN (`vcan`) support.
* **Protocol:** Controller Area Network (CAN-bus) via SocketCAN.
* **Language:** Python 3.11 (`python-can` library).
* **Containerization:** Docker (`python:3.11-slim`).
* **CI/CD & Security:** GitHub Actions integrated with **Trivy** vulnerability scanner.

---

## ⚙️ Prerequisites

To run this project locally, you need a Debian-based Linux environment with kernel CAN support and `can-utils`:

```bash
# 1. Load kernel vcan module
sudo modprobe vcan

# 2. Setup virtual CAN interface
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# 3. Install network diagnostic utilities (optional)
sudo apt update && sudo apt install can-utils -y
```

---

## 🚀 Quick Start (Local Execution)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/edge-can-collector.git
   cd edge-can-collector
   ```

2. **Run the ECU Simulator (Terminal 1):**
   ```bash
   python3 can_simulator.py
   ```

3. **Run the Telemetry Collector (Terminal 2):**
   ```bash
   python3 can_collector.py
   ```
   *(Alternatively, monitor raw traffic using `candump vcan0`)*

---

## 🐳 Running via Docker

To run the collector inside an isolated container with access to the host's virtual CAN network:

1. **Build the Docker image:**
   ```bash
   docker build -t edge-can-collector:latest .
   ```

2. **Run the container (using host network namespace):**
   ```bash
   docker run --rm --net=host edge-can-collector:latest
   ```

---

## 🔒 Security & CI/CD

The project features automated vulnerability scanning using **Trivy** in GitHub Actions (`.github/workflows/ci.yml`). Every push or pull request triggers an automated container build and security audit, balancing robust security checks with realistic base-image management (risk-based triage).
