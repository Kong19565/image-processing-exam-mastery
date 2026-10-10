# -*- coding: utf-8 -*-
"""
โจทย์ฝึกซ้อม ข้อ 4: Noise Removal on Dio Image (การกำจัดสัญญาณรบกวนคาบเวลา)
-----------------------------------------------------------------------------
สถานการณ์: ภาพตัวละคร Dio มีทั้ง Salt-and-Pepper Noise และ Periodic Noise (ลายทาง)
คำสั่ง:
1. กำจัดสัญญาณรบกวนทั้งสองชนิดโดยคงรายละเอียดลายเส้นของภาพไว้
2. บันทึกผลลัพธ์เป็น "Result4.png"
3. เขียน Comment ภาษาไทยอธิบายขั้นตอนอย่างละเอียด
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import cv2
import numpy as np
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_IMAGE = os.path.join(CURRENT_DIR, "..", "test_images", "Q4-NoisyDio.png")
OUT_IMAGE = os.path.join(CURRENT_DIR, "Result4.png")

def main():
    img = cv2.imread(TEST_IMAGE, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: ไม่พบภาพ {TEST_IMAGE}")
        return

    # ขั้นตอนที่ 1: กำจัด Impulse / Salt-and-Pepper Noise ด้วย Median Filter
    denoised_med = cv2.medianBlur(img, 3)

    # ขั้นตอนที่ 2: แปลงสู่โดเมนความถี่ด้วย 2D Fast Fourier Transform (FFT)
    f = np.fft.fft2(denoised_med.astype(np.float32))
    fshift = np.fft.fftshift(f)

    # ขั้นตอนที่ 3: สร้าง Gaussian Notch Reject Filter
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    
    # พิกัดของคู่ Noise Spikes ที่พบในภาพ Dio
    notches = [
        (47, 47), (-47, -47),
        (94, 94), (-94, -94)
    ]
    
    d0 = 12.0  # รัศมีของ Notch
    H = np.ones((rows, cols), dtype=np.float32)
    
    u = np.arange(rows) - crow
    v = np.arange(cols) - ccol
    U, V = np.meshgrid(u, v, indexing='ij')

    for (uk, vk) in notches:
        Dk = np.sqrt((U - uk)**2 + (V - vk)**2)
        H = H * (1.0 - np.exp(-(Dk**2) / (2.0 * (d0**2))))

    # ขั้นตอนที่ 4: คูณสเปกตรัมด้วย Filter และแปลงกลับ (IFFT)
    fshift_filtered = fshift * H
    f_ishift = np.fft.ifftshift(fshift_filtered)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.real(img_back)

    # ขั้นตอนที่ 5: ปรับความคมชัดและช่วงสี (Contrast & Clip)
    res = np.clip(img_back, 0, 255).astype(np.uint8)

    cv2.imwrite(OUT_IMAGE, res)
    print(f"บันทึกผลลัพธ์ {os.path.basename(OUT_IMAGE)} เรียบร้อย")

if __name__ == "__main__":
    main()
