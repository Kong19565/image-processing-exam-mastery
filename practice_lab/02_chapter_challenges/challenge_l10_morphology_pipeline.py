# -*- coding: utf-8 -*-
"""
Challenge L10: Morphological Boundary Extraction β(A) = A - (A ⊖ B)
-----------------------------------------------------------------------------
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import numpy as np

def morphological_boundary(binary_img):
    # Structuring element 3x3
    pad = np.pad(binary_img, 1, mode='constant', constant_values=0)
    eroded = np.zeros_like(binary_img)
    
    # 3x3 Box erosion
    h, w = binary_img.shape
    for r in range(h):
        for c in range(w):
            sub = pad[r:r+3, c:c+3]
            if np.all(sub == 1):
                eroded[r, c] = 1

    boundary = binary_img - eroded
    return boundary

if __name__ == "__main__":
    test_blob = np.zeros((15, 15), dtype=np.uint8)
    test_blob[4:11, 4:11] = 1
    b = morphological_boundary(test_blob)
    assert b.sum() == (7*4 - 4), "เส้นรอบวงสี่เหลี่ยม 7x7 ต้องได้ 24 พิกเซล"
    print("✓ Challenge L10 (Morphological Boundary Extraction) ผ่าน!")
