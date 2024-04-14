
def quadratic_solver(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        solution1 = (-b + (discriminant ** 0.5)) / (2 * a)
        solution2 = (-b - (discriminant ** 0.5)) / (2 * a)
        return solution1, solution2

    elif discriminant == 0:
        solution = -b / (2 * a)
        return solution, solution

    else:
        return
