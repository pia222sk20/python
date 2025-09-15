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
        return f'상품명: {self.product_name}, 가격: {self.product_price}, 재고: {self.product_stock}'