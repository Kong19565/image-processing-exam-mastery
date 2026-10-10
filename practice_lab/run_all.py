# -*- coding: utf-8 -*-
"""
Master Test Runner: รันแบบทดสอบทั้งหมดใน practice_lab
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import subprocess
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    print("##################################################")
    print("   310-3311 Image Processing Lab Suite Runner")
    print("##################################################\n")

    # 1. Run Pretest Runner
    p1 = os.path.join(CURRENT_DIR, "01_pretest_final", "test_runner_pretest.py")
    subprocess.run([sys.executable, p1])

    print("\n")
    # 2. Run Challenges Runner
    p2 = os.path.join(CURRENT_DIR, "02_chapter_challenges", "test_runner_challenges.py")
    subprocess.run([sys.executable, p2])

    print("\n🎉 ทดสอบระบบปฏิบัติการทั้งหมดเรียบร้อยแล้ว!")

if __name__ == "__main__":
    main()
