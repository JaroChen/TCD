# src/functions.py
def func1(x, y):
    return 7 * (x - 9)**4 + 3 * (y - 9)**2

def grad_func1(x, y):
    grad_x = 28 * (x - 9)**3
    grad_y = 6 * (y - 9)
    return np.array([grad_x, grad_y])

def func2(x, y):
    return max(x - 9, 0) + 3 * abs(y - 9)

def grad_func2(x, y):
    grad_x = 1 if x > 9 else 0
    grad_y = 3 * np.sign(y - 9)
    return np.array([grad_x, grad_y])
