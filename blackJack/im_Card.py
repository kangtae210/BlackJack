#카드 클래스 생성
class Card:
    name = ""
    shape = ""
    value1 = 0
    value2 = 0
    value_list = []
    status = True       #True:숨기기, False : 공개하기
    def __init__(self, shape,  name, value1, value2, status):
        self.shape = shape
        self.name = name
        self.value1 = value1
        self.value2 = value2
        self.status = status
        self.value_list = [value1, value2]

    def open_card(self):
        self.status = False