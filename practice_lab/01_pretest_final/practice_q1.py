# -*- coding: utf-8 -*-
"""
โจทย์ฝึกซ้อม ข้อ 1: Intensity Transformation (การปรับระดับความเข้มสี)
-----------------------------------------------------------------------------
สถานการณ์: ภาพท้องฟ้ามีเครื่องบินซ่อนอยู่ซึ่งกลืนไปกับความสว่างจัดของพื้นหลัง
คำสั่ง:
1. เขียนโปรแกรมปรับระดับความเข้มสี (s = a*r + b) โดย 'ลด Contrast' และ 'เพิ่ม Brightness'
2. บันทึกภาพผลลัพธ์เป็น "Result1.png"
3. บันทึกฮิสโทแกรมก่อนประมวลผลเป็น "Result1-Hist-Before.png"
4. บันทึกฮิสโทแกรมหลังประมวลผลเป็น "Result1-Hist-After.png"
5. อย่าลืมเขียน Comment ภาษาไทยอธิบายทุกขั้นตอน!
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# เส้นทางไฟล์
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_IMAGE = os.path.join(CURRENT_DIR, "..", "test_images", "Q1-1.jpg")

OUT_IMAGE = os.path.join(CURRENT_DIR, "Result1.png")
OUT_HIST_BEFORE = os.path.join(CURRENT_DIR, "Result1-Hist-Before.png")
OUT_HIST_AFTER = os.path.join(CURRENT_DIR, "Result1-Hist-After.png")

def main():
    # ขั้นตอนที่ 1: อ่านภาพต้นฉบับ
    img = cv2.imread(TEST_IMAGE)
    if img is None:
        print(f"Error: ไม่พบไฟล์ภาพที่ {TEST_IMAGE}")
        return

    # TODO: บันทึกฮิสโทแกรมก่อนประมวลผล (Result1-Hist-Before.png)
    plt.figure()
    plt.hist(img.ravel(), 256, [0, 256], color="steelblue")
    plt.title("Histogram Before Processing")
    plt.xlabel("Intensity Level")
    plt.ylabel("Pixel Count")
    plt.savefig(OUT_HIST_BEFORE)
    plt.close()
    print("บันทึก Result1-Hist-Before.png เรียบร้อย")

    # TODO: ปรับระดับความเข้มสีเพื่อลด Contrast และเพิ่ม Brightness
    # คำใบ้:
    # 1. แปลงเป็น float32 เพื่อป้องกัน overflow
    # 2. ลด Contrast: เลือกความชัน 0 < a < 1 (เช่น a = 0.55)
    # 3. เพิ่ม Brightness: บวกค่าคงที่ b > 0 (เช่น b = 80)
    # 4. ตัดขอบเขตด้วย np.clip(..., 0, 255).astype(np.uint8)
    
    img_float = img.astype(np.float32)
    a = 0.55   # ค่าความชัน (ลด Contrast)
    b = 85.0   # ค่าชดเชยความสว่าง (เพิ่ม Brightness)
    
    result = np.clip(a * img_float + b, 0, 255).astype(np.uint8)

    # TODO: บันทึกภาพผลลัพธ์ Result1.png
    cv2.imwrite(OUT_IMAGE, result)
    print("บันทึก Result1.png เรียบร้อย")

    # TODO: บันทึกฮิสโทแกรมหลังประมวลผล (Result1-Hist-After.png)
    plt.figure()
    plt.hist(result.ravel(), 256, [0, 256], color="crimson")
    plt.title("Histogram After Processing")
    plt.xlabel("Intensity Level")
    plt.ylabel("Pixel Count")
    plt.savefig(OUT_HIST_AFTER)
    plt.close()
    print("บันทึก Result1-Hist-After.png เรียบร้อย")

if __name__ == "__main__":
    main()
