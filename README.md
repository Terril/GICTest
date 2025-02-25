# Driving Car Simulation Project

This project simulates the movement of cars on a rectangular grid field. Users can define the field size, add cars with specific starting positions, directions, and command sequences, and then run the simulation to observe the cars movements and detect collisions.


## Project Structure

-   `src/car.py`: Contains the `Car` class, which defines the properties and behaviors of a car, including movement and rotation logic.
-   `src/simulation.py`: Contains the `Simulation` class, which manages the simulation field, adds cars, runs the simulation, and detects collisions.
-   `src/main.py`: Contains the `Main` class, which provides a command-line interface for users to interact with the simulation.
-   `test/test_simulation.py`: Contains unit tests for the `Car` and `Simulation` classes.
-   `.vscode/settings.json`: VS Code settings for the project.


## Features

*   **Field Creation:** Users can define the width and height of the simulation field.
*   **Car Addition:** Users can add multiple cars to the field, specifying their name, initial position (x, y), direction (N, S, E, W), and a sequence of commands.
*   **Command Processing:** Cars can execute commands to move forward ('F'), rotate left ('L'), or rotate right ('R').
*   **Boundary Detection:** Cars cannot move beyond the boundaries of the field.
*   **Collision Detection:** The simulation detects collisions between cars and identifies the colliding cars.
*   **Concurrency:** The simulation uses threading to simulate the movement of multiple cars concurrently.
*   **Results Display:** The simulation displays the final positions and directions of the cars after the simulation, as well as any collision messages.
*   **Start Over/Exit:** After a simulation run, users can choose to start over with a new simulation or exit the program.


## Running the Simulation
1.  Run the [main.py] script:
    python src/main.py

2.  Follow the prompts in the command-line interface.

## Running the Tests

To run the unit tests, use the following command:
    python -m unittest discover -s test