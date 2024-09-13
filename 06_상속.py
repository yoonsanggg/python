class ParentClass() :
    def parent_method(self):
        return "찐부모클래스의 메서드"

# 자식클래스에서 부모클래스를 지정
class ChildClass(ParentClass) :
    def child_method(self):
        return "난 자식인데요?"
        # 자바에서 setter랑 똑같은가?
    def parent_method(self):
        return "자식에서 재정의한 부모 ㄷㄷ"
cc = ChildClass()

print(cc.child_method())
# 자식클래스의 메서드에서 부모 메서드 접근 가능
print(cc.parent_method())