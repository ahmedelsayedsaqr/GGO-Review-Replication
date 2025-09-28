#!/usr/bin/env bash
# Run all benchmark experiments for GGO

echo "🚀 Starting all benchmark experiments..."

python src/run_benchmarks.py --bench sphere --n_runs 20 --dim 30 --pop_size 30 --max_iter 200
python src/run_benchmarks.py --bench rastrigin --n_runs 20 --dim 30 --pop_size 30 --max_iter 200
python src/run_benchmarks.py --bench ackley --n_runs 20 --dim 30 --pop_size 30 --max_iter 200
python src/run_benchmarks.py --bench rosenbrock --n_runs 20 --dim 30 --pop_size 30 --max_iter 200
python src/run_benchmarks.py --bench griewank --n_runs 20 --dim 30 --pop_size 30 --max_iter 200

echo "✅ All experiments completed! Results saved in the 'results/' folder."
