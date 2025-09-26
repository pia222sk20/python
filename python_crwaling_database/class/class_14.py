# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __init__
# 메소드 __str__  __eq__ __ne__ __lt__ __gt__ __le__ __ge__
# property  getter,setter,deleter, private --> 함수를 변수처럼 사용
# 객체생성

# 상품 클래스명  Product
# 상품명 product_name,가격 product_price,재고 product_stock

class Product:
    count = 0
    def __init__(self, product_name, product_price, product_stock):
        self.id = Product.count + 1
        Product.count += 1
        self.product_name = product_name
        self._product_price = product_price
        self._product_stock = product_stock
    @property
    def product_price(self):
        return self._product_price
    @product_price.setter
    def product_price(self, value):
        if value < 0:
            print("가격은 0보다 작을 수 없습니다.")
        else:
            self._product_price = value
    @property
    def product_stock(self):
        return self._product_stock
    @product_stock.setter
    def product_stock(self, value):
        if value < 0:
            print("재고는 0보다 작을 수 없습니다.")
        else:
            self._product_stock = value            

    def __str__(self):
        return f'상품명: {self.product_name}, \
        가격: {self.product_price}, 재고: {self.product_stock}'
    def __eq__(self, value):
        return self._product_stock == value._product_stock

products = [
    Product("노트북", 1000000, 10),
    Product("스마트폰", 500000, 20),
    Product("태블릿", 300000, 15)
]    
# 노트북의 가격을 20% 인하
for p in products:
    if p.product_name == '노트북':
        p.product_price = p.product_price * 0.8
# 스마트폰은 가격을 10% 인상
for p in products:
    if p.product_name == '스마트폰':
        p.product_price = p.product_price*0.1 + p.product_price
# 전체제품 출력
for p in products:
    print(p)
# 제품 추가
products.append('TV',200000,100)
# 제품 삭제 - 수량이 남아 있으면 삭제 못하게
del_productname = 'TV'
for idx, p in enumerate(products):
    if p.product_name == 'TV':
        del products[idx]
        break
# 현재 모든 재품의 수량의 합
totla_stock = 0
for p in products:
    totla_stock += p.product_stock
# 가격x 수량을 기준으로 같다 크다 크거나같다 작다 작거나같다
products[0] == products[1]