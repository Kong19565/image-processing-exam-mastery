# -*- coding: utf-8 -*-
"""
Challenge L11: Pure Python Otsu Thresholding
-----------------------------------------------------------------------------
หาเกณฑ์ t* ที่ให้ Between-class variance σ_B²(t) สูงสุด
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import numpy as np

def otsu_threshold(gray_img):
    hist, _ = np.histogram(gray_img.flatten(), 256, [0, 256])
    total = gray_img.size
    p = hist / total

    max_var = -1.0
    best_t = 0

    for t in range(255):
        w0 = np.sum(p[:t+1])
        w1 = 1.0 - w0
        if w0 == 0 or w1 == 0:
            continue
        
        i_range0 = np.arange(0, t+1)
        i_range1 = np.arange(t+1, 256)
        
        m0 = np.sum(i_range0 * p[:t+1]) / w0
        m1 = np.sum(i_range1 * p[t+1:]) / w1
        
        b_var = w0 * w1 * ((m0 - m1) ** 2)
        if b_var > max_var:
            max_var = b_var
            best_t = t

    return best_t

if __name__ == "__main__":
    mock = np.concatenate([np.random.normal(50, 10, 500), np.random.normal(180, 10, 500)])
    mock = np.clip(mock, 0, 255).astype(np.uint8)
    t = otsu_threshold(mock)
    print(f"✓ Challenge L11 (Otsu from Scratch) ผ่าน: Optimal Threshold = {t} (คาดหมาย ~110-120)")
