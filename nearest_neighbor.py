from typing import List, Tuple
from utils import euclidean_distance


def nearest_neighbor(
    points: List[List[float]], query_point: List[float]
) -> Tuple[int, List[float]]:
    min_dist = float("inf")
    nearest_idx = -1
    for idx, p in enumerate(points):
        dist = euclidean_distance(p, query_point)
        if dist < min_dist:
            min_dist = dist
            nearest_idx = idx
    return nearest_idx, points[nearest_idx]
