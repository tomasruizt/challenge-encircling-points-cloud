from Circle import Circle
import matplotlib.pyplot as plt

import numpy as np
import vector_ops as v


def main():
    points = v.generate_random_points(seed=0)
    circle = Circle.guaranteed_to_encompass(points)

    curve = create_curve_for(circle)
    plt.scatter(*points.T)
    plt.plot(*curve)
    plt.savefig("encompassingCircle.svg")


def create_curve_for(circle: Circle) -> np.ndarray:
    t = np.linspace(0, 2*np.pi)
    unit_circle = np.array([np.sin(t), np.cos(t)])
    right_size_circle = unit_circle*circle.radius
    offset = circle.center_point.reshape((2, 1))
    return right_size_circle + offset


def load_example_points():
    import pandas as pd
    path = "./ex-data.json"
    return pd.read_json(path).values


if __name__ == '__main__':
    main()
