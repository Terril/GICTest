import unittest
from src.simulation import Simulation
from src.car import Car

class TestSimulation(unittest.TestCase):
    def test_single_car(self):
        simulation = Simulation()
        simulation.create_grid(10, 10)
        car = Car("A", 1, 2, "N", list("FFRFFFFRRL"))
        simulation.add_car(car)
        simulation.run_simulation()
        self.assertEqual(car.x, 5)
        self.assertEqual(car.y, 4)
        self.assertEqual(car.direction, "S")
        
    def test_multiple_cars(self):
        simulation = Simulation()
        simulation.create_grid(10, 10)
        car_a = Car("A", 0, 0, "E", list("FFRFF"))
        car_b = Car("B", 1, 1, "N", list("FFLFF"))
        car_c = Car("C", 2, 2, "W", list("FFRFF"))
        simulation.add_car(car_a)
        simulation.add_car(car_b)
        simulation.add_car(car_c)
        simulation.run_simulation()
        self.assertEqual(car_a.x, 2)
        self.assertEqual(car_a.y, 0)
        self.assertEqual(car_a.direction, "S")
        self.assertEqual(car_b.x, 1)
        self.assertEqual(car_b.y, 2)
        self.assertEqual(car_b.direction, "N")
        self.assertEqual(car_c.x, 1)
        self.assertEqual(car_c.y, 2)
        self.assertEqual(car_c.direction, "W")

    def test_collision(self):
        simulation = Simulation()
        simulation.create_grid(10, 10)
        car_a = Car("A", 1, 2, "N", list("FFRFFFFRRL"))
        car_b = Car("B", 7, 8, "W", list("FFLFFFFFFF"))
        simulation.add_car(car_a)
        simulation.add_car(car_b)
        simulation.run_simulation()
        self.assertTrue(car_a.collided)
        self.assertTrue(car_b.collided)
        self.assertEqual(car_a.x, 5)
        self.assertEqual(car_a.y, 4)
        self.assertEqual(car_b.x, 5)
        self.assertEqual(car_b.y, 4)

    def test_boundary_check(self):
        simulation = Simulation()
        simulation.create_grid(5, 5)
        car = Car("C", 0, 0, "S", list("FFFFF"))
        simulation.add_car(car)
        simulation.run_simulation()
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 0)

    def test_complex_commands(self):
        simulation = Simulation()
        simulation.create_grid(10,10)
        car = Car("D", 0, 0, "E", list("FRFRFRFR"))
        simulation.add_car(car) 
        simulation.run_simulation()
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 1)
        self.assertEqual(car.direction, "E")

if __name__ == '__main__':
    unittest.main()