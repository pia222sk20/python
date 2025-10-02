
# 직원(Employee) 클래스
class Employee:
	def __init__(self, emp_id, name, base_salary=0):
		self.emp_id = emp_id
		self.name = name
		self.base_salary = base_salary
	def get_pay(self):
		return self.base_salary
	def __str__(self):
		return f"[직원] {self.emp_id} {self.name} 급여: {self.get_pay()}"

# 정규직(FullTimeEmployee) 클래스
class FullTimeEmployee(Employee):
	def __init__(self, emp_id, name, base_salary, bonus):
		super().__init__(emp_id, name, base_salary)
		self.bonus = bonus
	def get_pay(self):
		return self.base_salary + self.bonus
	def __str__(self):
		return f"[정규직] {self.emp_id} {self.name} 급여: {self.get_pay()} (기본급: {self.base_salary}, 보너스: {self.bonus})"

# 계약직(PartTimeEmployee) 클래스
class PartTimeEmployee(Employee):
	def __init__(self, emp_id, name, hourly_wage, hours):
		super().__init__(emp_id, name, 0)
		self.hourly_wage = hourly_wage
		self.hours = hours
	def get_pay(self):
		return self.hourly_wage * self.hours
	def __str__(self):
		return f"[계약직] {self.emp_id} {self.name} 급여: {self.get_pay()} (시급: {self.hourly_wage}, 시간: {self.hours})"

# 인턴(Intern) 클래스
class Intern(Employee):
	def __init__(self, emp_id, name, allowance):
		super().__init__(emp_id, name, 0)
		self.allowance = allowance
	def get_pay(self):
		return self.allowance
	def __str__(self):
		return f"[인턴] {self.emp_id} {self.name} 급여: {self.get_pay()} (고정수당: {self.allowance})"

# 다양한 직원 객체를 리스트에 저장
emp = [
	FullTimeEmployee('F001', '홍길동', 3000000, 500000),
	FullTimeEmployee('F002', '김철수', 2800000, 400000),
	PartTimeEmployee('P001', '이영희', 20000, 80),
	PartTimeEmployee('P002', '박민수', 18000, 100),
	Intern('I001', '최지우', 1000000),
	Intern('I002', '정해인', 900000)
]

# 직원 정보 출력
for e in emp:
	print(e)
