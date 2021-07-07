import cv2  # state of the art computer vision algorithms library
import numpy as np  # fundamental package for scientific computing
import matplotlib.pyplot as plt  # 2D plotting library producing publication quality figures
import pyrealsense2 as rs  # Intel RealSense cross-platform open-source API
import torch

def detect(pipe):
    while True:
        # Store next frameset for later processing:
        frame_present, frameset = pipe.try_wait_for_frames()
        if not frame_present:
            break

        color_frame = frameset.get_color_frame()
        depth_frame = frameset.get_depth_frame()
        print("Frames Captured")

        color = np.asanyarray(color_frame.get_data())
        plt.rcParams["axes.grid"] = False
        plt.rcParams['figure.figsize'] = [12, 6]
        plt.imshow(color)
        plt.show()

        colorizer = rs.colorizer()
        colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())
        plt.imshow(colorized_depth)
        plt.show()

