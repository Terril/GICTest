from src.simulation import Simulation
from src.car import Car

class Main:
    def main(self):
            simulation = Simulation()

            print("Welcome to Auto Driving Car Simulation!\n")
            while True:
                try:
                    width, height = map(int, input("Please enter the width and height of the simulation field in x y format:\n").split())
                    simulation.create_grid(width, height)
                    print(f"\nYou have created a field of {width} x {height}.\n")
                    break
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")

            while True:
                print("Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation")
                choice = input()

                if choice == '1':
                    name = input("Please enter the name of the car:\n")
                    while True:
                        try:
                            x, y, direction = input(f"Please enter initial position of car {name} in x y Direction (N,S,E,W) format (eg., 5 5 N):\n").split()
                            x, y = int(x), int(y)
                            if direction not in ['N', 'S', 'E', 'W']:
                                raise ValueError("Invalid Direction")
                            if x < 0 or y < 0 or x > simulation.width or y > simulation.height:
                                raise ValueError(f"The {x} and {y} is outside of the simulation field")
                            break
                        except ValueError as e:
                            print(f"Invalid input: {e}. Please enter valid x, y (within field bounds) and direction (N, S, E, W). Field size is {simulation.width}x{simulation.height}")
                    
                    while True:
                        commands_str = input(f"Please enter the commands for car {name} (eg., FFRFFLFF):\n")
                        commands = list(commands_str)
                        valid_commands = True
                        for command in commands:
                            if command not in ['F', 'L', 'R']:
                                valid_commands = False
                                break
                        if valid_commands:
                            break
                        else:
                            print("Invalid commands. Please use only 'F', 'L', and 'R'.")
                            
                    car = Car(name, x, y, direction, commands)
                    simulation.add_car(car)

                    print("Your current list of cars are:")
                    for c in simulation.cars:
                        print(c)

                elif choice == '2':
                    simulation.run_simulation()
                    collision = False
                    for car in simulation.cars:
                        if car.collided:
                            collision=True
                            break

                    if collision:
                        simulation.display_collision_results()
                    else:
                        simulation.display_results()

                    while True:
                        choice = input("Please choose from the following options:\n[1] Start over\n[2] Exit\n")
                        if choice == '1':
                            simulation = Simulation()
                            self.main()
                            return
                        elif choice == '2':
                            print("Thank you for running the simulation. Goodbye!")
                            return
                        else:
                            print("Invalid choice.")
                else:
                    print("Invalid choice.")

if __name__ == "__main__":
        Main().main()
        