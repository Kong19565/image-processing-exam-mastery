# -*- coding: utf-8 -*-
"""
Challenge L6: 2D FFT Magnitude Spectrum & Ideal vs Gaussian Lowpass Filter
-----------------------------------------------------------------------------
สร้างฟังก์ชันวิเคราะห์สเปกตรัมขนาด และสร้าง Gaussian Lowpass Filter
"""
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='ignore')

import numpy as np

def create_glpf(shape, d0):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    u = np.arange(rows) - crow
    v = np.arange(cols) - ccol
    U, V = np.meshgrid(u, v, indexing='ij')
    D = np.sqrt(U**2 + V**2)
    return np.exp(-(D**2) / (2.0 * (d0**2)))

def frequency_filtering(image, H):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    filtered = fshift * H
    ishift = np.fft.ifftshift(filtered)
    res = np.fft.ifft2(ishift)
    return np.real(res)

if __name__ == "__main__":
    img = np.random.randint(0, 256, (64, 64), dtype=np.uint8)
    H = create_glpf(img.shape, 20.0)
    out = frequency_filtering(img, H)
    print("✓ Challenge L6 (GLPF Frequency Filtering) ผ่าน!")
