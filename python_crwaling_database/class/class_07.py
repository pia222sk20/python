class Dog:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # 인스턴스 변수 (각 인스턴스마다 다름)
        self.name = name
        self.age = age

# 인스턴스 생성
dog1 = Dog("바둑이", 2)
dog2 = Dog("초코", 5)

print("=== 클래스 변수 접근 ===")
print(f"dog1의 species: {dog1.species}")  # Canis familiaris
print(f"dog2의 species: {dog2.species}")  # Canis familiaris
print()

print("=== 인스턴스 변수 접근 ===")
print(f"dog1: 이름={dog1.name}, 나이={dog1.age}")  # 바둑이 2
print(f"dog2: 이름={dog2.name}, 나이={dog2.age}")  # 초코 5
print()

print("=== 클래스 변수 변경 (모든 인스턴스에 영향) ===")
Dog.species = "Canis lupus familiaris"
print(f"dog1의 species: {dog1.species}")  # Canis lupus familiaris
print(f"dog2의 species: {dog2.species}")  # Canis lupus familiaris
print()

print("=== 인스턴스 변수 변경 (해당 인스턴스에만 영향) ===")
dog1.age = 3
print(f"dog1: 이름={dog1.name}, 나이={dog1.age}")  # 3
print(f"dog2: 이름={dog2.name}, 나이={dog2.age}")  # 5