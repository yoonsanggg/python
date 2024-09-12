class MyClass:
    pass
# 클래스의 인스턴스를 생성
myClass = MyClass()
myClass2 = MyClass()

# 인스턴스마다 각각 다른 정보를 저장 할 수 있다.
print(myClass is myClass2)

class MyClass:
    # 생성자는 매개값으로 self 받아와야함
    # self 매개변수 : 생성된 객체를 참조 (this랑 비슷함), 인스턴스변수, 메서드에 접근
    def __init__(self, *args, **kwargs):
        print('MyClass 생성자 호출')
        
#이렇게 실행? 
myClass = MyClass()
class MyClass:
    # 클래스 변수
    var = '파이썬 클래스'
    # 반환타입 명시 : None - void랑 같음
    #       타입힌트는 필수는 아니지만 코드의 가독성을 높이고 코드의 오류를 발견하는데 도움을 줄수 있다
    def __init__(self, name) -> None:
        self.instance_var = "인스턴스 변수"
        self.name = name
        
    # 클래스 변수는 따로 접근해서 바꾸면 인스턴스 변수 설정한것과 다름 없으니...
    # 클래스 자체 수정, 클래스 관련 정보 반환하려면 이렇게 
    # 데코레이터(어노테이션) 잡아줘야 첫번째 매개변수랑 클래스랑 연결됨
    # 지금은 cls와 클래스가 연결 됐으니 .찍고var 하면 접근..
    @classmethod
    def set_class_var(cls, value):
        cls.var = value
    
    # 생성하지 않고 사용 ㄱㄱ혓 / 정적메서드
    @staticmethod
    def static_method():
        return "정적 메서드"
        
        # 인스턴스에 종속적
        # MyClass()를  생성하면 클래스 안의 값 무한증식 가능
        # 인스턴스 변수는 생성자를 통해 초기화됨 
        # MyClass(여기서 초기화) , 혹은 직접 접근해서 바꿔주던가
print(MyClass.static_method())
print("="*90)
myClass = MyClass('2교육장')
myClass1 = MyClass('1교육장')
print(myClass1.name)
print(myClass.name)
print(f"instance_var: {myClass.instance_var}")

myClass.instance_var = '값 변경'
print(f"instance_var: {'걍마클',myClass.instance_var}")
print(f"instance_var: {'마클1',myClass1.instance_var}")
myClass1.instance_var = '나인원'
print(f"instance_var: {'마클1',myClass1.instance_var}")
# 인스턴스 변수 - 각각 인스턴스마다
# 클래스 변수 - 인스턴스가 공유하는 변수 (같은 값 유지)
print(f"var: {myClass.var}")
print(f"var: {myClass1.var}")
# class
myClass.set_class_var("합치냐?")
print(f"var: {myClass.var}")
print(f"var: {myClass1.var}")
# 근데 인스턴스 변수를 생성해 버리면 사라져 버리는...
# 인스턴스 변수를 생성했다? 넌 나가라

# 이렇게 한게 인스턴스 변수를 생성
myClass.var = "0가냐?"
print(f"var: {myClass.var}")
print(f"var: {myClass1.var}")
myClass1.var = "1간다?"
print(f"var: {myClass.var}")
print(f"var: {myClass1.var}")

myClass.set_class_var("합치냐?")
print(f"var: {myClass.var}")
print(f"var: {myClass1.var}")

# 서로의 값을 공유하지 않음 - 인스턴스 변수


class myClass:
    def __init__(self):
        self.instance ="갈게"
    @classmethod
    def set_class_var(cls,value):
        cls.var = value
hi = myClass()
print(hi.instance)
hi.instance="진짜 갈게"
print(hi.instance)
