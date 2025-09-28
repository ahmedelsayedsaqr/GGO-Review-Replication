import numpy as np

class GGO:
    """
    Reference implementation of Grey Geese Optimizer (GGO) in Python.
    """

    def __init__(self, obj_fn, dim, bounds=(-10, 10), pop_size=30, max_iter=100, seed=None):
        self.obj_fn = obj_fn
        self.dim = dim
        self.lb, self.ub = bounds
        self.pop_size = pop_size
        self.max_iter = max_iter
        self.rng = np.random.default_rng(seed)

        self.positions = None
        self.fitness = None
        self.best_pos = None
        self.best_fit = np.inf

    def _init_population(self):
        self.positions = self.rng.uniform(self.lb, self.ub, size=(self.pop_size, self.dim))
        self.fitness = np.apply_along_axis(self.obj_fn, 1, self.positions)
        best_idx = np.argmin(self.fitness)
        self.best_fit = self.fitness[best_idx]
        self.best_pos = self.positions[best_idx].copy()

    def _ensure_bounds(self, x):
        return np.clip(x, self.lb, self.ub)

    def optimize(self, verbose=False):
        self._init_population()
        history = []

        for t in range(self.max_iter):
            leader_idx = t % self.pop_size
            leader = self.positions[leader_idx]

            for i in range(self.pop_size):
                r1, r2 = self.rng.random(self.dim), self.rng.random(self.dim)
                step = 0.6 * r1 * (leader - self.positions[i]) + 0.4 * r2 * (self.best_pos - self.positions[i])
                perturb = 0.1 * self.rng.normal(size=self.dim) * (self.ub - self.lb)

                new_pos = self._ensure_bounds(self.positions[i] + step + perturb)
                new_fit = self.obj_fn(new_pos)

                if new_fit < self.fitness[i]:
                    self.positions[i] = new_pos
                    self.fitness[i] = new_fit
                    if new_fit < self.best_fit:
                        self.best_fit = new_fit
                        self.best_pos = new_pos.copy()

            history.append(self.best_fit)

            if verbose and (t % max(1, self.max_iter // 10) == 0):
                print(f"Iter {t}/{self.max_iter} Best = {self.best_fit:.6e}")

        return {"best_pos": self.best_pos, "best_fit": self.best_fit, "history": history}
