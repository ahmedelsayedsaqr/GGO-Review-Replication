import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import trange

from ggo import GGO
from benchmarks import BENCHMARKS

# إعداد مجلد النتائج
BASE_DIR = os.path.dirname(__file__)
RESULTS_DIR = os.path.join(BASE_DIR, "..", "results")
TABLES_DIR = os.path.join(RESULTS_DIR, "tables")
PLOTS_DIR = os.path.join(RESULTS_DIR, "plots")
os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

def run_with_history(bench, n_runs=10, dim=30, pop_size=30, max_iter=500):
    fn, lb, ub = BENCHMARKS[bench]
    histories, finals = [], []

    for r in trange(n_runs, desc=f"Running {bench}"):
        optimizer = GGO(fn, dim, (lb, ub), pop_size=pop_size, max_iter=max_iter, seed=r)
        out = optimizer.optimize()
        histories.append(out["history"])
        finals.append(out["best_fit"])

    histories = np.array(histories)
    finals = np.array(finals)

    # حفظ النتائج كـ CSV
    df = pd.DataFrame({"run": np.arange(n_runs), "best_fit": finals})
    df.to_csv(os.path.join(TABLES_DIR, f"{bench}_results.csv"), index=False)

    # رسم منحنى التقارب (Median + Mean)
    iters = np.arange(1, histories.shape[1] + 1)
    median_curve = np.median(histories, axis=0)
    mean_curve = np.mean(histories, axis=0)

    plt.figure(figsize=(7,5))
    plt.plot(iters, median_curve, label="Median best")
    plt.plot(iters, mean_curve, "--", label="Mean best")
    plt.xlabel("Iteration")
    plt.ylabel("Best fitness")
    plt.title(f"Convergence curve - {bench}")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(PLOTS_DIR, f"{bench}_convergence.png"), dpi=150)
    plt.close()

    # رسم boxplot للقيم النهائية
    plt.figure(figsize=(6,4))
    sns.boxplot(x=finals)
    plt.xlabel("Best fitness")
    plt.title(f"Final best fitness distribution - {bench}")
    plt.savefig(os.path.join(PLOTS_DIR, f"{bench}_boxplot.png"), dpi=150)
    plt.close()

    print(f"Saved results for {bench}")

if __name__ == "__main__":
    # شغّل كل الدوال
    for bench in BENCHMARKS.keys():
        run_with_history(bench, n_runs=10, dim=30, pop_size=30, max_iter=500)
