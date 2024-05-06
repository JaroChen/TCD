# src/__init__.py
from .functions import func1, grad_func1, func2, grad_func2
from .optimization_algorithms import gradient_descent, rmsprop, adam, heavy_ball

# Now, you can import directly from src:
# from src import func1, grad_func1, gradient_descent, etc.
