class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [(0,0)] 

for point in points:
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")