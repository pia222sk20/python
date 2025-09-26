# 클래스 변수 VS 인스턴스 변수

class StudentMng():
    name = '홍길동'  # 클래스변수    

s1 =  StudentMng() 
s2 =  StudentMng() 
s3 =  StudentMng() 

print(s1.name, s2.name,s3.name)
s1.name = '강감찬'  # 인스턴스 변수
StudentMng.name = '이순신'  # 클래스 변수
print(s1.name, s2.name,s3.name)

# 클래스변수는 모든 객체가 참조하는 변수
# but 객체가 변수를 재 할당받으면 해당객체는 더이상 참조하지 않는다
