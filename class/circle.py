import math

class Circle:

    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.cx = cx
        self.cy = cy
         
    def area(self):
        answer = float(self.radius) * float(self.radius) * math.pi
        return round(answer,2)

    def center(self):
        return ("({}, {})".format(self.cx, self.cy))



def main():
    radius = input("반지름 : ")
    cx = float(input("x좌표 : "))
    cy = float(input("y좌표 : "))

    #class 생성
    circle = Circle(radius, cx, cy)
    #정보 출력
    print("*****************")
    print("원의 중심 => {}".format(circle.center()))
    print("원의 넓이 => {}".format(circle.area()))
    print("*****************")


if __name__ == "__main__":
    main()










