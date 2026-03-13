### Environment Setup

* Migrated development environment to **Ubuntu WSL** for better compatibility with scientific computing libraries.
* Created a clean Python virtual environment (`chemcrow_env`).
* Installed and configured key computational chemistry and visualization libraries:

  * PySCF for quantum chemistry calculations
  * RDKit for molecular structure handling
  * py3Dmol for 3D molecular visualization
  * LangChain and OpenAI API for AI agent integration.

Features
Quantum Harmonic Oscillator Solver

Computes energy levels using the analytical quantum mechanics solution:

Eₙ = ħω(n + 1/2)

Hartree–Fock Quantum Calculations

Performs ab initio electronic structure calculations using PySCF.

Example:

Water molecule

Benzene

Ethanol

Molecular Visualization

Converts SMILES strings into 3D molecular structures and visualizes them interactively.

Agentic AI Workflow

The AI agent can:

Interpret chemistry questions

Choose appropriate scientific tools

Execute calculations

Return scientific results

Technologies Used

Python

PySCF

RDKit

py3Dmol

LangChain

OpenAI API

Installation

Clone the repository:

git clone https://github.com/yourusername/QuantumChemCrow.git
cd QuantumChemCrow

Create environment:

python -m venv chemcrow_env
source chemcrow_env/bin/activate

Install dependencies:

pip install -r dev-requirements.txt
pip install pyscf rdkit py3Dmol

Set OpenAI API key:

export OPENAI_API_KEY="your_key"
Example Usage

Quantum Harmonic Oscillator:

from chemcrow.tools.quantum.qho_solver import quantum_harmonic_oscillator

quantum_harmonic_oscillator(5, 1e14)

Hartree–Fock Energy:

from chemcrow.tools.quantum.hf_energy import hartree_fock_energy

hartree_fock_energy("O")

Molecular Visualization:

from chemcrow.tools.quantum.molecule_visualizer import visualize_molecule

visualize_molecule("c1ccccc1")
Example Output

Hartree–Fock energy for water:

SCF Energy = -74.96 Hartree
Project Structure
chemcrow/
    agents/
    tools/
        quantum/
            hf_energy.py
            molecule_visualizer.py
            qho_solver.py
Author

Tejas Lokhande

Master's Student in Computational Chemistry
Computational Chemistry and Machine Learning Lab

License

MIT License
