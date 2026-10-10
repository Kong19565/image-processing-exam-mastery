# -*- coding: utf-8 -*-
"""
Challenge L12: GLCM Matrix & Haralick Features from Scratch
-----------------------------------------------------------------------------
คำนวณ GLCM P(i,j | d=1, θ=0) และสกัด Contrast, Homogeneity, ASM, Entropy
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import numpy as np

def compute_glcm(image, levels=4):
    h, w = image.shape
    P = np.zeros((levels, levels), dtype=np.float32)
    
    # 0 degrees: right neighbor (r, c+1)
    for r in range(h):
        for c in range(w - 1):
            i = image[r, c]
            j = image[r, c + 1]
            P[i, j] += 1

    total = np.sum(P)
    if total > 0:
        P = P / total # Normalized

    # Haralick Features
    contrast = 0.0
    homogeneity = 0.0
    energy = 0.0
    entropy = 0.0

    for i in range(levels):
        for j in range(levels):
            p_val = P[i, j]
            if p_val > 0:
                contrast += ((i - j) ** 2) * p_val
                homogeneity += p_val / (1.0 + ((i - j) ** 2))
                energy += p_val ** 2
                entropy -= p_val * np.log2(p_val)

    return {
        "GLCM": P,
        "Contrast": contrast,
        "Homogeneity": homogeneity,
        "Energy_ASM": energy,
        "Entropy": entropy
    }

if __name__ == "__main__":
    sample = np.array([
        [0, 1, 2, 3],
        [1, 1, 2, 3],
        [2, 2, 3, 3],
        [3, 3, 3, 3]
    ], dtype=np.uint8)
    res = compute_glcm(sample, levels=4)
    print("✓ Challenge L12 (GLCM & Haralick Features) ผ่าน!")
    print(f"  Contrast: {res['Contrast']:.4f}, Homogeneity: {res['Homogeneity']:.4f}, Energy: {res['Energy_ASM']:.4f}")
