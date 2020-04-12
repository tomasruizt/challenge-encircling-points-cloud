from typing import Tuple

import numpy as np


def generate_random_points(seed: int = 0) -> np.ndarray:
    dims, num_points = 2, 60
    np.random.seed(seed)
    return np.random.randint(low=-15, high=15, size=(num_points, dims))


def find_most_distant(pts, x):
    """O(n)"""
    ds = [distance(p, x) for p in pts]
    return pts[np.argmax(ds)].reshape(x.shape)


def find_most_distant_point_pair(pts) -> Tuple[np.ndarray, np.ndarray]:
    """O(n)"""
    mean = np.mean(pts, axis=0)
    p1 = find_most_distant(pts, mean)
    p2 = find_most_distant(pts, p1)
    return p1, p2


def distance(e1, e2) -> float:
    """Euclidean distance in R^2"""
    return np.linalg.norm(np.subtract(e1, e2))

