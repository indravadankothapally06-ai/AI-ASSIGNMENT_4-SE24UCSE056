# AI Assignment 4: Constraint Satisfaction Problems (CSP)

This repository contains Python implementations of standard Constraint Satisfaction Problems (CSP) using backtracking algorithms and heuristics like Minimum Remaining Values (MRV). It was created for an Artificial Intelligence course programming assignment.

## 📂 Repository Structure

The project is divided into four distinct folders, each containing the problem's source code, a JSON file for dynamic data input, and a specific README for that problem.

- **`1_Australia_Map_Coloring/`**
  - Solves the classic map coloring problem for the 7 principal territories of Australia using 3 colors.
  - `australia_csp.py`, `australia_data.json`

- **`2_Telangana_Map_Coloring/`**
  - Applies the Four Color Theorem to the 33 districts of Telangana to ensure no two adjacent districts share the same color.
  - `telangana_csp.py`, `telangana_data.json`

- **`3_Sudoku_CSP/`**
  - Formulates a standard 9x9 Sudoku puzzle purely as a CSP, evaluating rows, columns, and 3x3 subgrids as constraints.
  - `sudoku_csp.py`, `sudoku_board.json`

- **`4_Cryptarithmetic_CSP/`**
  - Solves letter-to-digit cryptanalysis puzzles (e.g., SEND + MORE = MONEY) where every letter represents a unique digit and constraints govern the arithmetic logic.
  - `cryptarithmetic_csp.py`, `puzzle_data.json`

## ⚙️ Prerequisites

- **Python 3.x** installed on your system.
- Standard built-in Python libraries are used (`json`, `itertools`); no external dependencies like `pip install` are required.

## 🚀 How to Run

Navigate into any of the specific problem folders and execute the Python script. The scripts are designed to automatically read their constraints and variables from the accompanying `.json` files.

Example:
```bash
cd 1_Australia_Map_Coloring
python australia_csp.py
