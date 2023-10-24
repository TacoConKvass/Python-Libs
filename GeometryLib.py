from math import pi
from VectorLib import Vector2

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