# Spatiotemporal Signal Propagation

**Systems Biology · University of Warsaw**





This project investigates whether local neighbor activity influences future signaling events. The analysis combines spatial graph construction with temporal tracking of single-cell signaling dynamics to quantify local coordination effects in structured cell populations. By integrating neighborhood activity with future cellular responses, the framework provides a scalable approach to studying context-dependent signaling behavior in imaging-based biological systems.

For more informations about the project, read the [report](./report_Bankowska_Rawa.pdf)



Output files for tasks:

- Task A1 (Multi-Mutation Spatiotemporal Comparison):
    - mutations_comparison_table.csv
    - rr_comparison_plot.png

- Task A2 (Lagged Exposure Analysis Across Mutations):
    - lagged_exposure_table.csv
    - lagged_exposure_table.png

- Task A3 (Parameter Robustness Assessment):
    - parameter_sensitivity_analysis_plot.png


- Task B (Spatial Heterogeneity Analysis):
    - for each biosensor: outputs/B_TASK_OUTPUT/{biosensor}_table/spatial_comparison_ALL.csv
    - main comparison: outputs/B_TASK_OUTPUT/final_comparison.csv

---

## Repository structure

```
repo-root/
│
├── scripts/
│   ├── compare_spatiotemporal_behavior.py
│   ├── spatiotemporal_signal_propagation.py
│   └── task_b.py   #for task B
│   ├── make_comparison_delete_input.py #for task B (manage task_b.py outputs)
│
├── notebooks/
│   ├── TaskA1_MutationComparison.ipynb
│   ├── TaskA2_LaggedExposure.ipynb
│   ├── TaskA3_ParameterRobustness.ipynb
│   └── task_b.ipynb
│
├── outputs/
│   ├── mutations_comparison_table.csv
    ├── lagged_exposure_table.png
    ├── rr_comparison_plot.png
    ├── lagged_exposure_table.csv
    ├── parameter_sensitivity_analysis_plot.png
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
└── setup_env.sh
└── requirements.txt
│
└── single-cell-tracks_exp1-6_noErbB2.csv.gz #main data file
└── 01-readme-experiment-description_2022-04-05.csv #experiment description
└── report_Bankowska_Rawa.pdf


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


---

## Code reproducibility

For each task, there is a  notebook in the root_folder/notebooks directory containing the exact step-by-step workflow used in the analysis. This ensures full reproducibility of the results, as all preprocessing, modeling, and visualization steps are explicitly documented and can be rerun end-to-end.

Links:
- [Task A1 notebook](./notebooks/TaskA1_MutationComparison.ipynb)
- [Task A2 notebook](./notebooks/TaskA2_LaggedExposure.ipynb)
- [Task A3 notebook](./notebooks/TaskA3_ParameterRobustness.ipynb)
- [Task B ntoebook](./notebooks/task_b.ipynb)

---