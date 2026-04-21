import cv2
import numpy as np

class Calibration:
    def __init__(self, ref_width_mm=100, ref_pixel_width=None):
        """
        ref_width_mm: known width in mm
        ref_pixel_width: measured pixel width of the same object
        """
        self.mm_per_pixel = None
        if ref_pixel_width is not None:
            self.mm_per_pixel = ref_width_mm / ref_pixel_width

    def calibrate_from_image(self, image, aruco_dict=cv2.aruco.DICT_4X4_50):
        """Use ArUco marker for calibration (optional)."""
        # Placeholder: user can implement marker detection
        pass

    def pixel_to_mm(self, pixel_coord):
        if self.mm_per_pixel is None:
            raise ValueError("Calibration not performed.")
        return pixel_coord * self.mm_per_pixel