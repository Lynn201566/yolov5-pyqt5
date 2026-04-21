import cv2
import numpy as np
import torch
import random

def load_mosaic9(images, labels, img_size=640):
    """Load 9 images in a 3x3 mosaic."""
    mosaic_img = np.full((img_size * 3, img_size * 3, 3), 114, dtype=np.uint8)
    offsets = [(0, 0), (0, img_size), (0, 2*img_size),
               (img_size, 0), (img_size, img_size), (img_size, 2*img_size),
               (2*img_size, 0), (2*img_size, img_size), (2*img_size, 2*img_size)]
    labels4 = []
    for i, (img, lb) in enumerate(zip(images, labels)):
        h, w = img.shape[:2]
        scale = min(img_size / max(h, w), 1.0)
        new_w, new_h = int(w * scale), int(h * scale)
        img = cv2.resize(img, (new_w, new_h))
        dx, dy = offsets[i]
        mosaic_img[dy:dy+new_h, dx:dx+new_w] = img
        if len(lb):
            lb[:, 1] = (lb[:, 1] * w) * scale + dx
            lb[:, 2] = (lb[:, 2] * h) * scale + dy
            lb[:, 3] *= w * scale
            lb[:, 4] *= h * scale
            labels4.append(lb)
    if labels4:
        labels4 = np.concatenate(labels4, 0)
    return mosaic_img, labels4