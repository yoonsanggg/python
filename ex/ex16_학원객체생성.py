
with open("ex/명단.json","r",encoding="utf-8") as f :
    from  ex15_학원 import 학원,Teacher,Student
    import json

    obj = json.load(f)
    print(obj['강사']['이름'])
    print(obj['학생'][0]['이름'])
    teacher = obj['강사']
    student = obj['학생']
    # print(f"이름: {teacher['이름']}, 과목: {teacher["과목"]}")
    t = Teacher(teacher['이름'], teacher['과목'])
    print(t)
    students =[]
    for i in student:
        print(i['이름'])
        print(i['학번'])
        student = Student(i['이름'],i['학번'])
        students.append(student)
    
    a= 학원()
    a.add_teacher(t)
    a.add_students(students)
    print(a)
    
    
    #     s1 = s(x,y)
    #     a.add_student(s1)
    # print(a.get_students_info())
    
