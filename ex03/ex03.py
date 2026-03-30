import cv2
import numpy as np
import sys

def calculate_colors(r, g, b):
    r_n, g_n, b_n = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r_n, g_n, b_n)
    cmin = min(r_n, g_n, b_n)
    diff = cmax - cmin

    # --- HSV ---
 
    h = 0
    if diff != 0:
        if cmax == r_n: h = (60 * ((g_n - b_n) / diff) + 360) % 360
        elif cmax == g_n: h = (60 * ((b_n - r_n) / diff) + 120) % 360
        elif cmax == b_n: h = (60 * ((r_n - g_n) / diff) + 240) % 360
    
    s_hsv = 0 if cmax == 0 else (diff / cmax)
    v = cmax
    
    pixel = np.uint8([[[b, g, r]]])
    hsv_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]

    # --- HSL ---
    l = (cmax + cmin) / 2
    s_hsl = 0 if diff == 0 else diff / (1 - abs(2 * l - 1))
    
    hls_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HLS)[0][0]

    # ---  YCrCb ---
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cr = (r - y) * 0.713 + 128
    cb = (b - y) * 0.564 + 128
    
    ycrcb_cv = cv2.cvtColor(pixel, cv2.COLOR_BGR2YCrCb)[0][0]

    print(f"\nResults for RGB({r}, {g}, {b}):")
    print("-" * 30)
    print(f"HSV Manual: H={h:.2f}°, S={s_hsv:.2f}, V={v:.2f}")
    print(f"HSV OpenCV: H={hsv_cv[0]}, S={hsv_cv[1]}, V={hsv_cv[2]}")
    print("-" * 30)
    print(f"HSL Manual: H={h:.2f}°, S={s_hsl:.2f}, L={l:.2f}")
    print(f"HSL OpenCV: H={hls_cv[0]}, L={hls_cv[1]}, S={hls_cv[2]}")
    print("-" * 30)
    print(f"YCrCb Manual: Y={y:.2f}, Cr={cr:.2f}, Cb={cb:.2f}")
    print(f"YCrCb OpenCV: Y={ycrcb_cv[0]}, Cr={ycrcb_cv[1]}, Cb={ycrcb_cv[2]}")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        r_in = int(sys.argv[1])
        g_in = int(sys.argv[2])
        b_in = int(sys.argv[3])
        calculate_colors(r_in, g_in, b_in)