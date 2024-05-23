class Rectangle:
        height: int
        width: int

def getPerimeter(self):
        perimeter = self.height * 2 + self.width * 2
        return perimeter
def getArea(self):
        area = self.height * 2 + self.width * 2
        return area
def getStr(self):
        s = ""
        w = "*" * self.width + "\n"
        s += w
        for i in range (self.height - 2):
            s += "*"
            s += " " * (self.width -2)
            s += "*\n"
        s += w
        return s
def main():
    print("Retangle Calculator")
    print()

    again = "y"
    while again.lower() == "y":
           height = int(input("Height:  "))
           width = int(input("Width:  "))

           rectangle = Rectangle(height, width)
           print("Perimeter:", rectangle.getPermeter())
           print("Area:  ", rectangle.getArea())
           print(rectangle. getStr())

           again = input("Continue? (y/n): ") .lower()
           print()
    print("Bye!")

if __name__=="__main__": 
       main()

