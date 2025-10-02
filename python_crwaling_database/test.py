def func(x, y=[]):
    y.append(x)
    return y

print(func(1))
print(func(2))