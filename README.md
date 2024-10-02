# Project Euler Solutions

This repository contains my solutions to problems from [Project Euler](https://projecteuler.net/). 

## Purpose

The goal is to improve my problem-solving skills by tackling a range of mathematical and algorithmic challenges.

## How to Use

Each problem is located in the `solutions/` folder. Each problem contains:
- A `solution.py` file with the code.
- An optional `explanation.md` file with the problem's description, my thought process, and potential optimizations.

## Prerequisites
- Python 3.12+
- Poetry for package management
 
## Running the Solutions

1. Clone the repository:

```bash
git clone https://github.com/JAlbertoSoriaR/project-euler-solutions.git
cd project-euler-solutions 
```

2. Install dependecies using Poetry:

```bash
poetry install 
```

3. Run a solution: 

```bash
poetry run python solutions/problem_1/solution.py
```

## Testing

Unit tests are provided for each solution. To run the tests:

```bash
PYTHONPATH=./ poetry run pytest
```


 