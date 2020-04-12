import numpy as np
import vector_ops as v


class Circle:

    def __init__(self, center_point, radius):
        self.center_point = center_point
        self.radius = radius

    @staticmethod
    def guaranteed_to_encompass(points):
        """Proof of the encompassing guarantee in Analysis.ipynb"""

        pair = v.find_most_distant_point_pair(points)
        circle = Circle._smallest_that_contains(*pair)  # no guarantee to contain all points

        circle_with_guarantee = Circle(
            radius=v.distance(circle.center_point, v.find_most_distant(points, circle.center_point)),
            center_point=circle.center_point
        )
        return circle_with_guarantee

    @staticmethod
    def _smallest_that_contains(p1, p2):
        center_point = np.multiply(p1, 0.5) + np.multiply(p2, 0.5)
        radius = v.distance(p1, p2)
        return Circle(center_point, radius)
