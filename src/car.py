import threading
import logging
class Car:
    def __init__(self, name, initial_x, initial_y, direction, commands):
        self.name = name
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.initial_direction = direction
        self.x = initial_x
        self.y = initial_y
        self.direction = direction
        self.commands = commands
        self.index = 0
        self.collided = False
        self.lock = threading.Lock()

    def __repr__(self):
        return f"- {self.name}, ({self.initial_x},{self.initial_y}) {self.initial_direction}, {''.join(self.commands)}"

    def rotate_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def rotate_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def move_forward(self, width, height):
        if self.direction == 'N' and self.y + 1 < height:
            self.y += 1
        elif self.direction == 'S' and self.y - 1 >= 0:
            self.y -= 1
        elif self.direction == 'E' and self.x + 1 < width:
            self.x += 1
        elif self.direction == 'W' and self.x - 1 >= 0:
            self.x -= 1

    def process_command(self, width, height):
        with self.lock:
            if self.collided or self.index >= len(self.commands):
                return

            command = self.commands[self.index]
            if command == 'L':
                self.rotate_left()
            elif command == 'R':
                self.rotate_right()
            elif command == 'F':
                self.move_forward(width, height)
            else:
                logging.warning(f"Car {self.name}: Invalid command '{command}' ignored.")
            self.index += 1