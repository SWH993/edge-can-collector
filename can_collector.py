import can


def parse_can_message(msg: str) -> None:
    if msg.arbitration_id == 0x101:
        speed = msg.data[0]
        print(f"[COLLECTOR] Speed Update: {speed} km/h")

    elif msg.arbitration_id == 0x102:
        temp = msg.data[0]
        print(f"[COLLECTOR] Engine Temp: {temp} °C")

def start_collector():
    print("[*] Starting CAN Telemetry Collector listening on vcan0...")
    try:
        bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    except OSError as e:
        print(f"[-] Error attaching to CAN bus: {e}")
        return

    try:
        for msg in bus:
            parse_can_message(msg)
    except KeyboardInterrupt:
        print("\n[*] Stopping CAN Collector.")
        bus.shutdown()


if __name__ == "__main__":
    start_collector()