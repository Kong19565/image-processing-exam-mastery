# -*- coding: utf-8 -*-
"""
Automated Test Runner for 01_pretest_final
ตรวจสอบความถูกต้อง ขนาดไฟล์ และชนิดข้อมูลของไฟล์ผลลัพธ์
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import os
import cv2
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def test_all():
    print("==================================================")
    print("เริ่มการตรวจสอบผลลัพธ์ข้อสอบ Pre-Test Final (Q1 - Q4)")
    print("==================================================")

    # Test Q1
    q1_img = os.path.join(CURRENT_DIR, "Result1.png")
    q1_hb = os.path.join(CURRENT_DIR, "Result1-Hist-Before.png")
    q1_ha = os.path.join(CURRENT_DIR, "Result1-Hist-After.png")

    if os.path.exists(q1_img) and os.path.exists(q1_hb) and os.path.exists(q1_ha):
        im = cv2.imread(q1_img)
        print(f"✓ ข้อ 1 ผ่าน: สร้าง Result1.png ขนาด {im.shape} และกราฟฮิสโทแกรมครบถ้วน")
    else:
        print("✗ ข้อ 1 ยังไม่ผ่าน: ไม่พบไฟล์ผลลัพธ์ครบ 3 ไฟล์")

    # Test Q2
    q2_1 = os.path.join(CURRENT_DIR, "Result2-1.png")
    q2_2 = os.path.join(CURRENT_DIR, "Result2-2.png")
    if os.path.exists(q2_1) and os.path.exists(q2_2):
        im1 = cv2.imread(q2_1, cv2.IMREAD_GRAYSCALE)
        im2 = cv2.imread(q2_2, cv2.IMREAD_GRAYSCALE)
        u1 = np.unique(im1)
        u2 = np.unique(im2)
        if set(u1).issubset({0, 255}) and set(u2).issubset({0, 255}):
            print(f"✓ ข้อ 2 ผ่าน: Result2-1 และ Result2-2 เป็น Binary Mask (0, 255) ถูกต้อง")
        else:
            print(f"⚠️ ข้อ 2 คำเตือน: พบค่าสีที่ไม่ใช่ 0 หรือ 255 ในภาพ ({u1})")
    else:
        print("✗ ข้อ 2 ยังไม่ผ่าน: ไม่พบไฟล์ Result2-1.png หรือ Result2-2.png")

    # Test Q3
    q3 = os.path.join(CURRENT_DIR, "Result3.png")
    if os.path.exists(q3):
        im3 = cv2.imread(q3, cv2.IMREAD_GRAYSCALE)
        u3 = np.unique(im3)
        if set(u3).issubset({0, 255}):
            print(f"✓ ข้อ 3 ผ่าน: Result3.png เป็น Binary Mask (0, 255) ถูกต้อง")
        else:
            print(f"⚠️ ข้อ 3 คำเตือน: พบค่าสีที่ไม่ใช่ 0 หรือ 255 ({u3})")
    else:
        print("✗ ข้อ 3 ยังไม่ผ่าน: ไม่พบไฟล์ Result3.png")

    # Test Q4
    q4 = os.path.join(CURRENT_DIR, "Result4.png")
    if os.path.exists(q4):
        im4 = cv2.imread(q4, cv2.IMREAD_GRAYSCALE)
        print(f"✓ ข้อ 4 ผ่าน: Result4.png ขนาด {im4.shape} ถูกสร้างเรียบร้อย")
    else:
        print("✗ ข้อ 4 ยังไม่ผ่าน: ไม่พบไฟล์ Result4.png")

    print("==================================================")

if __name__ == "__main__":
    test_all()
