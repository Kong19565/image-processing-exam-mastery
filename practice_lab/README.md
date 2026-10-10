# 310-3311 Image Processing - Final Exam Practice Lab

ยินดีต้อนรับสู่ชุดไฟล์แบบฝึกหัดสำหรับเตรียมความพร้อมสอบปลายภาควิชา **310-3311 การประมวลผลภาพดิจิทัล**

---

## 📁 โครงสร้างโฟลเดอร์

```
practice_lab/
├── test_images/                 # ไฟล์ภาพทดสอบจริงจากระบบสอบ (Q1-1, Q2-1, Q2-2, Q3-2, Q4-NoisyDio)
├── 01_pretest_final/           # ชุดข้อสอบเสมือนจริง 4 ข้อหลักตามแนว Pre-Test Final
│   ├── practice_q1.py          # สคริปต์ฝึกทำข้อ 1 (Intensity Transformation)
│   ├── practice_q2.py          # สคริปต์ฝึกทำข้อ 2 (Invariant Barcode Detection)
│   ├── practice_q3.py          # สคริปต์ฝึกทำข้อ 3 (Green Sign Detection)
│   ├── practice_q4.py          # สคริปต์ฝึกทำข้อ 4 (Periodic Noise Removal)
│   ├── solution_q*_annotated.py# เฉลยละเอียดพร้อม Comment ภาษาไทยทุกสเต็ป
│   └── test_runner_pretest.py  # ระบบตรวจคำตอบอัตโนมัติ
├── 02_chapter_challenges/      # ชุดโจทย์เพิ่มเติมครอบคลุมเนื้อหาสำคัญ
│   ├── challenge_l04_hist_matching.py      # Histogram Specification
│   ├── challenge_l05_custom_convolution.py # 2D Convolution & Unsharp Mask
│   ├── challenge_l06_fourier_notch.py      # 2D FFT & GLPF Filter
│   ├── challenge_l09_canny_harris.py       # Harris Corner Response
│   ├── challenge_l10_morphology_pipeline.py# Morphological Boundary Extraction
│   ├── challenge_l11_otsu_segmentation.py  # Pure Python Otsu's Thresholding
│   ├── challenge_l12_glcm_features.py      # GLCM Matrix & Haralick Features
│   └── test_runner_challenges.py           # ตัวตรวจผลโจทย์ท้าทาย
└── run_all.py                  # คำสั่งเดียวรันตรวจผลลัพธ์ทั้งหมด
```

---

## 🚀 วิธีการฝึกซ้อม

1. **เปิดไฟล์ใน `01_pretest_final/`** เช่น `practice_q1.py` ใน VS Code หรือ IDE ที่คุณใช้งาน
2. **ลองเขียนโค้ดตามคำสั่งในโจทย์** โดยปฏิบัติตามกฎเหล็ก:
   - บันทึกไฟล์ผลลัพธ์ตามชื่อที่กำหนด เช่น `Result1.png`
   - เขียน Comment ภาษาไทยอธิบายขั้นตอนทุกสเต็ป
   - ค่า Binary Mask ต้องเป็น 0 และ 255 อย่างเคร่งครัด
3. **สั่งรันโค้ดและตรวจผลลัพธ์**:
   ```bash
   python test_runner_pretest.py
   ```
4. **เปิดดูเว็บแอปพลิเคชันแบบอินเทอร์แอคทีฟ**:
   ดับเบิลคลิกไฟล์ `Image_Processing_Final_Exam_Prep.html` ที่อยู่ในโฟลเดอร์หลัก เพื่อทบทวนทฤษฎีและทำข้อสอบจำลองจับเวลา
