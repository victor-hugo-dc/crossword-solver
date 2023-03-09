# Crossword Solver

Simple crossword puzzle solver that utilizes ChatGPT to solve given clues. The program connects to a crossword puzzle from the website [downforacross](https://www.downforacross.com/) and extracts all of the clues and solves it using the ChatGPT API.

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
4. Put your OpenAI key in the a config.py file in the root directory.
5. Get a valid [downforacross](https://www.downforacross.com/) link. 
6.  Run
    ```
    python3 solver.py
    ```
    and provide the link as input when prompted
