from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Charger le jeu de données Iris
iris = load_iris()
X = iris.data  # les caractéristiques
y = iris.target  # les étiquettes

# Entraîner le modèle K-means avec k=3 (puisque nous avons trois classes dans Iris)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Obtenir les centres des clusters et les affectations de chaque point
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Affichage des clusters en fonction des deux premières caractéristiques
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, c='red')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-means clustering on Iris dataset')
plt.show()
