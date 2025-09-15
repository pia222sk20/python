# 파이썬 클래스에서 getter setter 사용법
import random
class Person:
    def __init__(self, name, age):
        self._name = name  # private 변수로 설정
        self._age = age    # private 변수로 설정
    # 데코레이터를 이용한 setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        self._age = age
p = Person("홍길동", 25)
print(p.name)
print(p.age)    
p.name = "김철수"
p.age = 30
