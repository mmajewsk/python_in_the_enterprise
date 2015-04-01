import unittest
import flight

class PlaneTest(unittest.TestCase):
	def test_init(self):
		plane = flight.Plane()
		self.assertEqual(plane.minima,-5)
		self.assertEqual(plane.maxima,5)
		self.assertEqual(plane.middle,0)
		self.assertEqual(plane.orientation,0)

	def test_init_with_args(self):
		plane = flight.Plane(range_of_tilt = (1,7))
		self.assertEqual(plane.minima,1)
		self.assertEqual(plane.maxima,7)
		self.assertEqual(plane.middle,4)
		self.assertEqual(plane.orientation,0)

	def setUp(self):
		self.test_plane1 = flight.Plane()
		self.test_plane2 = flight.Plane(range_of_tilt = (1,7))

	def test_tilt(self):
		result1 = self.test_plane1.tilt()
		result2 = self.test_plane2.tilt()
		self.assertTrue(isinstance(result1,(int,long,float,complex)))
		self.assertTrue(isinstance(result2,(int,long,float,complex)))

	def test_fly(self):
		number_of_desired_simulation_steps = 4
		iterator1 = xrange(number_of_desired_simulation_steps)
		orientation = self.test_plane1.orientation
		actual_number_of_steps = 0
		for v in self.test_plane1.fly(iterator1):
			orientation2 = self.test_plane1.orientation
			self.assertNotEqual(orientation2,orientation)
			self.assertTrue(v)
			orientation = orientation2
			actual_number_of_steps += 1
		self.assertEqual(actual_number_of_steps,number_of_desired_simulation_steps)

class FlightCorrectorSimulatorTest(unittest.TestCase):
	def setUp(self):
		self.plane = flight.Plane()

	def test_init(self):
		simulator = flight.FlightCorrectorSimulator(self.plane)
		self.assertEqual(simulator.plane,self.plane)


if __name__ == "__main__":
	unittest.main()