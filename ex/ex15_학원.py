# 학원
# 교실
# 학생
# 강사

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def __str__(self) -> str:
        return f"선생님 이름 :{self.name} ,과목 :{self.subject}"

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def __str__(self) -> str:
        return f"학생 이름 : {self.name}, 과목 : {self.student_id}"
        
        
class 학원:
    name = '휴먼컴퓨터 학원'

    def __init__(self) -> None:
        self.teacher = None
        self.students = []
    
    def add_teacher(self,teacher):
        self.teacher = teacher

    def add_student(self,student):
        self.students.append(student)
        
    def add_students(self, students) :
        self.students += students
        
    def get_teacher_info(self):
        return self.teacher.__str__()

    def get_students_info(self) -> str:
        s_str = ''
        for s in self.students:
            s_str += s.__str__() +"\n"
        return s_str
    
    def __str__(self) -> str:
        s = self.name + "\n"+ self.get_teacher_info() + "\n" + self.get_students_info()
        return s



# 자바로 치면 메인 메서드랑 비슷한 역할
# 다른 모듈에서 실행할경우 실행하지 않음 
if __name__ == '__main__' :

    t = Teacher("오미선","컴무터")
    
    s1 = Student("김윤상",1)
    s2 = Student("김뮤사",2)
    s3 = Student("고미스",3)
    s4 = Student("크레용",4)
    s5 = Student("팝팝팝",5)
    a = 학원()
    a.add_student(s1)
    a.add_student(s2)
    a.add_student(s3)
    a.add_student(s4)
    a.add_student(s5)
    a.add_teacher(t)
    
    print(a.get_students_info())
    print(a.get_teacher_info())
    print("전부 출력===============================")
    print(a.__str__())
    
    import csv
    f = open("ex/학원명단.txt","r",encoding="utf-8")
    read = csv.reader(f)
    x=[]
    y=[]
    z={}
    for i in read:
        print(i[0])
        x.append(i[0].replace("학생 이름 :","").split(","))
        y.append(i[1])
    print(x)

    print("="*60)

# 텍스트에 학생, 선생님 파일 정보 넣어놓고 긁어오기

# class 교실():
#     def __init__(self, 반, 인원수):
#         self.반 = 반
#         self.인원수 = 인원수