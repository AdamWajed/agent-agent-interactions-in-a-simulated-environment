# Agent-Agent Interactions in a Simulated Environment

This repository contains the source code, prompts and results required for the investigation, detailed in: https://AdamWajed.github.io/agent-agent-interactions-in-a-simulated-environment/



The study here is a development of work by Apollo Research and uses some of the prompts in the attached repository: https://github.com/ApolloResearch/insider-trading/tree/main


## Installation

The required Python packages can be installed by executing
```bash
pip install -r requirements.txt
```
in the root directory of this repository. To ensure reproducibility, all packages in ``requirements.txt`` are version pinned, and Python ``3.10.20`` should be used.

## Reproducing the data

Experiment ``Xy`` can be run by executing:
```bash
python -m src.exp.exp_Xy
```
in the root directory of this repository. 

### Plotting the data 

The results of Experiment ``X`` can be plotted by executing:
```bash
python -m plotting.exp_X
```
in the root directory of this repository.

## File Structure

This repository is organised as follows:

```bash
docs/
├── figures/
└──	index.html
figures/
plotting/
├──	exp_0.py
├──	exp_1.py
└── exp_2.py
prompts/
├──	exp_0a/
	└──	default.json
    ...
└──	exp_3a/
	├──	alpha1.json
    └──	alpha2.json
results/
├──	exp_0a/
	├──	gpt-4-0613/
	├──	gpt-4.1/
	└── gpt-5.5/
    ...
└──	exp_3a/
	└──	gpt-4-0613+gpt-4-0613/
src/
├──	exp/
    ├──	exp_0a.py
    ├──	exp_0b.py
    ...
    └──exp_3a.py
└──	functions.py	
README.md
requirements.txt
```

Notes:
- The `prompts/` directory contains JSON prompt definitions used in experiments.

- The `results/` directory stores experiment outputs organised by experiment and model.




