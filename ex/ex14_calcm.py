# 모든 클래스, 변수, 코드가 실행됨
# import ex13_calc
# from 파일의 이름 import 사용할클래스이름
"""
from ex13_calc import 계산기
# 여기서 구분해놓은 name 은 ex13_calc이걸로 나오네요
# __main__을 실행하지 않아서 안나온다
calc = 계산기(20,11)
print("calcm =============")
calc.더하기()
calc.빼기()
calc.곱하기()
calc.나누기()"""
import ex13_calc
calc = ex13_calc.계산기(1,2)
calc.더하기()