# 반복 가능한 객체 vs 반복 객체
# 이더레이터(iterator) = 반복객체
# next() 함수 호출 시 다음 요소 반환하는 객체/
# 근데 얜 특이한게 거기서 끝나는게 아니라 값이 저장되던데

# 반복 가능(iterable) 객체
# 반복문을 통해 반복처리 가능한놈
# 리스트, 튜플, 딕셔너리

# 반복 가능객체로부터 반복 객체를 반환 하는 함수
from itertools import tee
list = [1, 2, 3]
iter_list = iter(list)  # 리스트로부터 반복자 생성
a, b= tee(iter_list)
# 호출 할 때 next 
# 더 이상 반환할 요소가 없으면 StopIteration 예외를 발생시킵니다.
print(type(a))
print(next(a))
print(next(a))
print(next(a))
# 두번이상 순회 하고 싶으면 tee()를 사용하세요
print("반복가능객체================")
    
class 반복가능객체:

    def __init__(self,data) -> None:
        self.data = data
        self.position = 0
    # 반복 가능 객체는 보통 클래스의 객체(인스턴스를) 반환(자기자신self)
    def __iter__(self):
        return self
    # 다음값을 계속해서 반환하기위해 1씩 증가
    def __next__(self):
        # 반복할값 >= 데이터값
        # 반복할게 없잖슴 예외 ㄱㄱ
        if self.position >= len(self.data):
            # 예외를 발생 시켜줘
            raise StopIteration
        x = self.data[self.position]
        self.position += 1
        return x
    
list = 1,2,3,4,6
cl = iter(반복가능객체(list))
print(next(cl))
print(next(cl))
print(next(cl))
print(next(cl))
print(next(cl))
print(next(cl))