from Lib.VectorLib import Vector2
from Lib.GeometryLib import *
from enum import Enum
from time import sleep
from math import radians
import turtle as t

FPS = 60
UNITS_TO_METERS = 100

class Color(Enum):
    Red = (1., 0., 0.)
    Green = (0., 1., 0.)
    Blue = (0., 0., 1.)
    Yellow = (1., 1., 0.)
    Cyan = (0., 1., 1.)
    Magenta = (1., 0., 1.)
    White = (1., 1., 1.)
    Black = (0., 0., 0.)
    Gray = (.3, .3, .3)

def TurtleSetup():
    t.ht()
    t.pencolor('white')
    t.bgcolor('black')
    t.pensize = 1
    t.speed(0)
    t.tracer(0, 0)
    
def Intersects(shape: object, shape2: object) -> bool:
	return False

def DrawFrame(shape: object, rgb: tuple = (1.0, 1.0, 1.0)) -> None:
    if type(shape) not in [Rectangle, Circle, Line, Triangle, Polygon]:
        return

    last_vertice_id = len(shape.vertices) - 1

    t.pencolor(rgb)
    t.pu()
    t.setpos( ((shape.center + shape.vertices[last_vertice_id]) * UNITS_TO_METERS).show() )
    t.pd()
    for vertice in shape.vertices:
        t.setpos( ((shape.center + vertice) * UNITS_TO_METERS).show() )

def DrawFace(shape: object, rgb: tuple = (1.0, 1.0, 1.0)) -> None:
    if type(shape) not in [Rectangle, Circle, Triangle, Polygon]:
        return

    last_vertice_id = len(shape.vertices) - 1

    t.fillcolor(rgb)
    t.pu()
    t.setpos( ((shape.center + shape.vertices[last_vertice_id]) * UNITS_TO_METERS).show() )
    t.begin_fill()
    for vertice in shape.vertices:
        t.setpos( ((shape.center + vertice) * UNITS_TO_METERS).show() )
    t.end_fill()
    
    
def RunMainLoop(objects: list, colors: list) -> None:
    TurtleSetup()
    while True:
        t.clear()
        for element in object_list:
            current = object_list.index(element)
            color = colors[current].value

            if (type(element) in [Rectangle, Triangle]) or (type(element) == Polygon and len(element.vertices) >= 3):
                DrawFace(element, color)
            else:
                DrawFrame(element, color)

            object_list[current] = element.RotatedBy(radians(60)/FPS) if type(element) == Circle else element.RotatedBy(radians(-60)/FPS)

            if type(element) == Polygon:
                object_list[current].center = object_list[0].vertices[(current* 10)-1]

        t.update()
        sleep(1/FPS)

obj = Circle(2)
obj2 = Polygon()
obj3 = Polygon()
obj4 = Polygon()
object_list = [obj, obj2, obj3, obj4]
color_list = [Color.White, Color.Red, Color.Green, Color.Blue]
RunMainLoop(object_list, color_list)
