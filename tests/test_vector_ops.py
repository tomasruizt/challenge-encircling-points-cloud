import numpy as np
import vector_ops as v


def test_distance_takes_lists_and_np_arrays():
    """Make sure that lists are correctly handled"""
    point = [1, 2, 3]
    assert np.equal(v.distance(point, point), 0)

    np_array = np.array(point)
    assert np.equal(v.distance(np_array, np_array), 0)
