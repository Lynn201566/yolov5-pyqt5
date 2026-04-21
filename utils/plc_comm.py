import serial
import time

class PLCComm:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
        except Exception as e:
            print(f"PLC serial error: {e}")

    def send_split_position(self, position_mm):
        """Send split position in mm to PLC."""
        if self.ser and self.ser.is_open:
            cmd = f"SPLIT,{int(position_mm)}\n"
            self.ser.write(cmd.encode())
            return True
        return False

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()