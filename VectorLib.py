from math import sin, cos, acos, sqrt, pi

class Vector2:
	def __init__(self, x: float, y: float):
		self.x: float = float(x)
		self.y: float = float(y)
		self.length: float = self.GetLength()
		
	def GetLength(self) -> float:
		return sqrt( (self.x ** 2) + (self.y ** 2) )
		
	def show(self) -> list:
		return [self.x, self.y]
		
	def __str__(self):
		return str(self.show())
	
	def __add__(self, secondVector):
		return Vector2(self.x + secondVector.x, self.y + secondVector.y)
		
	def __sub__(self, secondVector):
		return Vector2(self.x - secondVector.x, self.y - secondVector.y)
		
	def __neg__(self):
		return Vector2(-self.x, -self.y)
		
	def __mul__(self, magnitude: float):
		return Vector2(self.x * magnitude, self.y * magnitude)
		
	def __truediv__(self, divider: float):
		return Vector2(self.x / divider, self.y / divider)
		
	def __floordiv__(self, divider: float):
		return Vector2(self.x // divider, self.y // divider)
		
	def __mod__(self, modulo: float):
		return Vector2(self.x % modulo, self.y % modulo)
		
	def __pow__(self, exponent: float):
		return Vector2(self.x ** exponent, self.y ** exponent)
		
	def __round__(self, afterComma: int = 1):
		return Vector2(float(round(self.x, afterComma)), float(round(self.y, afterComma)))

	def __invert__(self):
		return Vector2(self.y, self.x)
		
	def __lt__(self, secondVector):
		return self.length < secondVector.length
		
	def __le__(self, secondVector):
		return self.length <= secondVector.length
		
	def __gt__(self, secondVector):
		return self.length > secondVector.length
		
	def __ge__(self, secondVector):
		return self.length >= secondVector.length
		
	def __eq__(self, secondVector):
		return self.length == secondVector.length
		
	def __ne__(self, secondVector):
		return self.length != secondVector.length
	
	def GetAngle(self) -> float:
		return acos(self.x / self.length)
		
	def RotatedTowards(self, angleInRadians: float):
		angleInRadians %= 2*pi
		
		if angleInRadians < 0:
			angleInRadians+= 2*pi
		
		if angleInRadians == pi:
			return Vector2(-self.length, 0)
			
		if angleInRadians == pi/2:
			return Vector2(0, self.length)
			
		if angleInRadians == pi*3/2:
			return Vector2(0, -self.length)
			
		return Vector2(cos(angleInRadians) * self.length, sin(angleInRadians) * self.length)
		
	def RotatedBy(self, angleInRadians: float):
		return self.RotatedTowards(self.GetAngle() + angleInRadians )