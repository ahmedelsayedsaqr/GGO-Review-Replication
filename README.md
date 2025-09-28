# GGO-Review-Replication
📂 This repository provides the replication materials for the paper:

📑 "A Software-Oriented Review of the Grey Geese Optimizer: Implementations, Benchmarks, and Comparative Performance"

✨ The repository includes:
- 🐦 A clean Python implementation of the Grey Geese Optimizer (GGO).
- 📊 Standard benchmark functions (Sphere, Rastrigin, Ackley, Rosenbrock, Griewank).
- ⚙️ Experimental scripts to reproduce all results reported in the paper.
- 📈 Tables and plots with comparative results against other metaheuristics.
- 🔁 A replication workflow to ensure full reproducibility.

🎓 This project is intended to support both researchers and practitioners by offering a reproducible reference implementation of GGO and standardized benchmarking protocols.

---

# Installation

Follow the steps below to set up and run the Grey Geese Optimizer (GGO) implementation in Python:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ahmedelsayedsaqr/GGO-Review-Replication.git
cd GGO-Review-Replication


2️⃣ Create a virtual environment
Using venv
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Or using conda:
conda create -n ggo-env python=3.9
conda activate ggo-env

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run full replication (all benchmarks)
bash run_all.sh

5️⃣ Quick test
python src/python/run_benchmarks.py --bench sphere --n_runs 3 --pop_size 30 --dim 30
