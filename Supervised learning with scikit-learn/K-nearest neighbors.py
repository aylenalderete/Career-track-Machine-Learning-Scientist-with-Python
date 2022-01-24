# k-Nearest Neighbors: Fit
from sklearn.neighbors import KNeighborsClassifier

# X and y are a DataFrame and Series respectively; the scikit-learn API
# will accept them in this form also as long as they are of the right shape.
y = df['party'].values
X = df.drop('party', axis=1).values

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X, y)