# Spatiotemporal Signal Propagation

**Systems Biology · University of Warsaw**





This project investigates whether local neighbor activity influences future signaling events, and whether this propagation differs across:
- spatial position (edge vs central)
- genetic background (mutations)
- temporal dynamics (lagged responses)



Key outputs include:

final_comparison.csv – edge vs central RR statistics
group_level_summary.csv – mutation-level propagation summary
analysis_outputs/ – per-block graph and propagation results
Figures for RR comparisons and statistical tests

---

## Repository structure

```
repo-root/
│
├── scripts/
│   ├── compare_spatiotemporal_behavior.py
│   ├── make_comparison_delete_input.py
│   ├── spatiotemporal_signal_propagation.py
│   └── task_b.py
│
├── notebooks/
│   ├── TaskA1_MutationComparison.ipynb
│   ├── TaskA2_LaggedExposure.ipynb
│   ├── TaskA3_ParameterRobustness.ipynb
│   └── TaskB_SpatialHeterogeneity.ipynb
│
├── outputs/
│   ├── group_level_summary.csv
│   │
│   └── B_TASK_OUTPUT/
│       ├── final_comparison.csv
│       │
│       ├── FoxO3A_table/
│       │   └── spatial_comparison_ALL.csv
│       │
│       └── ERKKTR_table/
│           └── spatial_comparison_ALL.csv
│
├── analysis_outputs/
│
├── README.md
└── requirements.txt
```


## Getting started
Python 3 was used
```bash
# 2. Create and activate a virtual environment
bash setup_env.sh
source .venv/bin/activate


# 4. Run a quick single-block analysis to verify the setup
python scripts/spatiotemporal_signal_propagation.py \
    --exp-id 1 --site-id 1 \
    --signal-col ERKKTR_ratio \
    --output-dir analysis_outputs
```

---

## Dependencies

See `requirements.txt`. Core dependencies: `numpy`, `pandas`, `scipy`, `matplotlib`.
All notebooks require `jupyter` (or JupyterLab).

---
|
