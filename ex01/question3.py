import math
import numpy as np
import matplotlib.pyplot as plt

def convert_to_radians(degrees):
    radians = math.radians(degrees)
    return radians

degrees_list = [0, 90, 180, 45, 30, 10, 5, 1]

print("cos,sin,radians,degrees")

for deg in degrees_list:
    rad = convert_to_radians(deg)
    
    s = math.sin(rad)
    c = math.cos(rad)
    
    print(f"{c},{s},{rad},{deg}")


# א. יצירת מטריצת סיבוב 30 מעלות
theta = math.radians(30)
r_30 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
print("Rotation Matrix (30 deg):\n", r_30)

# ב. מטריצת מתיחה פי 2 בציר ה-x
sx_2 = np.array([
    [2, 0],
    [0, 1]
])
print("\nScaling Matrix (x2):\n", sx_2)

# ג. חישוב rs (מתיחה ואז סיבוב)
rs = r_30 @ sx_2
print("\nRS Matrix (Scale then Rotate):\n", rs)

# ד. חישוב sr (סיבוב ואז מתיחה)
sr = sx_2 @ r_30
print("\nSR Matrix (Rotate then Scale):\n", sr)

# ה. יצירת מלבן ברוחב 2 וגובה 1 סביב הראשית
# קודקודים: (1, 0.5), (-1, 0.5), (-1, -0.5), (1, -0.5)
rectangle = np.array([
    [1, 0.5], [-1, 0.5], [-1, -0.5], [1, -0.5], [1, 0.5]
]).T # Transpose כדי שכל עמודה תהיה וקטור (x, y)

def plot_shape(shape, label, color):
    plt.plot(shape[0, :], shape[1, :], label=label, color=color)

plt.figure(figsize=(10, 8))

# ה. המלבן המקורי
plot_shape(rectangle, "Original", "black")

# ו. סיבוב המלבן
rect_rotated = r_30 @ rectangle
plot_shape(rect_rotated, "Rotated (r_30)", "blue")

# ז. מתיחת המלבן המקורי
rect_scaled = sx_2 @ rectangle
plot_shape(rect_scaled, "Scaled (sx_2)", "green")

# ח. הפעלת rs ו-sr
rect_rs = rs @ rectangle
rect_sr = sr @ rectangle

plot_shape(rect_rs, "RS (Scale then Rotate)", "red")
plot_shape(rect_sr, "SR (Rotate then Scale)", "orange")

# עיצוב הגרף
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)
plt.axis('equal')
plt.legend()
plt.title("Matrix Transformations on a Rectangle")
plt.grid(True, linestyle='--')
plt.show()