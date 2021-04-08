class Rectangle:
    def __init__(self, x,y,width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def __str__(self):
        return f"x={self.x} y={self.y} width={self.width} height={self.height}"

rectangle = Rectangle(5, 10, 50, 100)
print(rectangle)