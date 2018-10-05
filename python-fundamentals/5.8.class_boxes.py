'''8.	Boxes
Create a class Box, which will represent a rectangular box. The Box should have UpperLeft (Point), UpperRight (Point), BottomLeft (Point), BottomRight (Point).
Create, or use from the Lab, the class Point which has X (int) and Y (int) – coordinates in 2D space. Move the CalculateDistance() method in the Point class, exactly as it is. Then use “Point.CalculateDistance(point1, point2)” signature, to use the method.
Create 2 methods in the Box class:
CalculatePerimeter(width, height)
CalculateArea(width, height).
Make them return integers, representing the perimeter and area of the box.
The formulas are respectively – (2 * Width + 2 * Height) and (Width * Height).
The Width is the distance between the UpperLeft and the UpperRight Points, and ALSO – the Bottomleft and the BottomRight Points.
The Height is the distance between the UpperLeft and the BottomLeft Points, and ALSO – the UpperRight and the BottomRight Points.
You will receive several input lines in the following format:
{X1}:{Y1} | {X2}:{Y2} | {X3}:{Y3} | {X4}:{Y4}
Those will be the coordinates to UpperLeft, UpperRight, BottomLeft and BottomRight (IN THE SAME ORDER).
When you receive the command “end”. You must print all Boxes in the following format:
“Box: {width}, {height}
 Perimeter: {perimeter}
 Area: {area}”
Examples
Input	Output
0:2 | 2:2 | 0:0 | 2:0
-3:0 | 0:0 | -3:-3 | 0:-3
-2:2 | 2:2 | -2:-2 | 2:-2
end

Output
Box: 2, 2
Perimeter: 8
Area: 4
Box: 3, 3
Perimeter: 12
Area: 9
Box: 4, 4
Perimeter: 16
Area: 16
'''
from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def measure_distance(self, other_point):
        x = abs(self.x - other_point.x)
        y = abs(self.y - other_point.y)
        return sqrt(x ** 2 + y ** 2)


class Box:
    def __init__(self, u_l_p, u_r_p, b_l_p, b_r_p):
        self.u_l_p = u_l_p
        self.u_r_p = u_r_p
        self.b_l_p = b_l_p
        self.b_r_p = b_r_p
        self.width = Point.measure_distance(self.u_l_p, self.u_r_p)
        self.height = Point.measure_distance(self.u_l_p, self.b_l_p)
        self.perimeter = self.width * 2 + self.height * 2
        self.area = self.width*self.height


data = input()
list_boxes = []

while data != "end":
    upper_left = data.split(" | ")[0]
    upper_right = data.split(" | ")[1]
    bottom_left = data.split(" | ")[2]
    bottom_right = data.split(" | ")[3]

    upper_left_point = Point(int(upper_left.split(":")[0]), int(upper_left.split(":")[1]))
    upper_right_point = Point(int(upper_right.split(":")[0]), int(upper_right.split(":")[1]))
    bottom_left_point = Point(int(bottom_left.split(":")[0]), int(bottom_left.split(":")[1]))
    bottom_right_point = Point(int(bottom_right.split(":")[0]), int(bottom_right.split(":")[1]))

    myBox = Box(upper_left_point, upper_right_point, bottom_left_point, bottom_right_point)
    list_boxes.append(myBox)
    data = input()

for box in list_boxes:
    print(f"Box: (int(box.width)),(int(box.height))")
    print(f"Perimeter: (int(box.perimeter))")
    print(f"Area: (int(box.area))")




