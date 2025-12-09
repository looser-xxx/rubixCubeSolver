# Rubik's Cube Solver (NumPy Edition)

A portable, object-oriented Rubik's Cube engine and solver built entirely in Python. This project implements the cube's logic and physics from first principles using **NumPy** for state management and coordinate transformations.

> **Note:** This project is a strict "no external logic" challenge. The solving algorithms and 3D manipulations are implemented from scratch to practice advanced array manipulation and software architecture.

## 🚀 Features

* **Pure NumPy Engine:** The cube state is managed as a set of 2D arrays (matrices), utilizing highly optimized NumPy operations like `rot90`, `flip`, and masking for rotations.
* **Object-Oriented Design:** The `Cube` class acts as a physics engine (handling the mechanics of moves like `U`, `R'`, `F2`), completely separated from the solving logic.
* **Portable Logic:** The core engine is designed to be modular, allowing it to be plugged into different interfaces (CLI, GUI, or web) or different solving algorithms.
* **Validation System:** Built-in conservation checks ensure the cube state remains physically valid (e.g., preserving sticker counts) after every operation.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Core Library:** NumPy
* **Architecture:** Modular OOP (Physics vs. Solver separation)

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/looser-xxx/rubixCubeSolver.git](https://github.com/looser-xxx/rubixCubeSolver.git)
    cd rubixCubeSolver
    ```

2.  **Set up a virtual environment (Optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install numpy
    ```

## 💻 Usage

The `Cube` class initializes with a solved state (or a custom state). You can manipulate faces using standard notation.

```python
import numpy as np
from src.cube import Cube  # Assuming your file structure

# Initialize a standard solved cube
myCube = Cube()

# Check validity
if myCube.isValidState():
    print("Cube is ready!")

# Perform moves
myCube.rotateFace('U')      # Rotate Up face Clockwise
myCube.rotateFace('R_prime') # Rotate Right face Counter-Clockwise

# Access the raw NumPy state
print(myCube.state)
