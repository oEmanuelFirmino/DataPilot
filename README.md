# DataPilot: 3D K-means and Nearest Neighbor from Scratch

DataPilot is an interactive web application built with Streamlit that demonstrates K-means clustering and Nearest Neighbor search algorithms in a 3D space. Both algorithms are implemented in pure Python from scratch, providing a clear view of their inner workings. The application allows users to input their own 3D data points, run the algorithms, and visualize the results in an interactive 3D plot powered by Plotly.

## Features

- **K-means Clustering from Scratch**: Groups 3D data points into a specified number of clusters ($k$).
- **Nearest Neighbor Search**: Finds the closest point in the dataset to a given query point.
- **Interactive 3D Visualization**: Uses Plotly to create a dynamic 3D scatter plot of the data points, clusters, and centroids.
- **User-Friendly Interface**: Built with Streamlit for easy data entry and control over algorithm parameters.
- **Pure Python Implementation**: The core logic is written entirely from scratch, making it a great educational tool.

## Mathematical Concepts

The core of both algorithms relies on fundamental mathematical concepts, primarily the measure of distance between points.

### Euclidean Distance

The Euclidean distance is the straight-line distance between two points in Euclidean space. For two points $p$ and $q$ in an $n$-dimensional space, the distance is calculated as:

$$d(p, q) = \sqrt{\sum_{i=1}^{n} (p_i - q_i)^2}$$

In this project, we use it for 3D points ($n=3$), so for $p=(x_1, y_1, z_1)$ and $q=(x_2, y_2, z_2)$, the formula becomes:

$$d(p, q) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}$$

This metric is implemented in the `utils.py` file.

### K-means Clustering

K-means is an iterative unsupervised learning algorithm that aims to partition a dataset into $k$ distinct, non-overlapping subgroups (clusters) where each data point belongs to only one group. The algorithm works as follows:

1.  **Initialization**: $k$ points from the dataset are randomly chosen as the initial centroids.

2.  **Assignment Step**: Each data point is assigned to the cluster whose centroid is the nearest. The "nearness" is determined by the Euclidean distance. If $\mu_i^{(t)}$ is the centroid for cluster $i$ at iteration $t$, then a point $x_p$ is assigned to cluster $S_i^{(t)}$ based on the following condition:

    $$
    S_i^{(t)} = \{ x_p : \|x_p - \mu_i^{(t)}\|^2 \le \|x_p - \mu_j^{(t)}\|^2 \quad \forall j, 1 \le j \le k \}
    $$

3.  **Update Step**: The centroid of each cluster is recalculated as the mean of all data points assigned to it.

    $$
    \mu_i^{(t+1)} = \frac{1}{|S_i^{(t)}|} \sum_{x_p \in S_i^{(t)}} x_p
    $$

4.  **Convergence**: Steps 2 and 3 are repeated until the centroids' positions no longer change significantly between iterations (i.e., the algorithm has converged) or a maximum number of iterations is reached.

The implementation of this algorithm can be found in `kmeans.py`.

### Nearest Neighbor Search

This is a straightforward, brute-force search algorithm. Given a dataset $P$ and a query point $q$, the goal is to find the point $p_{nn} \in P$ that has the minimum Euclidean distance to $q$.

The algorithm iterates through every point $p_i$ in the dataset $P$, calculates $d(q, p_i)$, and keeps track of the point with the smallest distance found so far.

$$p_{nn} = \arg\min_{p_i \in P} d(q, p_i)$$

This logic is implemented in `nearest_neighbor.py`.

## Project Structure

```
.
├── .gitignore
├── LICENSE
├── README.md
├── app.py              # Main Streamlit application file
├── kmeans.py           # K-means algorithm implementation
├── nearest_neighbor.py # Nearest Neighbor search implementation
└── utils.py            # Utility functions (e.g., Euclidean distance)
```

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/oemanuelfirmino/DataPilot.git](https://github.com/oemanuelfirmino/DataPilot.git)
    cd DataPilot
    ```

2.  **Create a virtual environment and install dependencies:**
    It's recommended to create a virtual environment to manage dependencies.

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

    Install the required libraries:

    ```bash
    pip install streamlit plotly
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your default web browser.

## License

This project is licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for more details.
