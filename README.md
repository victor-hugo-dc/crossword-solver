# Crossword Solver

Simple crossword puzzle solver that utilizes ChatGPT to solve given clues. At the moment, the program connects to a crossword puzzle from the website [downforacross](https://www.downforacross.com/) and extracts all of the clues in the across direction, then it asks User which clue they would like to have solved.

## Usage
To run this project,
1. Install Python 3.8 or above from [here](https://www.python.org/download/releases/)
2. Clone the repository:
    ```
    git clone https://github.com/victor-hugo-dc/crossword-solver.git
    ```
    or download as a zip file and extract.
3. To install all dependencies, run:
    ```
    pip install -r requirements.txt
    ```
4. In the root directory, run:
    ```
    python3 solver.py
    ```
5. Follow the instructions printed by the program.

## Future Improvements
- [ ] Work on getting the down clues.
- [ ] Edge casing for proper usage.
