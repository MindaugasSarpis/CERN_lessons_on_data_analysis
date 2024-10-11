def solve_quad(a, b, c):
    D = b**2 - 4*a*c
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    return x1, x2