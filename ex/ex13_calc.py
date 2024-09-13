class MyError(Exception):
    # 출력문에 관여하는 함수
    # 프린트 할 때 얘 실행되는거임
    def __str__(self) -> str:
        return '에러가 입력되었습니다.'

def say_nick(nick):
    if nick == '에러':
        # 에러를 유발시키는거임
        # 에러를 발생시키는 코드
        # raise : 오류를 강제로 발생시키는 코드
        raise MyError()
    print(f"nick :{nick}")


say_nick('실행')
try:
    say_nick('에러')
except MyError as me :
    print(f"say_nick() 에러:{me}")
finally:
    
    print("="*60)


class 계산기():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def 더하기(self):
        print(self.num1 +self.num2)
    def 빼기(self):
        print(self.num1-self.num2)
    def 곱하기(self):
        print(self.num1*self.num2)
    def 나누기(self):
        print(self.num1/self.num2)
    def 나머지(self):
        print(self.num1%self.num2)
    def 정수만(self):
        print(self.num1//self.num2)

class 공학용계산기(계산기):
    def __init__(self,num1,num2,num3) -> None:
        super().__init__(num1,num2)
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def 더하기(self):
        return self.num1+self.num2+self.num3
# 모듈이 직접 실행되었는지를 판단
# 구분하는데 사용하는 특별한 변수
print(f"네임 출력 : {__name__}")
# 모듈이 직접 실행되면 name 이 __main__ 으로 지정됨
if __name__ == '__main__' :
    try:
        a = 공학용계산기(5,2,3)
        print(f"더하기 : {a.더하기()}")
        a.빼기()
        a.곱하기()
        a.나누기()
        a.나머지()
        a.정수만()
    except TypeError as te:
        print(te)
        print("에러남에러남에러남에러남에러남에러남에러남에러남에러남")
        
    else:
        print("굿")
    finally:
        print("프로그램을 종료합니다.")

        
    try :
        num = 10/2
    except ValueError as err:
        print(f"err: {err}")
    except ZeroDivisionError as ve:
        print(f"err: {ve}")
    except :
        print("error,,")
    else:
        print("오류안남")
        print(num)
    finally:
        print("프로그램 종료")
    
# 내가 직접 만든 예외
# Exception 클래스를 상속하여 사용자 정의 예외클래스를 정의 할 수 있다.





#init에는 매개변수 넣어놨는데 여기서 안넣어두면 오류남 
# try - except 
# 정해놓은 오류만 처리하고 -오류 메세지
# try - 오류가 발생할 가능성이 있는
# except- 오류가 발생
# else- 오류가 발생하지 않으면 실행
# finally - 언제나 실행
# 

# try:
#     a =계산기(57,5)
#     a.더하기()
#     a.빼기()
#     a.곱하기()
#     a.나누기()
#     a.정수만()
#     a.나머지()
#     a.fake()
# except Exception as e :
#     print("오류남")
#     pass
# else:
#     print("오류안남")
# finally:
#     print("프로그램 종료")

# try :
#     num = 10/0
# except ZeroDivisionError as err:
#     print(f"err: {err}")
#     pass
# else:
#     print("오류안남")
#     print(num)
# finally:
#     print("프로그램 종료")
