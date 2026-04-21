# Adaptive Interception System for Spiral Concentrators (Improved YOLOv5)

This repository contains the implementation of the adaptive concentrate interception system described in the paper:

> **Investigation of adaptive interception systems for concentrate in spiral concentrators**  
> Huizhong LIU, Fulong DENG,QIhua ZHOU, Yao LONG, Xixi LIU, Ruoyun ZHANG, Jian NING

The system uses an enhanced YOLOv5 deep learning model (YOLOv5‑CASM) to detect the concentrate split point in real time and automatically adjusts a servo‑driven splitter via PLC control.

## Features

- **Improved YOLOv5 detector** with:
  - CASM attention module (Channel Attention + Spatial Attention)
  - Small‑target detection layer for fuzzy ore band boundaries
  - CIoU loss function for better localization
  - Mosaic‑9 data augmentation

The pipeline consists of:
1. **Imaging subsystem** (Basler acA2500‑14gc camera) capturing ore band images.
2. **Vision server** running the improved YOLOv5 model.
3. **PLC & servo actuator** moving the splitter based on detected coordinates.

## Requirements

- **Python** 3.8+
- **PyTorch** 1.10+ (with CUDA support recommended)
- **OpenCV** 4.5+
- **NumPy**, **Matplotlib**, **Pandas**
- **PySerial** (for PLC communication, optional)

All dependencies can be installed via:
```bash
pip install -r requirements.txt
```

## Installation

```bash
git clone https://github.com/Lynn201566/yolov5-pyqt5.git
cd yolov5-pyqt5
pip install -e .
```

## Dataset Preparation

1. **Collect images** from the spiral concentrator under different feed concentrations, lighting conditions, and ore types.  
2. **Annotate** the concentrate split point using bounding boxes (label format: YOLO `class x_center y_center width height`).  l.yaml` with your dataset paths and number of classes (only one class: `concentrate_split`).

## Training

Train the improved YOLOv5 model from scratch or fine‑tune a pretrained checkpoint:

```bash
python train.py --data data/spiral.yaml --cfg models/yolov5s_casm.yaml --weights yolov5s.pt --epochs 300 --batch-size 16 --img-size 640
```

Key arguments:
- `--cfg`: model configuration with CASM, small‑target layer, and CIoU loss.
- `--hyp`: optional hyperparameters (e.g., Mosaic‑9 enabled by default in the custom config).
- `--device`: GPU ID(s).

## Results (as reported in paper)

| Model             | Precision (%) | Recall (%) | FPS  | mAP@0.5 (%) |
|-------------------|---------------|------------|------|-------------|
| YOLOv5 (baseline) | 72.4          | 63.7       | 69   | 68.5        |
| YOLOv5‑SE         | 78.2          | 71.5       | 65   | 74.1        |
| YOLOv5‑CBAM       | 84.6          | 78.3       | 64   | 81.2        |
| YOLOv5‑CASM       |90.1           | 85.3       | 63   | 87.6        |

## Citation

If you use this code in your research, please cite the original paper:

```bibtex
@article{
  title={Investigation of adaptive interception systems for concentrate in spiral concentrators},
  author={Liu, Huizhong and Deng, Fulong and Zhou, Qihua and Long, Yao and Liu, Xixi and Zhang, Ruoyun and Ning, Jian}
}
```

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
