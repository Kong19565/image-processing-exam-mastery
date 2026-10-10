# -*- coding: utf-8 -*-
"""
โจทย์ฝึกซ้อม ข้อ 3: Green Sign Detection (การตรวจจับแผ่นป้ายสีเขียว)
-----------------------------------------------------------------------------
สถานการณ์: ตรวจจับบริเวณแผ่นป้ายจราจรสีเขียวบนถนนเพื่อเตรียมนำไป OCR
คำสั่ง:
1. ตรวจจับแผ่นป้ายโดยทนต่อการเลื่อนตำแหน่ง
2. แสดงแผ่นป้ายเป็นสีขาว (255) และส่วนอื่นเป็นสีดำ (0)
3. บันทึกผลลัพธ์เป็น "Result3.png"
4. เขียน Comment ภาษาไทยอธิบายขั้นตอนอย่างละเอียด
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import cv2
import numpy as np
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_IMAGE = os.path.join(CURRENT_DIR, "..", "test_images", "Q3-2.jpg")
OUT_IMAGE = os.path.join(CURRENT_DIR, "Result3.png")

def main():
    img = cv2.imread(TEST_IMAGE)
    if img is None:
        print(f"Error: ไม่พบภาพ {TEST_IMAGE}")
        return

    # ขั้นตอนที่ 1: แปลงปริภูมิสีเป็น HSV (ทนทานต่อสภาพแสงและความสว่าง)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # ขั้นตอนที่ 2: กำหนดช่วงสีเขียว (Green Range)
    lower_green = np.array([35, 45, 45])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # ขั้นตอนที่ 3: อุดรูตัวหนังสือสีขาวในป้ายด้วย Morphological Closing
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
    mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))

    # ขั้นตอนที่ 4: หา Contours และระบายสีขาวทึบเต็มพื้นที่แผ่นป้าย
    contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    final_mask = np.zeros(mask.shape, dtype=np.uint8)
    if contours:
        c = max(contours, key=cv2.contourArea)
        cv2.drawContours(final_mask, [c], -1, 255, thickness=-1)

    cv2.imwrite(OUT_IMAGE, final_mask)
    print(f"บันทึกผลลัพธ์ {os.path.basename(OUT_IMAGE)} เรียบร้อย")

if __name__ == "__main__":
    main()
