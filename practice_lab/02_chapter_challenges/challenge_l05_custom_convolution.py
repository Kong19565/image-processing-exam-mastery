# -*- coding: utf-8 -*-
"""
Challenge L5: 2D Convolution & Unsharp Masking from Scratch
-----------------------------------------------------------------------------
เขียนฟังก์ชัน 2D Convolution โดยไม่อาศัย cv2.filter2D และทำ Unsharp Masking
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import numpy as np

def convolve2d(image, kernel):
    ih, iw = image.shape
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2

    # Zero padding
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    # Flip kernel 180 degrees for true convolution
    k_flipped = np.flip(np.flip(kernel, 0), 1)

    output = np.zeros_like(image, dtype=np.float32)
    for r in range(ih):
        for c in range(iw):
            region = padded[r:r+kh, c:c+kw]
            output[r, c] = np.sum(region * k_flipped)

    return output

def unsharp_mask(image, k=1.0):
    box = np.ones((3, 3), dtype=np.float32) / 9.0
    blurred = convolve2d(image, box)
    mask = image - blurred
    sharpened = image + k * mask
    return np.clip(sharpened, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    test_mat = np.random.randint(0, 256, (20, 20), dtype=np.uint8)
    res = unsharp_mask(test_mat, k=1.5)
    print("✓ Challenge L5 (Custom Convolution & Unsharp Mask) ผ่าน!")
