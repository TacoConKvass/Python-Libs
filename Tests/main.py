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


def DrawFrame(shape: object, rgb: tuple = (1.0, 1.0, 1.0)) -> None:
    if type(shape) not in [Rectangle, Circle, Line, Triangle]:
        return

    last_vertice_id = len(shape.vertices) - 1

    t.pencolor(rgb)
    t.pu()
    t.setpos( ((shape.center + shape.vertices[last_vertice_id]) * UNITS_TO_METERS).show() )
    t.pd()
    for vertice in shape.vertices:
        t.setpos( ((shape.center + vertice) * UNITS_TO_METERS).show() )

def DrawFace(shape: object, rgb: tuple = (1.0, 1.0, 1.0)) -> None:
    if type(shape) not in [Rectangle, Circle, Triangle]:
        return

    last_vertice_id = len(shape.vertices) - 1

    t.fillcolor(rgb)
    t.pu()
    t.setpos( ((shape.center + shape.vertices[last_vertice_id]) * UNITS_TO_METERS).show() )
    t.begin_fill()
    for vertice in shape.vertices:
        t.setpos( ((shape.center + vertice) * UNITS_TO_METERS).show() )
    t.end_fill()

TurtleSetup()
obj = Rectangle(3, 1)
obj2 = Triangle(3)
obj3 = Line(3)
object_list = [obj2, obj, obj3]

while True:
    t.clear()
    for element in object_list:
        current = object_list.index(element)
        color = Color.Gray.value if type(element) == Rectangle else Color.Yellow.value if type(element) == Line else Color.White.value

        if type(element) in [Rectangle, Triangle]:
            DrawFace(element, color)
        else:
            DrawFrame(element, color)

        object_list[current] = element.RotatedBy(radians(60)/FPS) if type(element) == Triangle else element.RotatedBy(radians(-60)/FPS)

        if type(element) == Line:
            object_list[current].center = object_list[0].vertices[2]
    t.update()
    sleep(1/FPS)