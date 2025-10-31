# perceptron_oop_plot.py
# A minimal OOP perceptron + decision boundary & loss plots (educational)

import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    """
    Very small, educational Perceptron for binary classification in R^d.
    Uses step activation: y = 1 if (w·x + b) >= 0 else 0
    Trained with the classic perceptron update rule.
    """
    def __init__(self, lr=0.1, epochs=20, shuffle=True):
        self.lr = lr
        self.epochs = epochs
        self.shuffle = shuffle
        self.w = None
        self.b = 0.0
        self.history_ = {"mistakes": []}

    def decision_function(self, X):
        """Raw score (before threshold)."""
        return X @ self.w + self.b

    def predict(self, X):
        """Binary predictions {0,1}."""
        scores = self.decision_function(X)
        return (scores >= 0).astype(int)

    def fit(self, X, y):
        """
        X: (n_samples, n_features)
        y: (n_samples,) with values in {0,1}
        """
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features, dtype=float)
        self.b = 0.0

        rng = np.random.default_rng(42)
        idx = np.arange(n_samples)

        for _ in range(self.epochs):
            if self.shuffle:
                rng.shuffle(idx)

            mistakes = 0
            for i in idx:
                xi = X[i]
                yi = y[i]
                yhat = 1 if (np.dot(self.w, xi) + self.b) >= 0 else 0
                err = yi - yhat

                if err != 0:  # only update on mistakes
                    # If target is 1 but predicted 0, we push up; vice-versa we push down
                    self.w += self.lr * err * xi
                    self.b += self.lr * err
                    mistakes += 1

            self.history_["mistakes"].append(mistakes)

        return self


def plot_decision_boundary_2d(model, X, y, title="Perceptron decision boundary"):
    """
    Works for 2D features only. Plots points and the learned separating line.
    """
    assert X.shape[1] == 2, "plot_decision_boundary_2d requires 2D input features."

    # Scatter the data
    plt.figure(figsize=(5.2, 4.2))
    plt.scatter(X[y == 0, 0], X[y == 0, 1], marker="o", label="class 0")
    plt.scatter(X[y == 1, 0], X[y == 1, 1], marker="^", label="class 1")

    # Draw decision boundary: w1*x1 + w2*x2 + b = 0  ->  x2 = -(w1/w2)*x1 - b/w2
    w1, w2 = model.w
    if abs(w2) > 1e-12:
        x1_vals = np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 100)
        x2_vals = -(w1 / w2) * x1_vals - (model.b / w2)
        plt.plot(x1_vals, x2_vals, linewidth=2, label="decision boundary")

    # Margin lines (optional visual): w·x + b = ±1
    # Only makes geometric sense for perceptron learning heuristic; not SVM margins.
    # Uncomment if you want:
    # if abs(w2) > 1e-12:
    #     x2_plus = -(w1 / w2) * x1_vals - (model.b - 1) / w2
    #     x2_minus = -(w1 / w2) * x1_vals - (model.b + 1) / w2
    #     plt.plot(x1_vals, x2_plus, linestyle="--", linewidth=1)
    #     plt.plot(x1_vals, x2_minus, linestyle="--", linewidth=1)

    plt.title(title)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_training_mistakes(model):
    """Plot number of mistakes per epoch (a simple learning curve proxy)."""
    plt.figure(figsize=(5.2, 3.8))
    plt.plot(model.history_["mistakes"], marker="o")
    plt.xlabel("Epoch")
    plt.ylabel("Number of mistakes")
    plt.title("Perceptron training mistakes per epoch")
    plt.tight_layout()
    plt.show()


# --- Demo 1: Learn the OR logic in 2D (linearly separable) --------------------
# Points: (x1, x2). We add slight jitter so the boundary is visible in 2D space.
def make_or_dataset():
    X = np.array([
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
    ], dtype=float)
    y = np.array([0, 1, 1, 1], dtype=int)
    # Tiny jitter for plotting aesthetics (optional)
    X += np.array([[0.0, 0.0], [0.0, 0.01], [0.01, 0.0], [0.01, 0.01]])
    return X, y


# --- Demo 2: A bigger, clearly separable toy dataset --------------------------
def make_separable_blobs(n=60, gap=1.5, seed=0):
    rng = np.random.default_rng(seed)
    cov = np.array([[0.15, 0.0], [0.0, 0.15]])
    c0 = np.array([-gap, 0.0])
    c1 = np.array([+gap, 0.0])
    X0 = rng.multivariate_normal(c0, cov, size=n//2)
    X1 = rng.multivariate_normal(c1, cov, size=n//2)
    X = np.vstack([X0, X1])
    y = np.hstack([np.zeros(len(X0), dtype=int), np.ones(len(X1), dtype=int)])
    return X, y


if __name__ == "__main__":
    # Try OR
    X_or, y_or = make_or_dataset()
    clf_or = Perceptron(lr=0.2, epochs=15).fit(X_or, y_or)
    print("Weights (OR):", clf_or.w, "Bias:", clf_or.b)
    print("Predictions (OR):", clf_or.predict(X_or))
    plot_decision_boundary_2d(clf_or, X_or, y_or, title="Perceptron on OR")
    plot_training_mistakes(clf_or)

    # Try a larger separable dataset
    X, y = make_separable_blobs(n=100, gap=1.2, seed=7)
    clf = Perceptron(lr=0.1, epochs=25).fit(X, y)
    print("Weights (blobs):", clf.w, "Bias:", clf.b)
    acc = (clf.predict(X) == y).mean()
    print(f"Training accuracy on blobs: {acc:.3f}")
    plot_decision_boundary_2d(clf, X, y, title="Perceptron on separable blobs")
    plot_training_mistakes(clf)
