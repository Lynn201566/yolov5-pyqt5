class SplitterController:
    def __init__(self, plc_comm, calibration):
        self.plc = plc_comm
        self.calib = calibration

    def update_splitter(self, detected_pixel_x):
        """Convert pixel x to mm and send to PLC."""
        mm = self.calib.pixel_to_mm(detected_pixel_x)
        print(f"Moving splitter to {mm:.1f} mm")
        self.plc.send_split_position(mm)