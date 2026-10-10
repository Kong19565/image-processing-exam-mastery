# -*- coding: utf-8 -*-
"""
Automated Test Runner for 02_chapter_challenges
รันและตรวจสอบผลการทำงานของชุดโจทย์ท้าทายประจำบทเรียนทั้งหมด
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import subprocess
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
scripts = [
    "challenge_l04_hist_matching.py",
    "challenge_l05_custom_convolution.py",
    "challenge_l06_fourier_notch.py",
    "challenge_l09_canny_harris.py",
    "challenge_l10_morphology_pipeline.py",
    "challenge_l11_otsu_segmentation.py",
    "challenge_l12_glcm_features.py"
]

def run_all_challenges():
    print("==================================================")
    print("เริ่มการทดสอบ Chapter Challenges (L4 - L12)")
    print("==================================================")
    passed = 0
    for s in scripts:
        path = os.path.join(CURRENT_DIR, s)
        res = subprocess.run([sys.executable, path], capture_output=True, text=True, encoding='utf-8')
        if res.returncode == 0:
            print(f"✓ {s}: ผ่านสำเร็จ!")
            passed += 1
        else:
            print(f"✗ {s}: ล้มเหลว! Error: {res.stderr[:200]}")

    print("==================================================")
    print(f"สรุปผลการทดสอบ: ผ่าน {passed}/{len(scripts)} ข้อ")
    print("==================================================")

if __name__ == "__main__":
    run_all_challenges()
