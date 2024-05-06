def gradient_descent(initial_x, initial_y, grad, alpha=0.01, num_iterations=100):
    x, y = initial_x, initial_y
    history = []
    for i in range(num_iterations):
        g = grad(x, y)
        x -= alpha * g[0]
        y -= alpha * g[1]
        history.append((x, y))
    return (x, y), history