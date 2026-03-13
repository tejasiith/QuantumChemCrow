## QuantumChemCrow

# Agentic AI framework for quantum chemistry built by extending the ChemCrow architecture.

This project integrates Large Language Models with quantum chemistry tools to enable intelligent reasoning and automated scientific workflows.

## Overview

QuantumChemCrow combines AI reasoning with computational chemistry tools. The system allows an AI agent to analyze chemical questions and automatically call scientific tools such as quantum calculations and molecular visualization.

This project extends the ChemCrow framework by adding quantum chemistry capabilities relevant to computational chemistry research.

## Environment Setup

* Migrated development environment to **Ubuntu WSL** for better compatibility with scientific computing libraries.
* Created a clean Python virtual environment named `chemcrow_env`.
* Installed and configured key computational chemistry and visualization libraries:

  * **PySCF** for quantum chemistry calculations.
  * **RDKit** for molecular structure parsing and manipulation.
  * **py3Dmol** for interactive 3D molecular visualization.
  * **LangChain** and **OpenAI API** for AI agent integration.

---

## Features

### 1. Quantum Harmonic Oscillator Solver

* Computes energy levels using the analytical quantum mechanics formula:

[
E_n = \hbar \omega (n + 1/2)
]

* Allows users to calculate energy states for different oscillator frequencies.

---

### 2. Hartree–Fock Quantum Calculations

* Performs **ab initio electronic structure calculations** using PySCF.
* Automatically converts molecular representations:

```
SMILES → RDKit Molecule → 3D Geometry → PySCF Calculation
```

* Tested on example molecules:

  * Water
  * Benzene
  * Ethanol

---

### 3. Molecular Visualization

* Converts **SMILES strings into 3D molecular structures**.
* Displays interactive molecules using **py3Dmol**.
* Works directly inside **Jupyter Notebook / JupyterLab**.

---

### 4. Agentic AI Workflow

The AI agent can:

* Interpret chemistry questions.
* Select appropriate computational tools.
* Execute quantum calculations.
* Return scientifically meaningful results.

---

## Technologies Used

* Python
* PySCF
* RDKit
* py3Dmol
* LangChain
* OpenAI API

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/QuantumChemCrow.git
cd QuantumChemCrow
```

### Create virtual environment

```bash
python -m venv chemcrow_env
source chemcrow_env/bin/activate
```

### Install dependencies

```bash
pip install -r dev-requirements.txt
pip install pyscf rdkit py3Dmol
```

### Set OpenAI API key

```bash
export OPENAI_API_KEY="your_key"
```

---

## Example Usage

### Quantum Harmonic Oscillator

```python
from chemcrow.tools.quantum.qho_solver import quantum_harmonic_oscillator

quantum_harmonic_oscillator(5, 1e14)
```

### Hartree–Fock Energy Calculation

```python
from chemcrow.tools.quantum.hf_energy import hartree_fock_energy

hartree_fock_energy("O")
```

### Molecular Visualization

```python
from chemcrow.tools.quantum.molecule_visualizer import visualize_molecule

visualize_molecule("c1ccccc1")
```

---

## Example Output

Hartree–Fock energy for water:

```
SCF Energy = -74.96 Hartree
```

---

## Project Structure

```
chemcrow/
    agents/
    tools/
        quantum/
            hf_energy.py
            molecule_visualizer.py
            qho_solver.py
```

---

## Author

**Tejas Lokhande**

Master's Student – IIT Hyderabad

---

## License

MIT License
