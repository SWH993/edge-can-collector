import time

import can


def simulate_ecu() -> None:
    print("[*] Starting Virtual ECU (CAN Simulator)...")

    try:
        bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    except OSError as e:
        print(f"[-] Error opening CAN bus: {e}")
        print("\t\tDid you run: sudo modprobe vcan && sudo ip link add dev vcan0 type vcan?")
        return

    counter = 0
    try:
        while True:
            speed = 50 + (counter % 30)
            msg_speed = can.Message(
                arbitration_id=0x101,
                data=[speed, 0x00, 0x0F, 0xFF, 0, 0, 0, 0],
                is_extended_id=False
            )

            temp = 90 + (counter % 5)
            msg_temp = can.Message(
                arbitration_id=0x102,
                data=[temp, 0x00, 0x00, 0, 0, 0, 0, 0],
                is_extended_id=False
            )

            bus.send(msg_speed)
            bus.send(msg_temp)

            print(f"[Sent] ECU Frame -> Speed: {speed} km/h | Engine Temp: {temp} °C")

            counter += 1
            time.sleep(1.0)

    except KeyboardInterrupt:
        print("\n[*] Stopping ECU Simulator.")
        bus.shutdown()

if __name__ == "__main__":
    simulate_ecu()