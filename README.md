# 🖼️ 310-3311 Image Processing Exam Mastery

[![GitHub Pages](https://img.shields.io/badge/Live-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://kong19565.github.io/image-processing-exam-mastery/)
[![Course](https://img.shields.io/badge/Course-310--3311%20Image%20Processing-blue?style=for-the-badge)](https://kong19565.github.io/image-processing-exam-mastery/)
[![Exam](https://img.shields.io/badge/Term-Final%20Exam%202026-orange?style=for-the-badge)](https://kong19565.github.io/image-processing-exam-mastery/)

> **Interactive Academic Preparation Hub & Exam Mastery Web Application for Digital Image Processing (การประมวลผลภาพดิจิทัล 310-3311)**
> ครอบคลุมเนื้อหาทั้ง 12 บทเรียน (Lectures 1–12) และแนวข้อสอบปฏิบัติการเสมือนจริง (Pre-Test Final Q1–Q4)

---

## 🌐 เข้าใช้งานเว็บแอปพลิเคชันออนไลน์
👉 **[คลิกที่นี่เพื่อเปิดใช้งาน Web Application ทันที](https://kong19565.github.io/image-processing-exam-mastery/)**
*(รองรับการใช้งานบนสมาร์ตโฟน แท็บเล็ต และคอมพิวเตอร์ ทำงานแบบ Client-side 100%)*

---

## 🚀 ฟังก์ชันเด่นในระบบ

### 1. 🧪 7 ห้องทดลองเสมือนจริง (Interactive Simulators)
1. **Point Ops & Histogram Equalizer (L4 & Q1):** ปรับค่า Contrast, Brightness, Gamma สดๆ พร้อมดูกราฟ s = T(r) และฮิสโทแกรม Before/After
2. **2D Spatial Convolution Sandbox (L5):** เลือก Kernel (Box, Gaussian, Sobel, Laplacian, Sharpen) คลิกพิกเซลดูขั้นตอนคูณและรวมผลทีละสเต็ป
3. **2D Fourier Spectrum & Notch Reject Filter (L6, L7 & Q4):** จำลอง Lowpass Filters (ILPF, BLPF, GLPF) และ Gaussian Notch Filter กำจัด Periodic Noise ในภาพ Dio
4. **Binary Morphology Sandbox (L10 & Q2, Q3):** ทดลองคำสั่ง Dilation, Erosion, Opening, Closing และ Boundary Extraction
5. **Otsu Threshold Calculator (L11):** คำนวณความแปรปรวนระหว่างกลุ่ม σ_B²(t) หาค่าขีดแบ่งที่ดีที่สุด t*
6. **GLCM Texture Matrix & Haralick Features (L12):** นับคู่พิกเซลมุม 0°, 45°, 90°, 135° คำนวณ Contrast, Homogeneity, ASM, Entropy
7. **Confusion Matrix & Metrics Evaluator (L10):** คำนวณ Accuracy, Precision, Recall, F1-Score และ IoU

### 2. ⏱️ ระบบจำลองสอบจับเวลาจริง (Timed Mock Exam Simulator)
- คลังข้อสอบ **72 ข้อ** สุ่มข้อสอบและสลับตัวเลือก
- ตั้งเวลาสอบถอยหลังจริง พร้อมระบบปักหมุดข้อที่ต้องการทบทวน
- ตรวจผลพร้อมตัดเกรด A ถึง F และวิเคราะห์ความแม่นยำแยกตามบทเรียน (Topic Mastery Breakdown)

### 3. 💻 คู่มือเจาะลึกข้อสอบแล็บปฏิบัติการ (Pre-Test Q1–Q4)
- **Q1:** Intensity Transformation เผยวัตถุในท้องฟ้า + กราฟฮิสโทแกรม
- **Q2:** Invariant Barcode Detection (ทนทานต่อการหมุน 180° และ Translation)
- **Q3:** Green Sign Detection ด้วย HSV + Morphology
- **Q4:** Periodic Noise Removal ด้วย 2D Fourier & Gaussian Notch Filter

---

## 📦 ดาวน์โหลดชุดฝึกปฏิบัติการ Python
- ดาวน์โหลดชุดแบบฝึกหัดพร้อมไฟล์ภาพทดสอบ: **[downloads/practice_lab.zip](downloads/practice_lab.zip)**
- สั่งรันชุดตรวจคำตอบอัตโนมัติ:
  ```bash
  python practice_lab/run_all.py
  ```

---

*จัดทำขึ้นเพื่อการเตรียมความพร้อมสอบปลายภาควิชา Digital Image Processing (310-3311)*
