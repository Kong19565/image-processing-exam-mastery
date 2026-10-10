# -*- coding: utf-8 -*-
"""
Challenge L9: Harris Corner Response Function R from Scratch
-----------------------------------------------------------------------------
คำนวณ Harris Response R = det(M) - k*(trace(M))^2
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import numpy as np

def harris_response(img_gray, k=0.04):
    # เกรเดียนต์แกน X และ Y ด้วย Sobel แบบง่าย [-1, 0, 1]
    Ix = np.zeros_like(img_gray, dtype=np.float32)
    Iy = np.zeros_like(img_gray, dtype=np.float32)
    Ix[:, 1:-1] = (img_gray[:, 2:].astype(np.float32) - img_gray[:, :-2].astype(np.float32)) / 2.0
    Iy[1:-1, :] = (img_gray[2:, :].astype(np.float32) - img_gray[:-2, :].astype(np.float32)) / 2.0

    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    # Gaussian weighting หรือ Box filter 3x3
    det_M = (Ixx * Iyy) - (Ixy * Ixy)
    trace_M = Ixx + Iyy
    R = det_M - k * (trace_M ** 2)
    return R

if __name__ == "__main__":
    mat = np.zeros((30, 30), dtype=np.uint8)
    mat[10:20, 10:20] = 255 # สี่เหลี่ยมสีขาวตรงกลาง มี 4 มุม
    R = harris_response(mat)
    print("✓ Challenge L9 (Harris Corner Response) ผ่าน: Min R =", R.min(), "Max R =", R.max())
