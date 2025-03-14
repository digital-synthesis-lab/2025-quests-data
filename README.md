# Data for: Model-free estimation of completeness, uncertainties, and outliers in atomistic machine learning using information theory

[![Data](https://zenodo.org/badge/DOI/10.5281/zenodo.15025644.svg)](https://doi.org/10.5281/zenodo.15025644)
[![Code](https://zenodo.org/badge/760951897.svg)](https://doi.org/10.5281/zenodo.15025957)

This repository contains the notebooks to reproduce the paper:

D. Schwalbe-Koda, S. Hamel, B. Sadigh, F. Zhou, V. Lordi. "Model-free estimation of completeness, uncertainties, and outliers in atomistic machine learning using information theory". arXiv:2404.12367 (2024). DOI: [10.48550/arXiv.2404.12367](https://doi.org/10.48550/arXiv.2404.12367)

- All the raw data for plotting the notebooks can be downloaded using the `download.sh` script.
- The Jupyter Notebooks in `nbs` contain all the code required to reproduce the analysis and the plots shown in the manuscript.

## Installing and running

To reproduce the results from the manuscript, first create a new Python environment using your preferred virtual environment (e.g., `venv` or `conda`).
Then, clone this repository and install it with

```bash
git clone git@github.com:digital-synthesis-lab/2025-quests-data.git
cd 2025-quests-data
pip install -e .
```

This should install all dependencies (see [pyproject.toml](pyproject.toml)) to reproduce the data in the manuscript.
For full reproducibility, all packages used when producing the results of this work are given in the [environment.txt](environment.txt) file.

To download the raw data that has all the results for this paper (and the required data for analysis), simply run

```bash
chmod +x download.sh
./download.sh
```

in the root of the repository.
While some of the data is already available in the repository, most of the raw data is too large for GitHub.
Thus, part of the raw data that reproduces the paper is hosted on Zenodo for persistent storage (DOI: [10.5281/zenodo.15025644](https://doi.org/10.5281/zenodo.15025644)).

## Data and Code Description

After downloading the raw data folder, the results will exhibit all data from the paper.
The `data` folder is sorted by section of the paper (01 through 05) and supplementary information (A01 through A11).
Its structure is the following:

```
    data/
    ├── 02-Aluminum
    ├── 02-GAP20
    ├── 02-rMD17
    ├── 04-TM23
    ├── 05-Cu
    ├── 05-Ta
    ├── A08-Denoiser
    ├── A11-Cu
    ├── A11-QTB
    └── A11-Sn
```

The notebooks in folder `nbs` contain all code to reproduce the figures from the raw data.
Examples on how to generate the data can be found at the [QUESTS package](https://github.com/dskoda/quests).

### Citing

If you use QUESTS or its data/examples in a publication, please cite the following paper:

```bibtex
@article{schwalbekoda2024information,
    title = {Model-free quantification of completeness, uncertainties, and outliers in atomistic machine learning using information theory},
    author = {Schwalbe-Koda, Daniel and Hamel, Sebastien and Sadigh, Babak and Zhou, Fei and Lordi, Vincenzo},
    year = {2024},
    journal = {arXiv:2404.12367},
    url = {https://arxiv.org/abs/2404.12367},
    doi = {10.48550/arXiv.2404.12367},
}
```
## License

This repository is distributed under the following license: BSD-3

All new contributions must be made under this license.

SPDX: BSD-3-Clause

## Acknowledgements

This work was initially produced under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344, with support from LLNL's LDRD program under tracking codes 22-ERD-055 and 23-SI-006.
