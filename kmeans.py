import math
import random
from typing import List, Tuple

from utils import euclidean_distance


def initialize_centroids(points: List[List[float]], k: int) -> List[List[float]]:
    return random.sample(points, k)


def assign_clusters(
    points: List[List[float]], centroids: List[List[float]]
) -> List[int]:
    clusters = []
    for p in points:
        distances = [euclidean_distance(p, c) for c in centroids]
        cluster_idx = distances.index(min(distances))
        clusters.append(cluster_idx)
    return clusters


def calculate_centroids(
    points: List[List[float]], clusters: List[int], k: int
) -> List[List[float]]:
    centroids = []
    for i in range(k):
        cluster_points = [p for p, c in zip(points, clusters) if c == i]
        if cluster_points:
            centroid = [
                sum(coords) / len(cluster_points) for coords in zip(*cluster_points)
            ]
        else:
            centroid = random.choice(points)
        centroids.append(centroid)
    return centroids


def has_converged(
    old_centroids: List[List[float]], new_centroids: List[List[float]], tol: float
) -> bool:
    total_movement = sum(
        euclidean_distance(o, n) for o, n in zip(old_centroids, new_centroids)
    )
    return total_movement < tol


def kmeans(
    points: List[List[float]], k: int, max_iters: int = 100, tol: float = 1e-4
) -> Tuple[List[int], List[List[float]]]:
    centroids = initialize_centroids(points, k)
    for iteration in range(max_iters):
        clusters = assign_clusters(points, centroids)
        new_centroids = calculate_centroids(points, clusters, k)
        if has_converged(centroids, new_centroids, tol):
            print(f"Converged at iteration {iteration}")
            break
        centroids = new_centroids
    return clusters, centroids
