import cv2  # state of the art computer vision algorithms library
import numpy as np  # fundamental package for scientific computing
import matplotlib.pyplot as plt  # 2D plotting library producing publication quality figures
import pyrealsense2 as rs  # Intel RealSense cross-platform open-source API
import torch

from continueDetection import detecft

print("Environment Ready")

# Setup:
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_device_from_file(r"C:\Users\14074\Documents\transitionin_with_RGB.bag")
profile = pipe.start(cfg)

detect(pipe)


