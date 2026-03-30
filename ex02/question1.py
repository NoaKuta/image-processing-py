import numpy as np

def matrix_translation(a, b):
    return np.array([
        [1, 0, a],
        [0, 1, b],
        [0, 0, 1]
    ])

    import numpy as np
import matplotlib.pyplot as plt

# פונקציות עזר (בנינו קודם)
def matrix_translation(a, b):
    return np.array([[1, 0, a], [0, 1, b], [0, 0, 1]])

def matrix_rotation(theta_deg):
    theta = np.radians(theta_deg)
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

def matrix_scale(sx, sy=None):
    if sy is None: sy = sx
    return np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

# הגדרת קודקודי המלבן (הומוגני - עם 1 בסוף)
# הוספנו את הנקודה הראשונה שוב בסוף כדי "לסגור" את הצורה בציור
rectangle = np.array([
    [1, 0.5, 1],
    [-1, 0.5, 1],
    [-1, -0.5, 1],
    [1, -0.5, 1],
    [1, 0.5, 1] 
]).T # אנחנו עושים Transpose כדי שכל עמודה תהיה נקודה

# חישוב המטריצות לסעיפים ג' ו-ד'
R45 = matrix_rotation(45)
S2 = matrix_scale(2, 1)

# מטריצה לסעיף ג': סיבוב ואז מתיחה
M_c = S2 @ R45 

# מטריצה לסעיף ד': מתיחה ואז סיבוב
M_d = R45 @ S2

# פונקציה להצגת התוצאות
def plot_rect(rect, title, subplot_pos):
    plt.subplot(2, 2, subplot_pos)
    plt.plot(rect[0, :], rect[1, :], 'b-o')
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)

plt.figure(figsize=(10, 8))

# א. המלבן המקורי
plot_rect(rectangle, "Original", 1)

# ב. סיבוב ב-30 מעלות
rect_b = matrix_rotation(30) @ rectangle
plot_rect(rect_b, "Rotate 30", 2)

# ג. סיבוב 45 ואז מתיחה
rect_c = M_c @ rectangle
plot_rect(rect_c, "Rotate 45 then Scale X", 3)

# ד. מתיחה ואז סיבוב 45
rect_d = M_d @ rectangle
plot_rect(rect_d, "Scale X then Rotate 45", 4)

plt.tight_layout()
plt.show()


#שאלה 3
def nearest_neighbor(alpha, beta, I00, I01, I10, I11):
    # עיגול הקואורדינאטות למציאת השכן הקרוב ביותר
    # 0.5 ומעלה יתעגל ל-1, פחות מ-0.5 יתעגל ל-0
    rounded_alpha = int(alpha + 0.5)
    rounded_beta = int(beta + 0.5)
    
    if rounded_beta == 0:
        return I00 if rounded_alpha == 0 else I01
    else:
        return I10 if rounded_alpha == 0 else I11
    
def bilinear_interpolation(alpha, beta, I00, I01, I10, I11):
    # חישוב המשקלים עבור כל פיקסל
    w00 = (1 - alpha) * (1 - beta)
    w01 = alpha * (1 - beta)
    w10 = (1 - alpha) * beta
    w11 = alpha * beta
    
    # סכימת הערכים המשוקללים
    return w00 * I00 + w01 * I01 + w10 * I10 + w11 * I11