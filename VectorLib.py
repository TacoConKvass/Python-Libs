from math import sin, cos, acos, sqrt, pi

class Vector2:
	def __init__(self, x: float, y: float) -> None:
		self.x: float = float(x)
		self.y: float = float(y)
		self.length: float = self.GetLength()
		
	def GetLength(self) -> float:
		return sqrt( (self.x ** 2) + (self.y ** 2) )
		
	def show(self) -> list:
		return [self.x, self.y]
		
	def __str__(self) -> str:
		return str(self.show())
	
	def __add__(self, secondVector: 'Vector2') -> 'Vector2':
		return Vector2(self.x + secondVector.x, self.y + secondVector.y)
		
	def __sub__(self, secondVector: 'Vector2') -> 'Vector2':
		return Vector2(self.x - secondVector.x, self.y - secondVector.y)
		
	def __neg__(self) -> 'Vector2':
		return Vector2(-self.x, -self.y)
		
	def __mul__(self, magnitude: float) -> 'Vector2':
		return Vector2(self.x * magnitude, self.y * magnitude)
		
	def __truediv__(self, divider: float) -> 'Vector2':
		return Vector2(self.x / divider, self.y / divider)
		
	def __floordiv__(self, divider: float) -> 'Vector2':
		return Vector2(self.x // divider, self.y // divider)
		
	def __mod__(self, modulo: float) -> 'Vector2':
		return Vector2(self.x % modulo, self.y % modulo)
		
	def __pow__(self, exponent: float) -> 'Vector2':
		return Vector2(self.x ** exponent, self.y ** exponent)
		
	def __round__(self, afterComma: int = 1) -> 'Vector2':
		return Vector2(float(round(self.x, afterComma)), float(round(self.y, afterComma)))

	def __invert__(self) -> 'Vector2':
		return Vector2(self.y, self.x)
		
	def __lt__(self, secondVector: 'Vector2') -> bool:
		return self.length < secondVector.length
		
	def __le__(self, secondVector: 'Vector2') -> bool:
		return self.length <= secondVector.length
		
	def __gt__(self, secondVector: 'Vector2') -> bool:
		return self.length > secondVector.length
		
	def __ge__(self, secondVector: 'Vector2') -> bool:
		return self.length >= secondVector.length
		
	def __eq__(self, secondVector: 'Vector2') -> bool:
		return self.length == secondVector.length
		
	def __ne__(self, secondVector: 'Vector2') -> bool:
		return self.length != secondVector.length
	
	def GetAngle(self) -> float:
		if self.y < 0:
			return 2 * pi - acos(self.x / self.length)
		return acos(self.x / self.length)
		
	def RotatedTowards(self, angleInRadians: float) -> 'Vector2':
		if angleInRadians == pi:
			return Vector2(-self.length, 0)
			
		if angleInRadians == pi/2:
			return Vector2(0, self.length)
			
		if angleInRadians == pi*3/2:
			return Vector2(0, -self.length)
			
		return Vector2(cos(angleInRadians) * self.length, sin(angleInRadians) * self.length)
		
	def RotatedBy(self, angleInRadians: float) -> 'Vector2':
		return self.RotatedTowards(self.GetAngle() + angleInRadians)

class Vector3:
	def __init__(self, x: float, y: float, z: float) -> None:
		self.x: float = float(x)
		self.y: float = float(y)
		self.z: float = float(z)
		self.length: float = self.GetLength()
		
	def GetLength(self) -> float:
		return sqrt( (self.x ** 2) + (self.y ** 2) + (self.z ** 2) )
		
	def show(self) -> list:
		return [self.x, self.y, self.z]
		
	def __str__(self) -> str:
		return str(self.show())
	
	def __add__(self, secondVector: 'Vector3') -> 'Vector3':
		return Vector3(self.x + secondVector.x, self.y + secondVector.y, self.z + secondVector.z)
		
	def __sub__(self, secondVector: 'Vector3') -> 'Vector3':
		return Vector3(self.x - secondVector.x, self.y - secondVector.y, self.z - secondVector.z)
		
	def __neg__(self) -> 'Vector3':
		return Vector3(-self.x, -self.y, -self.z)
		
	def __mul__(self, magnitude: float) -> 'Vector3':
		return Vector3(self.x * magnitude, self.y * magnitude, self.z * magnitude)
		
	def __truediv__(self, divider: float) -> 'Vector3':
		return Vector3(self.x / divider, self.y / divider, self.z / divider)
		
	def __floordiv__(self, divider: float) -> 'Vector3':
		return Vector3(self.x // divider, self.y // divider, self.z // divider)
		
	def __mod__(self, modulo: float) -> 'Vector3':
		return Vector3(self.x % modulo, self.y % modulo, self.z % divider)
		
	def __pow__(self, exponent: float) -> 'Vector3':
		return Vector3(self.x ** exponent, self.y ** exponent, self.z ** exponent)
		
	def __round__(self, afterComma: int = 1) -> 'Vector3':
		return Vector3(float(round(self.x, afterComma)), float(round(self.y, afterComma)), float(round(self.z, afterComma)))

	def __invert__(self) -> 'Vector3':
		return Vector3(self.z, self.y, self.x)
		
	def __lt__(self, secondVector: 'Vector3') -> bool:
		return self.length < secondVector.length
		
	def __le__(self, secondVector: 'Vector3') -> bool:
		return self.length <= secondVector.length
		
	def __gt__(self, secondVector: 'Vector3') -> bool:
		return self.length > secondVector.length
		
	def __ge__(self, secondVector: 'Vector3') -> bool:
		return self.length >= secondVector.length
		
	def __eq__(self, secondVector: 'Vector3') -> bool:
		return self.length == secondVector.length
		
	def __ne__(self, secondVector: 'Vector3') -> bool:
		return self.length != secondVector.length
	
	def GetAngles(self) -> float:
		if self.length == 0:
			return [0.0, 0.0]
		leng_xy = ( (self.x ** 2) + (self.y ** 2) )
		if leng_xy == 0:
			angle_x = 0
		else:
			angle_x = acos(self.x / leng_xy) if self.y > 0 else 2*pi - acos(self.x / leng_xy)
		angle_z = acos(self.z / self.length) if self.x > 0 else 2*pi - acos(self.z / self.length)
		return [angle_x, angle_z]