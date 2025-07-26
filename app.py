# app.py

import streamlit as st
import plotly.graph_objs as go
from typing import List

from kmeans import kmeans
from nearest_neighbor import nearest_neighbor

st.set_page_config(page_title="K-means + Nearest Neighbor 3D", layout="wide")


def plot_clusters_3d(
    points: List[List[float]], clusters: List[int], centroids: List[List[float]]
):
    colors = [
        "red",
        "blue",
        "green",
        "orange",
        "purple",
        "brown",
        "pink",
        "gray",
        "olive",
        "cyan",
    ]

    scatter_points = []
    for cluster_id in set(clusters):
        cluster_points = [p for p, c in zip(points, clusters) if c == cluster_id]
        xs, ys, zs = zip(*cluster_points)
        scatter_points.append(
            go.Scatter3d(
                x=xs,
                y=ys,
                z=zs,
                mode="markers",
                marker=dict(size=5, color=colors[cluster_id % len(colors)]),
                name=f"Cluster {cluster_id}",
            )
        )

    cx, cy, cz = zip(*centroids)
    centroid_trace = go.Scatter3d(
        x=cx,
        y=cy,
        z=cz,
        mode="markers",
        marker=dict(size=10, symbol="x", color="white", opacity=0.7),
        name="Centroides",
    )

    data = scatter_points + [centroid_trace]

    layout = go.Layout(
        margin=dict(l=0, r=0, b=0, t=0),
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        legend=dict(x=0, y=1),
    )

    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig, use_container_width=True)


def main():
    st.title("K-means e Nearest Neighbor em 3D - Construído do Zero")

    st.markdown("### Insira os pontos 3D (x, y, z), separados por vírgulas")
    points_input = st.text_area(
        "Cada linha é um ponto. Exemplo:\n1,2,3\n4,5,6\n7,8,9", height=150
    )

    if not points_input.strip():
        st.info("Insira ao menos um ponto para começar.")
        return

    try:
        points = []
        for line in points_input.strip().split("\n"):
            coords = list(map(float, line.strip().split(",")))
            if len(coords) != 3:
                st.error(f"Cada ponto deve ter 3 coordenadas. Linha inválida: {line}")
                return
            points.append(coords)
    except Exception as e:
        st.error(f"Erro ao processar os pontos: {e}")
        return

    k = st.slider(
        "Número de clusters (k)", min_value=1, max_value=min(10, len(points)), value=2
    )

    if st.button("Rodar K-means"):
        clusters, centroids = kmeans(points, k)
        st.session_state["clusters"] = clusters
        st.session_state["centroids"] = centroids
        st.session_state["points"] = points

        plot_clusters_3d(points, clusters, centroids)

    elif (
        "clusters" in st.session_state
        and "centroids" in st.session_state
        and "points" in st.session_state
    ):
        plot_clusters_3d(
            st.session_state["points"],
            st.session_state["clusters"],
            st.session_state["centroids"],
        )

    st.markdown("---")

    st.markdown("### Busca do Vizinho Mais Próximo")

    query_str = st.text_input("Insira um ponto para consulta (x,y,z)")

    if query_str:
        try:
            query_point = list(map(float, query_str.strip().split(",")))
            if len(query_point) != 3:
                st.error("O ponto de consulta deve ter 3 coordenadas.")
            else:
                if "points" not in st.session_state:
                    st.warning("Execute o K-means primeiro para carregar os pontos.")
                else:
                    idx, nearest = nearest_neighbor(
                        st.session_state["points"], query_point
                    )
                    st.write(f"Ponto mais próximo: índice {idx} -> {nearest}")

        except Exception as e:
            st.error(f"Erro ao processar ponto de consulta: {e}")


if __name__ == "__main__":
    main()
