from math import pi, radians as rad, sqrt

if __name__ == '__main__':
	from VectorLib import Vector2
else:
	from Lib.VectorLib import Vector2


class Rectangle:
	def __init__(self, width: float, height: float, center: Vector2 = Vector2(0, 0), rotation: float= 0) -> None:
		self.center = center
		self.width = width
		self.height = height
		self.vertices = [ Vector2(width/2, height/2),
						Vector2(width/2, -height/2),
						Vector2(-width/2, -height/2),
						Vector2(-width/2, height/2) ]
									
	def GetVertices(self) -> list:
		return [vector.show() for vector in self.vertices]
		
	def RotatedBy(self, angleInRadians: float) -> 'Rectangle':
		rotatedRect = Rectangle(self.width, self.height)
		rotatedRect.vertices = [vector.RotatedBy(angleInRadians) for vector in self.vertices]
		return rotatedRect

	def GetArea(self):
		return self.width * self.height
	
	def __str__(self) -> str:
		return str(self.GetVertices())

class Line:
	def __init__(self, length: float, center: Vector2 = Vector2(0, 0)) -> None:
		self.center = center
		self.length = length
		self.vertices = [ Vector2(0, length / 2), Vector2(0, -length / 2)]
	
	def GetVertices(self) -> list:
		return [vector.show() for vector in self.vertices]

	def RotatedBy(self, angleInRadians: float) -> 'Line':
		rotatedLine = Line(self.length)
		rotatedLine.vertices = [vector.RotatedBy(angleInRadians) for vector in self.vertices]
		return rotatedLine

	def __str__(self) -> str:
		return str(self.GetVertices())

class Circle:
	def __init__(self, radius: float, center: Vector2 = Vector2(0, 0)) -> None:
		self.center = center
		self.radius = radius
		self.vertices = self.GenerateVertices()

	def GenerateVertices(self) -> list:
		return [Vector2(self.radius, 0).RotatedBy(rad(x * 9)) for x in range(0, 40)]

	def GetVertices(self) -> list:
		return [vector.show() for vector in self.vertices]

	def RotatedBy(self, angleInRadians: float) -> 'Circle':
		rotatedCircle = Circle(self.radius)
		rotatedCircle.vertices = [vector.RotatedBy(angleInRadians) for vector in self.vertices]
		return rotatedCircle

	def GetArea(self):
		return pi * self.radius**2

	def __str__(self) -> str:
		return str(self.GetVertices())

class Triangle:
	def __init__(self, side: float, center: Vector2 = Vector2(0,0)) -> None:
		self.side = side
		self.center = center
		self.height = self.side * sqrt(3) / 2
		self.vertices = self.GenerateVertices()

	def GenerateVertices(self) -> list:
		return [Vector2(0, self.height * 2 / 3).RotatedBy(rad(x * 120)) for x in range(0, 3)]
	
	def GetVertices(self) -> list:
		return [vector.show() for vector in self.vertices]

	def RotatedBy(self, angleInRadians: float) -> 'Triangle':
		rotatedTriangle = Triangle(self.side)
		rotatedTriangle.vertices = [vector.RotatedBy(angleInRadians) for vector in self.vertices]
		return rotatedTriangle

	def GetArea(self):
		return self.side * self.height / 2

	def __str__(self) -> str:
		return str(self.GetVertices())