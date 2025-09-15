class People():
    def make_instance(self):
        self.name = None
        self.age = None
        self.addr = None

h1 = People()
h1.make_instance()
print(h1.addr)
h2 = People()
print(h2.addr)