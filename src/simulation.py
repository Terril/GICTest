import threading

class Simulation:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.cars = []
        self.lock = threading.Lock()
        self.collision_messages = []

    def create_grid(self, width, height):
        with self.lock:
            self.width = width
            self.height = height

    def add_car(self, car):
        with self.lock:
            self.cars.append(car)

    def run_simulation(self):
        step = 0
        while True:
            all_cars_finished = True
            with self.lock:
                for car in self.cars:
                    if car.index < len(car.commands) and not car.collided:
                        all_cars_finished = False
                        break
            if all_cars_finished:
                break

            step += 1
            positions = {}
            threads = []
            with self.lock:
                for car in self.cars:
                    if not car.collided:
                        thread = threading.Thread(target=car.process_command, args=(self.width, self.height))
                        threads.append(thread)
                        thread.start()
                for thread in threads:
                    thread.join()

            with self.lock:
                positions = {}
                for car in self.cars:
                    if not car.collided:
                        position = (car.x, car.y)
                        if position in positions:
                            collided_car_name = positions[position]
                            for c in self.cars:
                                if c.name == collided_car_name or c.name == car.name:
                                    c.collided = True
                            self.collision_messages.append(f"- {car.name}, collides with {collided_car_name} at ({car.x},{car.y}) at step {step}")
                        else:
                            positions[position] = car.name

    def display_results(self):
        print("\nYour current list of cars are:")
        with self.lock:
            for car in self.cars:
                print(car)

        print("\nAfter simulation, the result is:")
        with self.lock:
            for car in self.cars:
                if not car.collided:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")

    def display_collision_results(self):
        print("\nYour current list of cars are:")
        with self.lock:
            for car in self.cars:
                print(car)

        print("\nAfter simulation, the result is:")
        for message in self.collision_messages:
            print(message)
        with self.lock:
            for car in self.cars:
                if not car.collided:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")

                    