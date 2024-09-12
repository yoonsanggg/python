class 차():
    
    def __init__(self,whell,price):
        self.whell = whell
        self.price = price
        
class 자전차(차):
    def __init__(self,whell,price) :
        super().__init__(whell,price)

bicy = 자전차(2,100)
print(bicy.price)







"""human = 사람()
human.cry("엉엉")

human.cry("ㄱㅈㅇㅇㅇㅇㅇㅇ")

human.call("김찰서","010-1234-4567")

human.구구단(4,5)

human.개인정보("감윤상")

"""