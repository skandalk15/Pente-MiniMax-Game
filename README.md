# Pente Game Agent - README

This project implements an agent that plays the game of Pente, a two-player abstract strategy board game. The agent uses alpha-beta pruning to make decisions and aims to win either by connecting five pieces in a row or capturing five pairs of the opponent's pieces.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Input and Output Formats](#input-and-output-formats)
6. [Algorithm](#algorithm)
7. [Deployment](#deployment)
8. [Contributing](#contributing)

## Project Description

Pente is a turn-based strategy game played on a 19x19 board. The players take turns placing pieces on the board, aiming to either connect five pieces in a line or capture five pairs of the opponent's pieces. The first player always starts at the center of the board.

This project focuses on implementing a Pente-playing agent that uses the alpha-beta pruning algorithm to choose the best move based on the current state of the game.

## Features

- Implements the game of Pente on a 19x19 board.
- Uses alpha-beta pruning for efficient decision-making.
- Handles both regular and capture moves.
- Determines the winner based on the game's winning conditions.
- Reads the game state from an input file and writes the move to an output file.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/skandalk15/Pente-MiniMax-Game.git
cd pente-game-agent
```

2. **Install dependencies:**

There are no external dependencies required for this project.

## Usage

1. **Prepare the input file:**

The input file `input.txt` should be placed in the root directory. The format of this file is specified in the [Input and Output Formats](#input-and-output-formats) section.

2. **Run the agent:**

```bash
python pente_agent.py
```

3. **Check the output file:**

The output file `output.txt` will contain the agent's chosen move in the specified format.

## Input and Output Formats

### Input Format (`input.txt`)

The `input.txt` file should contain the following information:

1. The color of the next move (`WHITE` or `BLACK`).
2. The remaining play time (in seconds) as a float.
3. The number of captures for both players in the format `white_captures,black_captures`.
4. The current state of the board as a 19x19 grid, with each cell separated by a space.

Example:
```
BLACK
100.0
0,0
...................
...................
...................
...................
...................
...................
...................
...................
...................
.................w.
...................
...................
...................
...................
...................
...................
...................
...................
...................
```

### Output Format (`output.txt`)

The `output.txt` file will contain the chosen move in the format:
```
row<letter><column>
```

Example:
```
K10
```

## Algorithm

The agent uses the alpha-beta pruning algorithm to evaluate possible moves and select the best one. It considers both regular moves and capture moves to determine the most advantageous position. The evaluation function assesses the board based on the number of connected pieces, potential captures, and the overall game state.

## Deployment

This project does not require specific deployment steps as it is designed to be run locally for the purpose of the CSCI-561 Foundations of Artificial Intelligence course.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

### Steps to Contribute

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

---

Thank you for using and contributing to the Pente Game Agent! If you have any questions or need further assistance, feel free to open an issue or contact us at [your-email@example.com].
