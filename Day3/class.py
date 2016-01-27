class Vehicle(object):
	def __init__(self, engine_type, **kwargs):
		self.engine_type = engine_type
		for k, v in kwargs.items():
			setattr(self, k, v)
			 #self[k] = v

	def set_color(self, color):
		self.color = color

	def set_speed(self, speed):
		self.speed = speed
class Car(Vehicle):
	"""docstring for ClassName"""
	def __init__(self, car_category, engine_type, **kwargs):
		super(Car,self).__init__(engine_type, **kwargs)
		#self.arg = arg
		self.car_category = car_category
		self.doors = 5
		self.wheels = 4
#create an object
my_car = Car('VIT-120', 'saloon', engine_cc=1500, color='red', max_speed=120)
#my_car.car_category = "saloon"

print my_car.max_speed
print my_car.color
print my_car.engine_cc

