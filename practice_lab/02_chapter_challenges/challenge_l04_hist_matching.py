# -*- coding: utf-8 -*-
"""
Challenge L4: Histogram Matching (Specification) from Scratch
-----------------------------------------------------------------------------
เขียนฟังก์ชันแมปฮิสโทแกรมของภาพอินพุตให้มีรูปแบบการแจกแจงตามภาพอ้างอิง (Reference Image)
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import cv2
import numpy as np

def histogram_matching(source_img, reference_img):
    # คำนวณ Normalized Histogram และ CDF ของภาพตั้งต้น
    hist_src, _ = np.histogram(source_img.flatten(), 256, [0, 256])
    cdf_src = hist_src.cumsum()
    cdf_src_norm = cdf_src / cdf_src.max()

    # คำนวณ CDF ของภาพอ้างอิง
    hist_ref, _ = np.histogram(reference_img.flatten(), 256, [0, 256])
    cdf_ref = hist_ref.cumsum()
    cdf_ref_norm = cdf_ref / cdf_ref.max()

    # สร้าง Lookup Table (LUT) จับคู่ค่าที่ใกล้เคียงที่สุด
    lut = np.zeros(256, dtype=np.uint8)
    for src_val in range(256):
        diff = np.abs(cdf_src_norm[src_val] - cdf_ref_norm)
        lut[src_val] = np.argmin(diff)

    return lut[source_img]

if __name__ == "__main__":
    src = np.random.randint(50, 120, (100, 100), dtype=np.uint8)
    ref = np.random.randint(150, 240, (100, 100), dtype=np.uint8)
    matched = histogram_matching(src, ref)
    print("✓ Challenge L4 (Histogram Matching) ทดสอบผ่าน: Shape =", matched.shape)
