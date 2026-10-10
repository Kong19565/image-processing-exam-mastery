# -*- coding: utf-8 -*-
"""
โจทย์ฝึกซ้อม ข้อ 2: Invariant Barcode Detection
-----------------------------------------------------------------------------
สถานการณ์: เครื่องสแกนตั๋ว Boarding Pass อาจพบปัญหาตั๋วหมุนกลับด้าน 180° หรือเลื่อนตำแหน่ง
คำสั่ง:
1. พัฒนา Algorithm ระบุบริเวณ Barcode ที่ทนทานต่อ Translation และการหมุน 180°
2. ผลลัพธ์แสดง Barcode ด้วยสีขาว (255) และส่วนอื่นด้วยสีดำ (0)
3. บันทึกผลลัพธ์เป็น "Result2-1.png" และ "Result2-2.png"
4. เขียน Comment ภาษาไทยอธิบายขั้นตอนอย่างละเอียด
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import cv2
import numpy as np
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_1 = os.path.join(CURRENT_DIR, "..", "test_images", "Q2-1.png")
IMAGE_2 = os.path.join(CURRENT_DIR, "..", "test_images", "Q2-2.png")

def detect_barcode(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: ไม่พบภาพ {image_path}")
        return

    # ขั้นตอนที่ 1: แปลงเป็น Grayscale และเกาส์เซียนเบลอเล็กน้อย
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # ขั้นตอนที่ 2: หา Horizontal Gradient ด้วย Scharr/Sobel X
    # เส้นบาร์โค้ดแนวตั้งเมื่อหมุน 180° ก็ยังคงเป็นแนวตั้งเดิม ทำให้ Sobel X ตอบสนองเสมอ (Invariant)
    gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = cv2.convertScaleAbs(gradX)

    # ขั้นตอนที่ 3: ทำ Thresholding และ Morphological Closing ในแนวนอน
    _, thresh = cv2.threshold(gradX, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Kernel แนวนอนเชื่อมเส้นบาร์โค้ดแต่ละเส้นเข้าด้วยกัน
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=2)
    closed = cv2.dilate(closed, None, iterations=2)

    # ขั้นตอนที่ 4: หา Contours และคัดเลือกพื้นที่บาร์โค้ด
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    mask = np.zeros(gray.shape, dtype=np.uint8)
    if contours:
        # เลือก Contour ที่มีพื้นที่สอดคล้องกับบาร์โค้ด
        c = max(contours, key=cv2.contourArea)
        cv2.drawContours(mask, [c], -1, 255, thickness=-1)

    cv2.imwrite(output_path, mask)
    print(f"บันทึกผลลัพธ์ {os.path.basename(output_path)} เรียบร้อย")

def main():
    detect_barcode(IMAGE_1, os.path.join(CURRENT_DIR, "Result2-1.png"))
    detect_barcode(IMAGE_2, os.path.join(CURRENT_DIR, "Result2-2.png"))

if __name__ == "__main__":
    main()
